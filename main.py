from icinga_api import IcingaApi
import requests

api = IcingaApi("http://localhost", "a", "b")

try:
    api.hosts.get("A!B")
except ValueError as ex:
    print(ex)

try:
    api.services.get("A")
except ValueError as ex:
    print(ex)

try:
    api.services.get("A!B!C")
except ValueError as ex:
    print(ex)

try:
    api.notifications.get("A")
except ValueError as ex:
    print(ex)

try:
    api.notifications.get("A!B!C!D")
except ValueError as ex:
    print(ex)

try:
    api.hosts.get("A")
except requests.ConnectionError:
    pass

try:
    api.services.get("A!B")
except requests.ConnectionError:
    pass

try:
    api.notifications.get("A!B!C")
except requests.ConnectionError:
    pass
