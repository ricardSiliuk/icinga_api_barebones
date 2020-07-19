from typing import List, Optional
from requests import Session


class IcingaObject:
    SEPARATOR = "!"
    BASE_URL = "http://localhost:5665/api/v1"

    def __init__(self, session: Session, path: Optional[str] = None):
        self.session: Session = session
        self.url = "/".join([IcingaObject.BASE_URL, path])

    def get(self, object_fqdn: str):
        full_url = "/".join([self.url, object_fqdn])
        print(f"Calling GET {full_url} for {self.__class__.__name__}")
        return self.session.get(full_url)

    def post(self, object_fqdn: str, data=None):
        full_url = "/".join([self.url, object_fqdn])
        print(f"Calling POST {full_url} for {self.__class__.__name__}")
        return self.session.post(full_url, data=data)
