#%%
import yaml
import requests
from requests.auth import HTTPBasicAuth
from confluencecommandline.util import *
import argparse

def run(args):

    config = args.config

    # quickly check the yaml file
    with open(config, 'r') as stream:
        print(f"[create-skeleton] Checking configuration file {config}...")
        try:
            yaml_config = yaml.load(stream)
            print(yaml_config)
        except yaml.YAMLError as exc:
            print(exc)

    # check for the required elements
    host     = get_config_value(yaml_config, "host")
    username = get_config_value(yaml_config, "username")
    api_key  = get_config_value(yaml_config, "api_key")
    space    = get_config_value(yaml_config, "space")

    if args.space:
        space = args.space

    if args.username:
        username = args.username

    if args.api_key:
        api_key = args.api_key

    params = [
        (host, "host", "[ERROR] Please enter a valid host for your Confluence Cloud Installation."),
        (username, "username", "[ERROR] Please enter a valid username."),
        (api_key, "api_key", "[ERROR] Please enter a valid api key."),
        (space, "space", "[ERROR] Please enter a valid space name.")
    ]

    for k, _, m in params:
        if k is None:
            print(m)
            exit(1)

    api_config = APIConfig(host, space, username, api_key)

    print("[create-skeleton] OK")
    print("[create-skeleton] Checking Space Exists...")

    if not space_exists(api_config):
        print("[ERROR] Space doesn't exist or credentials are invalid. Please check and try again.")
        exit(1)

    print("[create-skeleton] Downloading current pages...")
    current_pages = get_current_pages(api_config)

    print("[create-skeleton] Found {} pages".format(len(current_pages)))

    # first extract a list of all potential pages to create
    all_pages = extract_pages_from_config(yaml_config)
    all_pages_unique    = set(all_pages)

    print("[create-skeleton] Checking pages are unique...")
    if not(len(all_pages) == len(all_pages_unique)):
        print("[ERROR] {} pages are not unique. All pages in a confluence space must have unique titles.".format(len(all_pages) - len(all_pages_unique)))
        exit(1)

    print("[create-skeleton] Checking for existing page conflicts...")
    # if any page exists
    for p in all_pages_unique:
        if p in current_pages:
            print(f"[ERROR] Page {p} currently exists within that space. Please rename your new page.")
            exit(1)

    print("[create-skeleton] OK, creating pages...")
    for p in yaml_config:
        if "page" in p:
            create_hierarchy(p, None, api_config)
