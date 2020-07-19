from icinga_api.objects.icinga_object import IcingaObject


class Notification(IcingaObject):
    URL_RESOURCE_PATH = "notifications"

    def __init__(self, session):
        super().__init__(session, Notification.URL_RESOURCE_PATH)

    def get(self, object_fqdn: str):
        self.__validate_fqdn__(object_fqdn)
        return super().get(object_fqdn)

    def __validate_fqdn__(self, object_fqdn: str) -> None:
        if "!" not in object_fqdn:
            raise ValueError(
                f"Notification Object FQDN must contain at least single '!' ({object_fqdn})"
            )
        if object_fqdn.count("!") > 2:
            raise ValueError(
                f"Notification Object FQDN can't contain more than two '!' ({object_fqdn})"
            )
