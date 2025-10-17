"""
GitHub API Client class & helper functions
"""
import json
import pandas as pd
import requests
from .github_model import GithubModel


def get_data_frame_from_json(json_response):
    """
    Converts JSON to DataFrame

    Parameters:
    json_response: Raw JSON Response from GitHub API Call

    Returns:
    df (DataFrame): Contains information for each repo
    """
    df = pd.DataFrame(json_response)
    return df


class GitHubClient:
    """
    GitHub client
    """
    def __init__(self, api_endpoint, token='', is_pretty=False) -> None:
        """
        GitHubClient constructor

        Parameters:
        api_endpoint (String): URL to call
        token (String that defaults to empty string): Auth Token
        is_pretty (Boolean): Enable/Disable Pretty Print of JSON data in the logs

        Returns: None
        """
        self.url =  f"https://api.github.com/users/{api_endpoint}/repos?per_page=100&page=1"
        self.api_token = token
        self.is_pretty = is_pretty

    def do_get(self):
        """
        Calls Client URL via HTTP GET Method

        Parameters:
        self: instance of GitHubClient

        Returns:
        json_response (Raw JSON Response or None): GitHub Response Body JSON
        """
        response = requests.get(self.url)
        if response.ok:
            json_response = json.loads(response.text or response.content)
            return json_response
        return None

    def main(self):
        """
        Clients main method & logic

        Parameters:
        self: instance of GitHubClient

        Returns:
        result_dict (Dictionary): Dict with
            Key: Row/Repository Index
            Value: Dict {login username, login ID, project/repository URL}
        """
        # GET JSON data
        result = self.do_get()
        if self.is_pretty:
            print(json.dumps(result, indent=4))

        # parse JSON to data frame
        df = get_data_frame_from_json(result)

        # Map response DF to model object
        result_dict = {}
        for index, row in df.iterrows():
            owner = GithubModel(row.owner['login'], row.owner['id'], row.html_url)
            result_dict[index+1] = json.dumps(owner, default=lambda o: o.__dict__)
        return result_dict
