# Lab 8
Rudi Aleidan

## Task 1

- `apps/bookmodule/urls.py` — added route:
  ```python
  path('lab8/task1', views.lab8_task1, name="books.lab8_task1"),
  ```

- `apps/bookmodule/views.py` — imported `Q` and added view at the bottom:
  ```python
  from django.db.models import Q

  def lab8_task1(request):
      mybooks = Book.objects.filter(Q(price__lte=80))
      return render(request, 'bookmodule/lab8_task1.html', {'books': mybooks})
  ```

- `apps/templates/bookmodule/lab8_task1.html` — new template that displays the filtered books, with an `{% empty %}` fallback if none are found.
    ```html
    {% extends "layouts/base.html" %}
    {% block title %} Lab8 Task1 {% endblock title %}
    {% block content %}
    <h1>Books with Price &le; 80</h1>
    {% for book in books %}
    ID: {{ book.id }}, Title: {{ book.title }}, Author: {{ book.author }}, Price: {{ book.price }}, Edition: {{ book.edition }}
    <hr>
    {% empty %}
    <p>No books found with price less than or equal to 80.</p>
    {% endfor %}
    {% endblock content %}
    ```

Output at `http://localhost:8000/books/lab8/task1`:
![lab8_task1_output.png](Screenshots/l55.png)

## Task 2

## Task 3

## Task 4

## Task 5

## Task 6

## Task 7