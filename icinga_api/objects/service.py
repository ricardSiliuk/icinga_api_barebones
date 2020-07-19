from icinga_api.objects.icinga_object import IcingaObject


class Service(IcingaObject):
    URL_RESOURCE_PATH = "services"

    def __init__(self, session):
        super().__init__(session, Service.URL_RESOURCE_PATH)

    def get(self, object_fqdn: str):
        self.__validate_fqdn__(object_fqdn)
        super().get(object_fqdn)

    def __validate_fqdn__(self, object_fqdn: str):
        if "!" not in object_fqdn:
            raise ValueError(
                f"Service Object FQDN must contain single '!' ({object_fqdn})"
            )
        if object_fqdn.count("!") > 1:
            raise ValueError(
                f"Service Object FQDN can't contain more than one '!' ({object_fqdn})"
            )
