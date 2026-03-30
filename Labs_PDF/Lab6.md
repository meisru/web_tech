# Lab 6
Rudi Aleidan

## Task 1: Build HTML form template

Using the master template `apps/templates/layouts/base.html` from Lab4, I imported in `<head>` section the following:

```css
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
```

<br>

Then using the master template `apps/templates/layouts/base.html`, created a view function and URL `/books/search` to a page that contains the following HTML form in `apps/templates/bookmodule/search.html`:

```html
{% extends "layouts/base.html" %}
{% load static %}
{% block title %} Searching Page {% endblock title %}
{% block stylesheets %}
<style>
.searchForm{
  margin-top: 20px;
}
button {
  color: #fff;
  background-color: #17a2b8;
  border-color: #17a2b8;
  border: none;
  padding: 16px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 4px 2px;
  transition-duration: 0.4s;
  cursor: pointer;
}
button:hover {
  background-color: green;
  color: white;
}
</style>
{% endblock stylesheets %}
{% block content %}
<form class="searchForm" method="post" action="">
  {% csrf_token %}
  <label>Keywords:</label>
  <input type="text" name="keyword" placeholder="enter a keyword"/>
  <br/>
  <label>Search in:</label>
  <input type="checkbox" name="option1"/><label>Title</label>
  <input type="checkbox" name="option2"/><label>Author</label>
  <br/>
  <button type="submit"><i class="fa fa-search" aria-hidden="true"></i> Search</button>
</form>
{% endblock content %}
```

<br>

Output after running the server at `http://127.0.0.1:8000/books/search`:

![search form](Screenshots/l47.png)

## Task 2: Handle the form once submitted

In `apps/bookmodule/view.py`, created the following function:

```python
def __getBooksList():
    book1 = {'id':12344321, 'title':'Continuous Delivery', 'author':'J.Humble and D. Farley'}
    book2 = {'id':56788765,'title':'Reversing: Secrets of Reverse Engineering', 'author':'E. Eilam'}
    book3 = {'id':43211234, 'title':'The Hundred-Page Machine Learning Book', 'author':'Andriy Burkov'}
    return [book1, book2, book3]
```

<br>

Then in the same corresponding view/controller in `views.py` that shows the form, added the code where if there is an action in the form, the form needs to be handled in that view.

```python
def search(request):
    if request.method == "POST":
        string = request.POST.get('keyword').lower()
        isTitle = request.POST.get('option1')
        isAuthor = request.POST.get('option2')
        books = __getBooksList()
        newBooks = []
        for item in books:
            contained = False
            if isTitle and string in item['title'].lower(): contained = True
            if not contained and isAuthor and string in item['author'].lower(): contained = True
            if contained: newBooks.append(item)
        return render(request, 'bookmodule/bookList.html', {'books': newBooks})
    return render(request, 'bookmodule/search.html')
```

<br>

Then created an HTMl file `bookList.html` to list the books:

```html
{% extends "layouts/base.html" %}
{% load static %}
{% block title %} Search Results {% endblock title %}
{% block content %}
<h1>Search Results</h1>
{% if books %}
  {% for book in books %}
    <div>
      <h2>{{ book.title }}</h2>
      <p>Author: {{ book.author }}</p>
      <p>ID: {{ book.id }}</p>
    </div>
    <hr>
  {% endfor %}
{% else %}
  <p>No books found.</p>
{% endif %}
<a href="{% url 'books.search' %}">Back to Search</a>
{% endblock content %}
```

<br>

Output at `http://127.0.0.1:8000/books/search`:

![search results](Screenshots/l48.png)