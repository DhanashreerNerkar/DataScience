import requests

def get_github_profile_info(username):
    user_api = f"https://api.github.com/users/{username}"
    repos_api = f"https://api.github.com/users/{username}/repos"

    headers = {
        'Accept': 'application/vnd.github+json'
    }

    # Fetch user profile data
    user_resp = requests.get(user_api, headers=headers)
    if user_resp.status_code != 200:
        print(f"Failed to fetch user data: {user_resp.status_code}")
        return

    user_data = user_resp.json()
    print(f"📄 Profile Info for: {username}")
    print(f"Name: {user_data.get('name')}")
    print(f"Bio: {user_data.get('bio')}")
    print(f"Location: {user_data.get('location')}")
    print(f"Company: {user_data.get('company')}")
    print(f"Email: {user_data.get('email')}")
    print(f"Blog: {user_data.get('blog')}")
    print(f"Public Repos: {user_data.get('public_repos')}")
    print(f"Followers: {user_data.get('followers')}")
    print(f"Following: {user_data.get('following')}")
    print("\n Repositories and Projects:\n")

    # Fetch repositories
    repos_resp = requests.get(repos_api, headers=headers)
    if repos_resp.status_code != 200:
        print(f"Failed to fetch repositories: {repos_resp.status_code}")
        return

    repos = repos_resp.json()
    for repo in repos:
        print(f"Repo Name: {repo['name']}")
        print(f"  Description: {repo.get('description')}")
        print(f"  Language: {repo.get('language')}")
        print(f"  Stars: {repo.get('stargazers_count')}")
        print(f"  Forks: {repo.get('forks_count')}")
        print(f"  URL: {repo.get('html_url')}\n")

get_github_profile_info("DhanashreerNerkar")
