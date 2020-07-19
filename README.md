# Object-Oriented Icinga2 Python API

Purpose of this library is to provide an easier access to Icinga API for maintenance while having an interface that is more user friendly.

For example, consider such previous usage:

```python
from icinga_api import IcingaApi

api = IcingaApi("hostname", "username", "password", "rkey")
status, response = api.get("host", "A")
```

with newer usage that explicitly provides group of objects we want to query:

```python
from icinga_api import IcingaApi

api = icinga_api.IcingaApi("hostname", "username", "password", "rkey")
api.hosts.get("A")

```

Along with providing cleaner implementation, this might help provide

* cleaner API via usage of inheritance
* object-specific interfaces
* cleaner CLI via better error handling
