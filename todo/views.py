from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic

from todo.models import Tag, Task


class TagListView(generic.ListView):
    model = Tag
    template_name = "todo/tag_list.html"

class TagCreateView(generic.CreateView):
    model = Tag
    fields = ("name",)
    success_url = reverse_lazy("todo:tag-list")
    template_name = "todo/create_update_form.html"

class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = ("name",)
    success_url = reverse_lazy("todo:tag-list")
    template_name = "todo/create_update_form.html"

class TagDeleteView(generic.DeleteView):
    model = Tag
    template_name = "todo/confirm_delete.html"
    success_url = reverse_lazy("todo:tag-list")


class IndexView(generic.ListView):
    model = Task
    template_name = "todo/index.html"

class TaskCreateView(generic.CreateView):
    model = Task
    fields = ("content", "deadline", "tags", "is_completed")
    success_url = reverse_lazy("todo:index")
    template_name = "todo/create_update_form.html"

class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = ("content", "deadline", "tags", "is_completed")
    success_url = reverse_lazy("todo:index")
    template_name = "todo/create_update_form.html"

class TaskDeleteView(generic.DeleteView):
    model = Task
    template_name = "todo/confirm_delete.html"
    success_url = reverse_lazy("todo:index")


def toggle_complete(request, pk):
    if request.method == "POST":
        task = Task.objects.get(id=pk)
        task.is_completed = not task.is_completed
        task.save()
    return HttpResponseRedirect(reverse_lazy("todo:index"))







