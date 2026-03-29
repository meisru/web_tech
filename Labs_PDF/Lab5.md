# Lab 5
By Rudi Aleidan

## Task 1: Links and layout customization

In `apps/static/main.css` is the new CSS file with styles for the 3 link blocks (padding, text center, text color, background color, display block) and :hover, :active, and :visited for each link:

```css
#link-new-tab {
    display: block;
    padding: 20px;
    text-align: center;
    background-color: #90EE90;
    color: #cc0000;
    text-decoration: underline;
}

#link-same-tab {
    display: block;
    padding: 20px;
    text-align: center;
    background-color: #444444;
    color: #FFA500;
    text-decoration: underline;
}

#link-visited {
    display: block;
    padding: 20px;
    text-align: center;
    background-color: #000000;
    color: #ffffff;
    text-decoration: underline;
}

/* Link states */
#link-new-tab:hover,
#link-same-tab:hover,
#link-visited:hover {
    color: #ff1a1a;
}

#link-new-tab:active {
    color: #990000;
}

#link-new-tab:visited {
    color: #555555;
}

#link-same-tab:active {
    color: #ff8800;
}

#link-same-tab:visited {
    color: #555555;
}

#link-visited:active {
    color: #aaaaaa;
}

#link-visited:visited {
    color: #555555;
}
```

<br>
In `apps/templates/bookmodule/links.html` is the new template that contains 3 links. 
The first link opens in a new tab (`target="_blank"`), the other two open in the same tab:

```html
{% extends "layouts/base.html" %}
{% load static %}
{% block title %}Links Page{% endblock title %}
{% block stylesheets %}
<link rel="stylesheet" href="{% static 'main.css' %}">
{% endblock stylesheets %}
{% block content %}
<a id="link-new-tab" href="https://www.qu.edu.sa/" target="_blank">Go to QU website (open a new tab)</a>
<a id="link-same-tab" href="https://www.qu.edu.sa/">Go to QU website (open in the same page/tab)</a>
<a id="link-visited" href="https://www.qu.edu.sa/">Go to QU website (open in the same page/tab)</a>
{% endblock content %}
```

<br>
In `apps/bookmodule/views.py` the `links` view was added:

```python
from django.shortcuts import render

def index(request):
    return render(request, "bookmodule/index.html")

def list_books(request):
    return render(request, 'bookmodule/list_books.html')

def viewbook(request, bookId):
    return render(request, 'bookmodule/one_book.html')

def aboutus(request):
    return render(request, 'bookmodule/aboutus.html')

def links(request): # Here
    return render(request, 'bookmodule/links.html')
```

<br>
In `apps/bookmodule/urls.py` the URL `html5/links` was added to the urlpatterns list:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name= "books.index"),
    path('list_books/', views.list_books, name= "books.list_books"),
    path('<int:bookId>/', views.viewbook, name="books.view_one_book"),
    path('aboutus/', views.aboutus, name="books.aboutus"),
    path('html5/links', views.links, name="books.links"),
]
```

<br>
The output at `http://127.0.0.1:8000/books/html5/links`:

![](Screenshots/l41.png)

Hovering over the links:

![](Screenshots/l42.png)

Visited state:

![](Screenshots/l43.png)

## Task 2: Text formatters (nested formatters)

In `apps/static/main.css` the `#formatting-heading` style was added for the h1 tag (green italic text, light yellow-green background):

```css
#formatting-heading {
    color: #2e7d00;
    background-color: #f0f4d8;
    padding: 10px 20px;
    font-style: italic;
}
```

<br>
In `apps/templates/bookmodule/text_formatting.html` is the new template that extends `base.html`, loads `main.css`, and displays 10 formatting tags:

```html
{% extends "layouts/base.html" %}
{% load static %}
{% block title %}Text Formatting{% endblock title %}
{% block stylesheets %}
<link rel="stylesheet" href="{% static 'main.css' %}">
{% endblock stylesheets %}
{% block content %}
<h1 id="formatting-heading">Example of Formatting tags</h1>
<p>This text has <b>subtext</b> using b tag</p>
<p>This text has <strong>subtext</strong> using strong tag</p>
<p>This text has <i>subtext</i> using i tag</p>
<p>This text has <em>subtext</em> using emphasize tag</p>
<p>This text has <small>subtext</small> using small tag</p>
<p>This text has <mark>subtext</mark> using mark tag</p>
<p>This text has <del>subtext</del> using del tag</p>
<p>This text has <ins>subtext</ins> using ins tag</p>
<p>This text has X<sub>subtext</sub> using sub tag</p>
<p>This text has X<sup>subtext</sup> using sup tag</p>
{% endblock content %}
```

<br>
In `apps/bookmodule/views.py` the `text_formatting` view was added:

```python
def text_formatting(request): # Here
    return render(request, 'bookmodule/text_formatting.html')
```

<br>
In `apps/bookmodule/urls.py` the URL `html5/text/formatting` was added to the urlpatterns list:

```python
path('html5/text/formatting', views.text_formatting, name="books.text_formatting"),
```

<br>
The output at `http://127.0.0.1:8000/books/html5/text/formatting`:

![](Screenshots/l44.png)

## Task 3: Listing (nested)