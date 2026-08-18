from django import forms
from django.utils import timezone

from todo.models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ("content", "deadline", "tags", "is_completed")

    def clean_deadline(self):
        deadline = self.cleaned_data.get("deadline")

        if not deadline:
            return deadline

        if self.instance and self.instance.pk:
            if deadline < self.instance.created_at:
                raise forms.ValidationError(
                    f"Deadline cannot be earlier than the task creation time "
                    f"({self.instance.created_at.strftime('%Y-%m-%d %H:%M')})."
                )
        else:
            if deadline < timezone.now():
                raise forms.ValidationError(
                    "Deadline cannot be earlier than the current time."
                )

        return deadline