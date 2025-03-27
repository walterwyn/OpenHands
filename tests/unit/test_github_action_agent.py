import unittest
from unittest.mock import patch, MagicMock
from openhands.agenthub.github_action_agent.github_action_agent import GitHubActionAgent

class TestGitHubActionAgent(unittest.TestCase):

    @patch('openhands.agenthub.github_action_agent.github_action_agent.requests.post')
    @patch('openhands.agenthub.github_action_agent.github_action_agent.open', create=True)
    def test_run(self, mock_open, mock_post):
        # Mock the environment variables
        with patch.dict('os.environ', {'GITHUB_REPOSITORY': 'test/repo', 'GITHUB_TOKEN': 'test_token'}):
            agent = GitHubActionAgent()

            # Mock the file write
            mock_file = MagicMock()
            mock_open.return_value.__enter__.return_value = mock_file

            # Mock the post request
            mock_response = MagicMock()
            mock_response.raise_for_status.return_value = None
            mock_post.return_value = mock_response

            # Run the agent
            agent.run()

            # Check if the file was written correctly
            mock_open.assert_called_once_with('.github/workflows/github-action-agent.yml', 'w')
            mock_file.write.assert_called_once()

            # Check if the post request was made correctly
            mock_post.assert_called_once_with(
                'https://api.github.com/repos/test/repo/actions/workflows/github-action-agent.yml/dispatches',
                headers={
                    'Authorization': 'token test_token',
                    'Accept': 'application/vnd.github.v3+json'
                },
                json={'ref': 'main'}
            )

if __name__ == '__main__':
    unittest.main()
