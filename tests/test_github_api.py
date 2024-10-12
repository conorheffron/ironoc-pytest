import json
from src.ironoc_pytest_conorheffron.github_api import GitHubClient

def test_github_api_conorheffron_success():
    # given
    hubspotClient = GitHubClient('conorheffron')

    # when
    result = hubspotClient.main()

    # then
    print(json.dumps(result, sort_keys=True, indent=4))
    assert result != None

def test_github_api_meta_success():
    # given
    hubspotClient = GitHubClient('meta')

    # when
    result = hubspotClient.main()

    # then
    print(json.dumps(result, sort_keys=True, indent=4))
    assert result != None

def test_github_api_ibm_cloud_success():
    # given
    hubspotClient = GitHubClient('IBM-Cloud')

    # when
    result = hubspotClient.main()

    # then
    print(json.dumps(result, sort_keys=True, indent=4))
    assert result != None