# TODO List App

A simple task management web application built with Django.

## Features

- Create, update, and delete tasks
- Set an optional deadline for each task
- Mark tasks as completed / undo completion
- Organize tasks with tags
- Tasks ordered by status (not done first) and creation date (newest first)
- Deadline validation — cannot be set earlier than task creation time or current time

## Tech Stack

- Python 3
- Django
- SQLite

## Project Structure

```
todolist/               ← project root
├── todolist/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── todo/               ← main app
    ├── static/
    │   └── css/
    │       └── stiles.css
    ├── templates/
    │   ├── base.html
    │   ├── includes/
    │   │   └── sidebar.html
    │   └── todo/
    │       ├── index.html
    │       ├── tag_list.html
    │       ├── create_update_form.html
    │       └── confirm_delete.html
    ├── admin.py
    ├── forms.py
    ├── models.py
    ├── tests.py
    ├── urls.py
    └── views.py
```

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd todolist
```

2. Create and activate a virtual environment:
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install django
```

4. Apply migrations:
```bash
python manage.py migrate
```

5. Create a superuser (optional, for admin panel):
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

Open `http://127.0.0.1:8000/` in your browser.

## URL Routes

| URL | Name | Description |
|-----|------|-------------|
| `/` | `todo:index` | Home page — task list |
| `/task/create/` | `todo:task-create` | Create a new task |
| `/task/<pk>/update/` | `todo:task-update` | Edit a task |
| `/task/<pk>/delete/` | `todo:task-delete` | Delete a task |
| `/task/<pk>/toggle_complete/` | `todo:toggle-complete` | Toggle task status (POST only) |
| `/tags/` | `todo:tag-list` | Tag list |
| `/tag/create/` | `todo:tag-create` | Create a new tag |
| `/tag/<pk>/update/` | `todo:tag-update` | Edit a tag |
| `/tag/<pk>/delete/` | `todo:tag-delete` | Delete a tag |
| `/admin/` | — | Django admin panel |

## Models

**Task**

| Field | Type | Description |
|-------|------|-------------|
| `content` | TextField | Task description |
| `created_at` | DateTimeField | Set automatically on creation |
| `deadline` | DateTimeField | Optional deadline |
| `is_completed` | BooleanField | Completion status, default `False` |
| `tags` | ManyToManyField | Related tags |

**Tag**

| Field | Type | Description |
|-------|------|-------------|
| `name` | CharField | Tag name |

## Validation

`TaskForm` validates the `deadline` field:

- **Create** — deadline must not be earlier than the current time
- **Update** — deadline must not be earlier than the task's `created_at`

## Running Tests

```bash
python manage.py test todo
```

The test suite covers:

- `TaskForm` deadline validation on create and update
- `toggle_complete` view — status toggling, redirect, GET safety
- `Task` model — `__str__` output and ordering
- `Tag` model — `__str__` output
- `IndexView` — response status, template, content