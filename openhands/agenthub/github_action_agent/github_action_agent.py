import os
import requests
from openhands.controller.agent import BaseAgent

class GitHubActionAgent(BaseAgent):
    def run(self):
        # Create a GitHub Action job
        self.create_github_action_job()

        # Run the GitHub Action job
        self.run_github_action_job()

    def create_github_action_job(self):
        # Define the GitHub Action job
        job = {
            "name": "Run GitHub Action",
            "on": {
                "push": {
                    "branches": ["main"]
                }
            },
            "jobs": {
                "build": {
                    "runs-on": "ubuntu-latest",
                    "steps": [
                        {
                            "name": "Checkout repository",
                            "uses": "actions/checkout@v4"
                        },
                        {
                            "name": "Set up Python",
                            "uses": "actions/setup-python@v5",
                            "with": {
                                "python-version": "3.12"
                            }
                        },
                        {
                            "name": "Install dependencies",
                            "run": "pip install poetry && poetry install"
                        },
                        {
                            "name": "Run tests",
                            "run": "poetry run pytest"
                        }
                    ]
                }
            }
        }

        # Save the job to a file
        with open(".github/workflows/github-action-agent.yml", "w") as f:
            f.write(job)

    def run_github_action_job(self):
        # Trigger the GitHub Action job
        url = f"https://api.github.com/repos/{os.getenv('GITHUB_REPOSITORY')}/actions/workflows/github-action-agent.yml/dispatches"
        headers = {
            "Authorization": f"token {os.getenv('GITHUB_TOKEN')}",
            "Accept": "application/vnd.github.v3+json"
        }
        data = {
            "ref": "main"
        }
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
