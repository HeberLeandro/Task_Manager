from ..models import Task


def register_task(task):
    Task.objects.create(title=task.title, description=task.description,
                        expiration_date=task.expiration_date, priority=task.priority)


def list_tasks():
    return Task.objects.all()


def list_task_id(id):
    return Task.objects.get(id=id)


def edit_task(task_db, new_task):
    task_db.title = new_task.title
    task_db.description = new_task.description
    task_db.expiration_date = new_task.expiration_date
    task_db.priority = new_task.priority
    task_db.save(force_update=True)


def remove_task(task_db):
    task_db.delete()
