from django.test import TestCase
from django.utils import timezone
from datetime import timedelta

from todo.models import Task


class ModelTests(TestCase):
    def setUp(self):
        self.now = timezone.now()
        self.future = self.now + timedelta(days=1)

        self.task_with_deadline = Task.objects.create(
            content="test_content_with_deadline",
            deadline=self.future,
            is_completed=False,
        )

        self.task_without_deadline = Task.objects.create(content="test_content", is_completed=False)

    def test_task_with_deadline_str(self):
        self.assertEqual(
            str(self.task_with_deadline),
            f"Task {self.task_with_deadline.pk}:"
            f" created at-{self.task_with_deadline.created_at}, "
            f"content - {self.task_with_deadline.content}. "
            f"DEADLINE - {self.task_with_deadline.deadline}",
        )

    def test_task_without_deadline_str(self):
        self.assertEqual(
            str(self.task_without_deadline),
            f"Task {self.task_without_deadline.pk}:"
            f" created at-{self.task_without_deadline.created_at}, "
            f"content - {self.task_without_deadline.content}.",
        )

    def test_ordering_not_done_first(self):
        Task.objects.create(content="done", is_completed=True)
        Task.objects.create(content="not done", is_completed=False)
        first = Task.objects.first()
        self.assertFalse(first.is_completed)

    def test_ordering_done_last(self):
        Task.objects.create(content="done", is_completed=True)
        Task.objects.create(content="not done", is_completed=False)
        last = Task.objects.last()
        self.assertTrue(last.is_completed)
