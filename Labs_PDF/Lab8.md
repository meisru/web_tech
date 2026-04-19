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

- `apps/bookmodule/urls.py` — added route:
  ```python
  path('lab8/task4', views.lab8_task4, name="books.lab8_task4"),
  ```

- `apps/bookmodule/views.py` — added view at the bottom:
  ```python
  def lab8_task4(request):
      mybooks = Book.objects.all().order_by('title')
      return render(request, 'bookmodule/lab8_task4.html', {'books': mybooks})
  ```

- `apps/templates/bookmodule/lab8_task4.html` — new template displaying books sorted by title, with an `{% empty %}` fallback if none are found.
  ```html
  {% extends "layouts/base.html" %}
  {% block title %} Lab8 Task4 {% endblock title %}
  {% block content %}
  <h1>Books Ordered by Title</h1>
  {% for book in books %}
    ID: {{ book.id }}, Title: {{ book.title }}, Author: {{ book.author }}, Price: {{ book.price }}, Edition: {{ book.edition }}
    <hr>
  {% empty %}
    <p>No books found.</p>
  {% endfor %}
  {% endblock content %}
  ```

Output at `http://localhost:8000/books/lab8/task4`:
![lab8_task4_output.png](Screenshots/l58.png)

## Task 5

Created URL `/books/lab8/task5` that displays aggregated book statistics (count, total, average, max, and min price) using Django aggregation functions.

**Files changed:**

- `apps/bookmodule/urls.py` — added route:
  ```python
  path('lab8/task5', views.lab8_task5, name="books.lab8_task5"),
  ```

- `apps/bookmodule/views.py` — imported aggregation functions and added view at the bottom:
  ```python
  from django.db.models import Q, Count, Sum, Avg, Max, Min

  def lab8_task5(request):
      stats = Book.objects.aggregate(
          count=Count('id'),
          total_price=Sum('price'),
          avg_price=Avg('price'),
          max_price=Max('price'),
          min_price=Min('price'),
      )
      return render(request, 'bookmodule/lab8_task5.html', {'stats': stats})
  ```

- `apps/templates/bookmodule/lab8_task5.html` — new template displaying the aggregated statistics.
  ```html
  {% extends "layouts/base.html" %}
  {% block title %} Lab8 Task5 {% endblock title %}
  {% block content %}
  <h1>Book Statistics</h1>
  <p>Number of Books: {{ stats.count }}</p>
  <p>Total Price: {{ stats.total_price }}</p>
  <p>Average Price: {{ stats.avg_price }}</p>
  <p>Maximum Price: {{ stats.max_price }}</p>
  <p>Minimum Price: {{ stats.min_price }}</p>
  {% endblock content %}
  ```

Output at `http://localhost:8000/books/lab8/task5`:
![lab8_task5_output.png](Screenshots/l59.png)

## Task 6

## Task 7