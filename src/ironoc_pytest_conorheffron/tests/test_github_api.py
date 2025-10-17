"""
GitHub Client Test Suite
"""
import json
from ironoc_pytest_conorheffron.github_api import GitHubClient

def test_github_api_conorheffron_success():
    """
    Test GitHub client for user 'conorheffron'
    """
    # given
    git_hub_client = GitHubClient('conorheffron')

    # when
    result = git_hub_client.main()

    # then
    print(json.dumps(result, sort_keys=True, indent=4))
    assert result is not None

def test_github_api_meta_success():
    """
    Test GitHub client for organization 'meta'
    """
    # given
    git_hub_client = GitHubClient('meta')

    # when
    result = git_hub_client.main()

    # then
    print(json.dumps(result, sort_keys=True, indent=4))
    assert result is not None

def test_github_api_ibm_cloud_success():
    """
    Test GitHub client for organization 'IBM-Cloud'
    """
    # given
    git_hub_client = GitHubClient('IBM-Cloud')

    # when
    result = git_hub_client.main()

    # then
    print(json.dumps(result, sort_keys=True, indent=4))
    assert result is not None
