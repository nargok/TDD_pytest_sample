import pytest
import tasks
from tasks import Task

def test_get_most_urgent(tasks_db):
  tasks.add(Task('Wake up', 'yattom'))
  tasks.add(Task('Eat', 'yattom'))
  tasks.add(Task('Sleep', 'yattom'))
  urgent_task = tasks.get_most_urgent()
  assert urgent_task.summary == 'Wake up'

