import pytest
import tasks
from tasks import Task

def test_get_single(tasks_db):
  tasks.add(Task('Wake up', 'yattom'))
  single_task = tasks.get_sigle()
  assert isinstance(single_task, Task)


