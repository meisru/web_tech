# Lab 9
Rudi Aleidan

## Task 1

Created URL `/books/lab9/task1` that lists all books with their percentage availability out of total stock, using a transient field on the `Book` model.

**Files changed:**

- `apps/bookmodule/models.py` — added `percentage` as a transient (non-DB) field on `Book`:
  ```python
  class Book(models.Model):
      ...
      percentage = None  # transient field, not stored in DB
  ```

- `apps/bookmodule/urls.py` — added route:
  ```python
  path('lab9/task1', views.lab9_task1, name="books.lab9_task1"),
  ```

- `apps/bookmodule/views.py` — added view at the bottom:
  ```python
  def lab9_task1(request):
      total = Book.objects.aggregate(total=Sum('quantity'))['total'] or 1
      mybooks = Book.objects.all()
      for book in mybooks:
          book.percentage = round((book.quantity / total) * 100, 2)
      return render(request, 'bookmodule/lab9_task1.html', {'books': mybooks})
  ```

- `apps/templates/bookmodule/lab9_task1.html` — new template displaying each book's title, quantity, and availability percentage.
  ```html
  {% extends "layouts/base.html" %}
  {% block title %} Lab9 Task1 {% endblock title %}
  {% block content %}
  <h1>Books Availability</h1>
  {% for book in books %}
    Title: {{ book.title }}, Quantity: {{ book.quantity }}, Availability: {{ book.percentage }}%
    <hr>
  {% empty %}
    <p>No books found.</p>
  {% endfor %}
  {% endblock content %}
  ```

Output at `http://localhost:8000/books/lab9/task1`:
![lab9_task1_output.png](Screenshots/l61.png)

## Task 2

## Task 3

## Task 4

## Task 5

## Task 6

## Task 7
