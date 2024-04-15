import requests
from requests.auth import HTTPBasicAuth

# *********************************************
#  IMPORTANT: Replace placeholders with your info
# *********************************************
YOUR_GITHUB_USERNAME = ""
YOUR_PERSONAL_ACCESS_TOKEN = ""
REPO_URL = "https://api.github.com/repos/username/repo_name" 
# *********************************************


def toggle_repo_visibility(repo_url, token):
    headers = {
    "Accept": "application/vnd.github.v3+json",
    "Authorization": "token {}".format(token)
    }

    response = requests.get(repo_url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        current_visibility = data['visibility']

        new_visibility = 'private' if current_visibility == 'public' else 'public'

        patch_response = requests.patch(repo_url, headers=headers, json={'visibility': new_visibility})

        if patch_response.status_code == 200:
            print("Repository visibility changed to %s" % new_visibility) 
        else:
            print("Failed to change visibility. Status code: %s" % patch_response.status_code)
    else:
        print("Error: Could not fetch repository details. Status code %s:" % response.status_code)


if __name__ == "__main__":
    toggle_repo_visibility(REPO_URL, YOUR_PERSONAL_ACCESS_TOKEN) 
