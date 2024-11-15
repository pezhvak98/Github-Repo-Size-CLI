
# GitHub Repository Size CLI Tool

A simple CLI tool to fetch and display the size of a GitHub repository. This tool also allows you to set and update your GitHub API token globally, so you don't need to enter it every time.

## Features

- Fetch the size of any public GitHub repository.
- Display the repository size in a human-readable format (KB, MB, GB).
- Optionally clone the repository after fetching its size.
- Set and update your GitHub API token globally for ease of use.

## Installation

### Install the Tool and All Prerequisites

To install this tool and all the required dependencies, simply run the installation script:

```bash
chmod +x install.sh
sudo ./install.sh
```
This will:

-   Install Python 3, `pip`, and `git` (if not already installed).
-   Install the required Python dependencies.
-   Create a symlink for the tool so it can be used globally from anywhere in your terminal.

Once the script finishes, the tool is installed, and you can run it with the `grs` command.

## Setting up Your GitHub API Token

### Step 1: Obtain Your GitHub API Token

Before using the tool, you need to set your GitHub API token. Follow these steps to generate your GitHub token:

1.  Go to GitHub and log in to your account.
2.  Navigate to **Settings** > **Developer settings** > **Personal access tokens**.
3.  Click **Generate new token**.
4.  Provide a name for the token, select the required scopes (for repository access, at least `repo` is needed), and then click **Generate token**.
5.  Copy the generated token. **Important**: You won't be able to see it again once you leave the page.

### Step 2: Set the GitHub API Token in the Tool

Once you have your token, you can set it globally using the tool. Run the following command:
```bash
grs --set-token <your-github-api-token>
```
This will store your GitHub API token in a global file (`~/.github_token`), so you won't need to enter it again in the future.

## Using the Tool

### Fetch Repository Size

To fetch the size of a repository, simply run:
```bash
grs https://github.com/owner/repository.git
```
Replace `owner` and `repository` with the actual GitHub repository details. The tool will display the repository size in a human-readable format (KB, MB, or GB).

Example output:
```bash
Size of repository owner/repo: 2.44 MB
```
### Clone the Repository (Optional)

After fetching the repository size, you will be asked if you'd like to clone the repository:
```bash
Do you want to clone the repository 'https://github.com/owner/repository.git'? (y/n):
```
Type `y` to clone the repository or `n` to skip cloning.

### Update Your Token (if needed)

If you need to update your GitHub API token (e.g., if it expires), run the following command:
```bash
grs --update-token
```
You will be prompted to enter your new token.

---
### Key Points: 
1. **Installation:** The script `install.sh` will handle everything related to installing prerequisites (like `Python3`, `pip`, and `git`). 
2. **GitHub API Token:** There is a detailed section on how to obtain and set the `GitHub API token`. 
3. **Tool Usage:** Clear instructions on how to use the tool, set the token, fetch repository sizes, clone repos, and update the token.