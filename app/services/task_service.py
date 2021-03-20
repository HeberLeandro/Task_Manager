from ..models import Task


def register_task(task):
    Task.objects.create(title=task.title, description=task.description,
                        expiration_date=task.expiration_date, priority=task.priority)
