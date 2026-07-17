"""
Lab: Singleton & Factory Patterns (Creational)
Course: Software Engineering (24PCA402)

Task:
1. Implement a Singleton so only one instance of a class ever exists.
2. Implement a Factory that returns different Notification objects
   based on a type string, without the caller knowing the concrete class.
"""


class Singleton:
    """Only one instance of this class can ever exist."""
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self, config_name="default"):
        if not self._initialized:
            self.config_name = config_name
            self._initialized = True


class Notification:
    def send(self, message):
        raise NotImplementedError


class EmailNotification(Notification):
    def send(self, message):
        return f"[EMAIL] {message}"


class SMSNotification(Notification):
    def send(self, message):
        return f"[SMS] {message}"


class PushNotification(Notification):
    def send(self, message):
        return f"[PUSH] {message}"


class NotificationFactory:
    """Creates the right Notification subclass from a type string."""

    _types = {
        "email": EmailNotification,
        "sms": SMSNotification,
        "push": PushNotification,
    }

    @classmethod
    def create(cls, notification_type):
        notification_cls = cls._types.get(notification_type.lower())
        if notification_cls is None:
            raise ValueError(f"Unknown notification type: {notification_type}")
        return notification_cls()


if __name__ == "__main__":
    a = Singleton("primary")
    b = Singleton("secondary")
    print("Singleton identity check:", a is b, "| config:", a.config_name)

    for kind in ("email", "sms", "push"):
        notifier = NotificationFactory.create(kind)
        print(notifier.send("Assignment deadline moved to Friday."))
