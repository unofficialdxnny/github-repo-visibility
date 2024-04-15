# github-repo-visibility

This Python script provides a convenient way to toggle the visibility of a GitHub repository between "public" and "private" using your personal access token.

----

## Features
- Simple and Effective: Easily change repository visibility with a single command.
- Error Handling: Provides informative messages if changes fail or repository - details cannot be fetched.
- API Integration: Smoothly interacts with the GitHub API.

## How to Use

1. Get a Personal Access Token:
    - 
    - Go to your GitHub settings > Developer Settings > Personal Access Tokens.
    - Generate a new token with the "repo" scope selected.

2. Replace Placeholders:
    - 

    - Open the script and replace the following:

    - `YOUR_GITHUB_USERNAME` with your GitHub username.

    - `YOUR_PERSONAL_ACCESS_TOKEN` with your generated token.

    - `https://api.github.com/repos/username/repo_name` with the API URL of the repository you want to modify.

3. Install Dependencies:
    -
    -Make sure you have the `requests` library: `pip install requests`

4. Run the script:
    - 
    - From your terminal, execute python `main.py`