"""
GitHub Model Module
"""
class GithubModel:
    """
    GitHub Model Class
    """
    def __init__(self, login_name, login_id, url) -> None:
        """
        GithubModel constructor

        Parameters:
        login (String): GitHub User or Organisation Name
        id (int): GitHub User or Organisation ID
        url (String): GitHub Repository URL

        Returns: None
        """
        self.login =  login_name
        self.id = login_id
        self.url = url
