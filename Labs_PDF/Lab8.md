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

- `apps/bookmodule/urls.py` — added route:
  ```python
  path('lab8/task2', views.lab8_task2, name="books.lab8_task2"),
  ```

- `apps/bookmodule/views.py` — added view at the bottom:
  ```python
  def lab8_task2(request):
      mybooks = Book.objects.filter(Q(edition__gt=3) & (Q(title__icontains='qu') | Q(author__icontains='qu')))
      return render(request, 'bookmodule/lab8_task2.html', {'books': mybooks})
  ```

- `apps/templates/bookmodule/lab8_task2.html` — new template displaying the filtered books, with an `{% empty %}` fallback if none are found.
  ```html
  {% extends "layouts/base.html" %}
  {% block title %} Lab8 Task2 {% endblock title %}
  {% block content %}
  <h1>Books with Edition &gt; 3 and Title or Author Contains 'qu'</h1>
  {% for book in books %}
    ID: {{ book.id }}, Title: {{ book.title }}, Author: {{ book.author }}, Price: {{ book.price }}, Edition: {{ book.edition }}
    <hr>
  {% empty %}
    <p>No books found matching the criteria.</p>
  {% endfor %}
  {% endblock content %}
  ```

Output at `http://localhost:8000/books/lab8/task2`:
![lab8_task2_output.png](Screenshots/l56.png)

## Task 3

- `apps/bookmodule/urls.py` — added route:
  ```python
  path('lab8/task3', views.lab8_task3, name="books.lab8_task3"),
  ```

- `apps/bookmodule/views.py` — added view at the bottom:
  ```python
  def lab8_task3(request):
      mybooks = Book.objects.filter(~Q(edition__gt=3) & ~(Q(title__icontains='qu') | Q(author__icontains='qu')))
      return render(request, 'bookmodule/lab8_task3.html', {'books': mybooks})
  ```

- `apps/templates/bookmodule/lab8_task3.html` — new template displaying the filtered books, with an `{% empty %}` fallback if none are found.
  ```html
  {% extends "layouts/base.html" %}
  {% block title %} Lab8 Task3 {% endblock title %}
  {% block content %}
  <h1>Books with Edition &le; 3 and Title and Author Do Not Contain 'qu'</h1>
  {% for book in books %}
    ID: {{ book.id }}, Title: {{ book.title }}, Author: {{ book.author }}, Price: {{ book.price }}, Edition: {{ book.edition }}
    <hr>
  {% empty %}
    <p>No books found matching the criteria.</p>
  {% endfor %}
  {% endblock content %}
  ```

Output at `http://localhost:8000/books/lab8/task3`:
![lab8_task3_output.png](Screenshots/l57.png)

## Task 4

## Task 5

## Task 6

## Task 7