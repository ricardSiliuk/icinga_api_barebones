from icinga_api.objects.icinga_object import IcingaObject


class Host(IcingaObject):
    URL_RESOURCE_PATH = "hosts"

    def __init__(self, session):
        super().__init__(session, Host.URL_RESOURCE_PATH)

    def get(self, object_fqdn: str):
        self.__validate_fqdn__(object_fqdn)
        return super().get(object_fqdn)

    def __validate_fqdn__(self, object_fqdn):
        if "!" in object_fqdn:
            raise ValueError(f"Host Object FQDN cannot contain '!' ({object_fqdn})")
