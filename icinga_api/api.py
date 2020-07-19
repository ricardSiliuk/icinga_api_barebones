from icinga_api.objects import *
import requests


class IcingaApi:
    def __init__(self, url: str, username: str, password: str):
        self.session = requests.Session()
        self.session.auth = (username, password)
        self.session.headers.update({"content-type": "application/json"})
        self.url = url
        self.hosts = Host(self.session)
        self.services = Service(self.session)
        self.notifications = Notification(self.session)
