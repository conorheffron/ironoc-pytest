import json
from ironoc_pytest_conorheffron.github_api import GitHubClient

def test_github_api_conorheffron_success():
    # given
    gitHubClient = GitHubClient('conorheffron')

    # when
    result = gitHubClient.main()

    # then
    print(json.dumps(result, sort_keys=True, indent=4))
    assert result != None

def test_github_api_meta_success():
    # given
    gitHubClient = GitHubClient('meta')

    # when
    result = gitHubClient.main()

    # then
    print(json.dumps(result, sort_keys=True, indent=4))
    assert result != None

def test_github_api_ibm_cloud_success():
    # given
    gitHubClient = GitHubClient('IBM-Cloud')

    # when
    result = gitHubClient.main()

    # then
    print(json.dumps(result, sort_keys=True, indent=4))
    assert result != None
