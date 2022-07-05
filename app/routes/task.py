from flask import Blueprint
from ..controller import controller_task

task = Blueprint("task", __name__)

LIST_URL = '/api/todo-list'


@task.route(LIST_URL, methods=["GET"])
def index():
    return controller_task.find_all_task()


@task.route(LIST_URL, methods=["POST"])
def list_task():
    return controller_task.create_task()


@task.route(f'{LIST_URL}/<id>', methods=["PUT"])
def edit_taks(id):
    return controller_task.update_task(id)


@task.route(f'{LIST_URL}/<id>', methods=["DELETE"])
def delete_task(id):
    return controller_task.delete_task(id)
