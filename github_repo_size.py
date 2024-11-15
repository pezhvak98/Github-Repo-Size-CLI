#!/usr/bin/env python3



import os
import json
import subprocess
import requests
import argparse



TOKEN_FILE = os.path.expanduser('~/.github_token')  # Store the token in the home directory

COLORS = {
    'green': '\033[92m',
    'red': '\033[91m',
    'reset': '\033[0m',
    'brown-orange': '\033[0;33m'
}

def load_token():
    #Load the token from the persistent storage file in the home directory (~/.github_token).
    if os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE, 'r') as f:
            return f.read().strip() 
    return None

def save_token(token):
    #Save the token to the persistent storage file in the home directory (~/.github_token).
    with open(TOKEN_FILE, 'w') as f:
        f.write(token)
    print(f"{COLORS['green']}GitHub API token saved successfully in {TOKEN_FILE}.{COLORS['reset']}")

def set_token(token):
    
    save_token(token)
    print(f"{COLORS['green']}API token saved successfully.{COLORS['reset']}")

def update_token():
    
    new_token = input(f"{COLORS['green']}Enter your new GitHub API token: {COLORS['reset']}")
    set_token(new_token)
    print(f"{COLORS['green']}Token has been updated successfully!{COLORS['reset']}")

def format_size(size_kb):
    if size_kb < 1000:
        return f"{size_kb} KB"
    elif size_kb < 1000000:  # Less than 1 GB
        size_mb = size_kb / 1024
        return f"{size_mb:.2f} MB"
    else:  # 1 GB or more
        size_gb = size_kb / (1024 * 1024)
        return f"{size_gb:.2f} GB"

def get_repo_size(owner, repo):

    token = load_token()  # Load the token from the global file

    if not token:
        print(f"{COLORS['red']}GitHub API token is not set. Please set the token using '--set-token <TOKEN>'.{COLORS['reset']}")
        return

    url = f'https://api.github.com/repos/{owner}/{repo}'
    headers = {'Authorization': f'token {token}'}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        data = response.json()
        size_kb = data.get('size', 0)  # Repository size in kilobytes
        formatted_size = format_size(size_kb)  # Format the size in KB/MB/GB

        print(f"{COLORS['green']}Size of repository {owner}/{repo}: {formatted_size}{COLORS['reset']}")

        # Ask the user if they want to clone the repository
        clone_repo(data['clone_url'])

    except requests.exceptions.HTTPError as e:
        if response.status_code == 404:
            print(f"{COLORS['red']}Repository not found.{COLORS['reset']}")
        elif response.status_code == 401:
            print(f"{COLORS['red']}Invalid or expired token.{COLORS['reset']}")
        else:
            print(f"{COLORS['red']}HTTP Error: {e}{COLORS['reset']}")
    except requests.exceptions.RequestException as e:
        print(f"{COLORS['red']}Error fetching repository details: {e}{COLORS['reset']}")

def clone_repo(repo_url):
    answer = input(f"Do you want to clone the repository '{repo_url}'? (y/n): ").strip().lower()
    if answer == 'y':
        try:
            print(f"{COLORS['green']}Cloning repository...{COLORS['reset']}")
            subprocess.run(['git', 'clone', repo_url], check=True)
            print(f"{COLORS['green']}Repository cloned successfully.{COLORS['reset']}")
        except subprocess.CalledProcessError:
            print(f"{COLORS['red']}Failed to clone the repository. Make sure 'git' is installed and accessible.{COLORS['reset']}")
    elif answer == 'n':
        print(f"{COLORS['brown-orange']}Skipping repository cloning.{COLORS['reset']}")
    else:
        print(f"{COLORS['red']}Invalid input. Please enter 'y' or 'n'.{COLORS['reset']}")

def parse_repo_url(repo_url):

    if repo_url.startswith("https://github.com/") and repo_url.endswith(".git"):
        parts = repo_url.split('/')
        if len(parts) >= 5:
            owner = parts[3]
            repo = parts[4][:-4]  # Remove the `.git` suffix
            return owner, repo
    return None, None

def main():
    
    # Main function to handle CLI arguments and workflow.
    
    parser = argparse.ArgumentParser(
        description='A CLI tool to fetch and display the size of GitHub repositories.',
        epilog='Developed by Pezhvak with ❤️',
    )
    parser.add_argument('repo_url', nargs='?', help='The URL of the GitHub repository.')
    parser.add_argument('--set-token', dest='set_token', help='Set the GitHub API token.', metavar='TOKEN')
    parser.add_argument('--update-token', dest='update_token', action='store_true', help='Update the GitHub API token.')

    args = parser.parse_args()

   
    if args.update_token:
        update_token()
        return

    token = load_token() 

    if not token and args.set_token is None:
        print(f"{COLORS['red']}GitHub API token is not set. Please set the token first using '--set-token <TOKEN>'.{COLORS['reset']}")
        return

    if args.set_token:
        set_token(args.set_token)
        return

    if args.repo_url:
        owner, repo = parse_repo_url(args.repo_url)
        if owner and repo:
            get_repo_size(owner, repo)
        else:
            print(f"{COLORS['red']}Invalid repository URL. Ensure it ends with '.git'.{COLORS['reset']}")
    else:
        print(f"{COLORS['red']}No repository URL provided. Use '--help' for usage details.{COLORS['reset']}")

if __name__ == "__main__":
    main()
