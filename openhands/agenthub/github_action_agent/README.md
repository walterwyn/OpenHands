# GitHubActionAgent

The `GitHubActionAgent` is a specialized agent designed to create and run GitHub Action jobs. This agent can be used to automate workflows and tasks within a GitHub repository.

## Purpose

The primary purpose of the `GitHubActionAgent` is to facilitate the creation and execution of GitHub Action jobs. This can be particularly useful for automating repetitive tasks, running tests, deploying applications, and more.

## Usage

To use the `GitHubActionAgent`, follow these steps:

1. **Initialize the Agent**: Create an instance of the `GitHubActionAgent` class.
2. **Run the Agent**: Call the `run` method to create and run a GitHub Action job.

### Example

Here is an example of how to configure and run the `GitHubActionAgent`:

```python
from openhands.agenthub.github_action_agent.github_action_agent import GitHubActionAgent

# Initialize the agent
agent = GitHubActionAgent()

# Run the agent
agent.run()
```

## Configuration

The `GitHubActionAgent` can be configured using environment variables. The following environment variables are required:

- `GITHUB_REPOSITORY`: The GitHub repository in the format `owner/repo`.
- `GITHUB_TOKEN`: A GitHub token with the necessary permissions to create and run workflows.

## Workflow File

The `GitHubActionAgent` creates a GitHub Actions workflow file named `github-action-agent.yml` in the `.github/workflows` directory. This file defines the job to be executed.

## Dependencies

The `GitHubActionAgent` requires the following dependencies:

- `requests`: Used to make HTTP requests to the GitHub API.
- `openhands`: The main OpenHands package.

Make sure to install these dependencies before running the agent.

## Notes

- Ensure that the GitHub token provided has the necessary permissions to create and run workflows.
- The agent is designed to work with Python 3.12 and Poetry for dependency management.
