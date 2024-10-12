import json
from .github_model import GithubModel
import pandas as pd
import requests

class GitHubClient(object):

    def __init__(self, api_endpoint, token='', is_pretty=False) -> None:
        self.url =  f"https://api.github.com/users/{api_endpoint}/repos?per_page=100&page=1"
        self.api_token = token
        self.is_pretty = is_pretty

    def do_get(self):
        response = requests.get(self.url)
        if(response.ok):
            jsonResponse = json.loads(response.text or response.content)
            return jsonResponse
        return None

    def get_data_frame_from_json(self, json):
        df = pd.DataFrame(json)
        return df

    def main(self):
        # GET JSON data
        result = self.do_get()
        if self.is_pretty:
            print(json.dumps(result, indent=4))

        # parse JSON to data frame
        df = self.get_data_frame_from_json(result)

        # Map response DF to model object
        result_dict = {}
        for index, row in df.iterrows():
            owner = GithubModel(row.owner['login'], row.owner['id'], row.html_url)
            result_dict[index+1] = json.dumps(owner, default=lambda o: o.__dict__)
        return result_dict
