"""
Lab: Observer Pattern (Behavioral)
Course: Software Engineering (24PCA402)

Task: Build a publish/subscribe notification system where multiple
observers react automatically whenever a subject's state changes.
"""


class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self, event):
        for observer in self._observers:
            observer.update(event)


class Observer:
    def update(self, event):
        raise NotImplementedError


class GradePublished(Subject):
    """Fires an event whenever a new grade is posted."""

    def post_grade(self, student, grade):
        self.notify({"student": student, "grade": grade})


class EmailAlert(Observer):
    def update(self, event):
        print(f"[EMAIL] {event['student']}: grade posted -> {event['grade']}")


class DashboardWidget(Observer):
    def __init__(self):
        self.history = []

    def update(self, event):
        self.history.append(event)
        print(f"[DASHBOARD] refreshed with {len(self.history)} record(s)")


class AuditLog(Observer):
    def update(self, event):
        print(f"[AUDIT] logged grade change for {event['student']}")


if __name__ == "__main__":
    board = GradePublished()
    board.attach(EmailAlert())
    board.attach(DashboardWidget())
    board.attach(AuditLog())

    board.post_grade("A. Rao", "A")
    board.post_grade("K. Shetty", "B+")
