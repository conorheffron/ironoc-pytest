"""
GitHub Model Object
"""
class GithubModel:

    def __init__(self, login, id, url) -> None:
        """
        GithubModel constructor

        Parameters:
        login (String): GitHub User or Organisation Name
        id (int): GitHub User or Organisation ID
        url (String): RGotHub Repository URL

        Returns: None
        """
        self.login =  login
        self.id = id
        self.url = url
