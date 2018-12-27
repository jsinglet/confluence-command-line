# Confluence Command Line (ccl)

Confluence Command Line (`ccl`) is a suite of command line utilities designed to make working with confluence faster and easier. 

# Installation 

```
pip install confluence-command-line
```

This will install the binary `ccl`, which will allow you to execute the various confluence command line utilities. 

# create-skeleton

Creating hierarchies of pages in Confluence is time consuming and error prone. The `create-skeleton` command is a is for creating confluence structures quickly and easily. 

Using `create-skeleton` is simple: just write up your structure (with optional content attributes) and run the tool over your `yml` file. 


## Example 

1. Create `.yml` file containing the structure you'd like to create. You'll have to set `host`, `username`, `api_key`, and `space`. Don't have an API key? Get one here: https://id.atlassian.com/manage/api-tokens


```yaml
- host: <your_cloud_host>
- username: <your_username>
- api_key: <key>

- space: <my_space_key>

- page: RootA
  content: "This is my content"
  children:
    - page: Child A1
      children:
      - page: Child A11
      - page: Child A12
      - page: Child A13
        children:
        - page: Child A111
        - page: Child A112
        - page: Child A113
          children:
          - page: Child A1111
          - page: Child A1112
          - page: Child A1113

    - page: Child A2
    - page: Child A3

- page: RootB
  children:
    - page: Child B1
    - page: Child B2
    - page: Child B3
```

2. Run the tool. Example usage:

```
ccl create-skeleton myfile.yml
```

# Feedback and Contributions

Feedback and contributions are welcome! Please open an issue or a pull request to get in touch. 
