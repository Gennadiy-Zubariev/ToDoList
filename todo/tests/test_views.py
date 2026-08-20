from django.test import TestCase, Client
from django.urls import reverse
from django.utils import timezone
from datetime import timedelta


from todo.models import Task


class ToggleCompleteViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.now = timezone.now()
        self.future = self.now + timedelta(days=1)
        self.task_completed = Task.objects.create(
            content="test_content_completed",
            deadline=self.future,
            is_completed=True,
        )
        self.task_in_completed = Task.objects.create(
            content="test_content_in_completed",
            deadline=self.future,
            is_completed=False,
        )

    def _url(self, pk):
        return reverse("todo:toggle-complete", args=[pk])

    def test_toggle_false_to_true(self):
        task = self.task_in_completed
        self.client.post(self._url(task.pk))
        task.refresh_from_db()
        self.assertTrue(task.is_completed)

    def test_toggle_true_to_false(self):
        task = self.task_completed
        self.client.post(self._url(task.pk))
        task.refresh_from_db()
        self.assertFalse(task.is_completed)

    def test_toggle_twice_returns_original_status(self):
        task = self.task_in_completed
        url = self._url(task.pk)
        self.client.post(url)
        self.client.post(url)
        task.refresh_from_db()
        self.assertFalse(task.is_completed)
