# Library Project

A Django web application for managing a library, built as part of the **Web Techniques** university course.

## Setup

1. Clone the repository and navigate to the project directory.
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
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
5. Run the development server:
   ```bash
   python manage.py runserver
   ```

## Project Structure

```
libraryproject/
├── apps/
│   ├── bookmodule/   # Book catalog app
│   ├── usermodule/   # User management app
│   ├── static/       # Static files
│   └── templates/    # HTML templates
├── libraryproject/   # Project settings
├── manage.py
└── Labs_PDF/          # Course labs documentation
```

## Requirements

- Python 3.x
- Django