from django.test import TestCase
from django.utils import timezone
from datetime import timedelta

from todo.forms import TaskForm


class TaskFormTests(TestCase):
    def setUp(self):
        self.now = timezone.now()
        self.future = self.now + timedelta(days=1)
        self.past = self.now - timedelta(days=1)

    def test_task_form_create_with_valid_deadline(self):
        form = TaskForm(data={"content": "test", "deadline": self.future})
        self.assertTrue(form.is_valid())

    def test_task_form_create_with_past_deadline(self):
        form = TaskForm(data={"content": "test", "deadline": self.past})
        self.assertFalse(form.is_valid())

    def test_task_form_create_without_deadline(self):
        form = TaskForm(data={"content": "test"})
        self.assertTrue(form.is_valid())
