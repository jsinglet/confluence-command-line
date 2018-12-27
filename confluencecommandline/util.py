import yaml
import requests
from requests.auth import HTTPBasicAuth


class APIConfig:
    def __init__(self, host, space, username, api_key):
        self.host = host
        self.space = space
        self.username = username
        self.api_key = api_key
        self.creds = HTTPBasicAuth(username, api_key)



def extract_pages_from_root(root):

    pages = [root['page']]

    if 'children' in root:
        for p in root['children']:
            pages = pages + extract_pages_from_root(p)

    return pages


def extract_pages_from_config(yaml_config):
    pages = []

    for e in yaml_config:
        if 'base_page' in e:
            pages.append(e['base_page'])

        elif 'page' in e:
            pages = pages + extract_pages_from_root(e)


    return pages


def get_current_pages(config : APIConfig, next_uri = None):

    if next_uri is None:
        response = requests.get(f"https://{config.host}/wiki/rest/api/space/{config.space}/content", auth=config.creds)
    else:
        response = requests.get(next_uri, auth=config.creds)

    data = response.json()

    titles = []

    if "page" in data:
        base = data["page"]
    else:
        base = data

    for page in base["results"]:
        titles.append(page["title"])

    if "next" in base["_links"]:
        return titles + get_current_pages(
            config,
            data["_links"]["base"] + base["_links"]["next"]
            )

    return titles

def get_config_value(c, key):

    for e in c:
        if key in e:
            return e[key]

    return None

def space_exists(config : APIConfig):

    response = requests.get(f"https://{config.host}/wiki/rest/api/space/{config.space}", auth=config.creds)

    if response.status_code == 200:
        return True

    #print(response.json())
    return False


def create_page(title, parent, content, config : APIConfig):

    print(f"Creating page {title} with parent {parent}")

    _data = {"type": "page",
            "title": f"{title}",
            "space": {"key": f"{config.space}"},
            "body" : {"storage":
                         {
                             "value": f"{content}",
                             "representation": "storage"
                         }
                     }
            }

    if parent is not None:
        children_data = [{"id": parent}]
        _data["ancestors"] = children_data

    response = requests.post(f"https://{config.host}/wiki/rest/api/content", json=_data, auth=config.creds)

    return response.json()["id"]


def create_hierarchy(root, parent, config : APIConfig):

    # create parent
    if "content" in root:
        content = root["content"]
    else:
        content = ""

    _parent = create_page(root["page"], parent, content, config)

    # visit children
    if 'children' in root:
        for p in root['children']:
            create_hierarchy(p, _parent, config)

