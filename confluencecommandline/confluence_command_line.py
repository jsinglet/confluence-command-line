import argparse
from confluencecommandline.commands import create_skeleton

def main():
    parser = argparse.ArgumentParser(
        prog="ccl",
        description='Confluence command utilities.'
    )

    parser.add_argument("command", type=str, choices=["create-skeleton"], help="Command to execute")
    parser.add_argument("--space", help="The space to create the pages in.")
    parser.add_argument("--api_key", help="The API Key to use.")
    parser.add_argument("--username", help="The username to use.")

    parser.add_argument("config", help="The YAML configuration to process.")

    args = parser.parse_args()

    if args.command == "create-skeleton":
        create_skeleton.run(args)


if __name__ == "__main__":
    main()
