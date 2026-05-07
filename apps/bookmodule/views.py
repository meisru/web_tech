from django.shortcuts import render, redirect
from .forms import BookForm
from django.db.models import Q, Count, Sum, Avg, Max, Min, Subquery, OuterRef
from .models import Book, Publisher, Author
from apps.usermodule.models import Address

def index(request):
    return render(request, "bookmodule/index.html")

def list_books(request):
    return render(request, 'bookmodule/list_books.html')

def viewbook(request, bookId):
    return render(request, 'bookmodule/one_book.html')

def aboutus(request):
    return render(request, 'bookmodule/aboutus.html')

def links(request):
    return render(request, 'bookmodule/links.html')

def text_formatting(request):
    return render(request, 'bookmodule/text_formatting.html')

def listing(request):
    return render(request, 'bookmodule/listing.html')

def tables(request):
    return render(request, 'bookmodule/tables.html')

def __getBooksList():
    book1 = {'id':12344321, 'title':'Continuous Delivery', 'author':'J.Humble and D. Farley'}
    book2 = {'id':56788765,'title':'Reversing: Secrets of Reverse Engineering', 'author':'E. Eilam'}
    book3 = {'id':43211234, 'title':'The Hundred-Page Machine Learning Book', 'author':'Andriy Burkov'}
    return [book1, book2, book3]

def simple_query(request):
    mybooks = Book.objects.filter(title__icontains='and') # <- multiple objects
    return render(request, 'bookmodule/bookList.html', {'books':mybooks})

# def complex_query(request):  # broken: uses removed fields author, edition
#     mybooks=books=Book.objects.filter(author__isnull = False).filter(title__icontains='and').filter(edition__gte = 2).exclude(price__lte = 100)[:10]
#     if len(mybooks)>=1:
#         return render(request, 'bookmodule/bookList.html', {'books':mybooks})
#     else:
#         return render(request, 'bookmodule/index.html')

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

def lab8_task1(request):
    mybooks = Book.objects.filter(Q(price__lte=80))
    return render(request, 'bookmodule/lab8_task1.html', {'books': mybooks})

# def lab8_task2(request):  # broken: uses removed fields edition, author
#     mybooks = Book.objects.filter(Q(edition__gt=3) & (Q(title__icontains='qu') | Q(author__icontains='qu')))
#     return render(request, 'bookmodule/lab8_task2.html', {'books': mybooks})

# def lab8_task3(request):  # broken: uses removed fields edition, author
#     mybooks = Book.objects.filter(~Q(edition__gt=3) & ~(Q(title__icontains='qu') | Q(author__icontains='qu')))
#     return render(request, 'bookmodule/lab8_task3.html', {'books': mybooks})

def lab8_task4(request):
    mybooks = Book.objects.all().order_by('title')
    return render(request, 'bookmodule/lab8_task4.html', {'books': mybooks})

def lab8_task5(request):
    stats = Book.objects.aggregate(
        count=Count('id'),
        total_price=Sum('price'),
        avg_price=Avg('price'),
        max_price=Max('price'),
        min_price=Min('price'),
    )
    return render(request, 'bookmodule/lab8_task5.html', {'stats': stats})

def lab8_task7(request):
    cities = Address.objects.annotate(student_count=Count('student'))
    return render(request, 'bookmodule/lab8_task7.html', {'cities': cities})

def lab9_task1(request):
    total = Book.objects.aggregate(total=Sum('quantity'))['total'] or 1
    mybooks = Book.objects.all()
    for book in mybooks:
        book.percentage = round((book.quantity / total) * 100, 2)
    return render(request, 'bookmodule/lab9_task1.html', {'books': mybooks})

def lab9_task2(request):
    publishers = Publisher.objects.annotate(total_stock=Sum('book__quantity'))
    return render(request, 'bookmodule/lab9_task2.html', {'publishers': publishers})

def lab9_task3(request):
    oldest_title = Book.objects.filter(
        publisher=OuterRef('pk')
    ).order_by('pubdate').values('title')[:1]

    oldest_pubdate = Book.objects.filter(
        publisher=OuterRef('pk')
    ).order_by('pubdate').values('pubdate')[:1]

    publishers = Publisher.objects.annotate(
        oldest_book=Subquery(oldest_title),
        oldest_pubdate=Subquery(oldest_pubdate),
    )
    return render(request, 'bookmodule/lab9_task3.html', {'publishers': publishers})

def lab9_task4(request):
    publishers = Publisher.objects.annotate(
        avg_price=Avg('book__price'),
        min_price=Min('book__price'),
        max_price=Max('book__price'),
    )
    return render(request, 'bookmodule/lab9_task4.html', {'publishers': publishers})

def lab9_task5(request):
    publishers = Publisher.objects.annotate(
        highly_rated_count=Count('book', filter=Q(book__rating__gte=4))
    ).filter(highly_rated_count__gt=0)
    return render(request, 'bookmodule/lab9_task5.html', {'publishers': publishers})

def lab9_task6(request):
    publishers = Publisher.objects.annotate(
        book_count=Count('book', filter=Q(book__price__gt=50) & Q(book__quantity__gte=1) & Q(book__quantity__lt=5))
    ).filter(book_count__gt=0)
    return render(request, 'bookmodule/lab9_task6.html', {'publishers': publishers})

# Lab 10 Part 1 – CRUD (no Django forms)

def lab10_part1_listbooks(request):
    books = Book.objects.all()
    return render(request, 'bookmodule/lab10_part1_listbooks.html', {'books': books})

def lab10_part1_addbook(request):
    if request.method == 'POST':
        title     = request.POST.get('title')
        price     = request.POST.get('price')
        quantity  = request.POST.get('quantity')
        pubdate   = request.POST.get('pubdate')
        rating    = request.POST.get('rating')
        author_id = request.POST.get('author_id')
        authorObj = Author.objects.get(id=author_id)
        obj = Book(title=title, price=float(price), quantity=int(quantity),
                   pubdate=pubdate or None, rating=int(rating))
        obj.save()
        obj.authors.add(authorObj)
        return redirect('books.lab10_part1_listbooks')
    authors = Author.objects.all()
    return render(request, 'bookmodule/lab10_part1_addbook.html', {'authors': authors})

def lab10_part1_editbook(request, bookId):
    book = Book.objects.get(id=bookId)
    if request.method == 'POST':
        book.title    = request.POST.get('title')
        book.price    = float(request.POST.get('price') or 0)
        book.quantity = int(request.POST.get('quantity') or 1)
        book.pubdate  = request.POST.get('pubdate') or None
        book.rating   = int(request.POST.get('rating') or 1)
        author_id     = request.POST.get('author_id')
        authorObj     = Author.objects.get(id=author_id)
        book.save()
        book.authors.set([authorObj])
        return redirect('books.lab10_part1_listbooks')
    authors = Author.objects.all()
    return render(request, 'bookmodule/lab10_part1_editbook.html', {'book': book, 'authors': authors})

def lab10_part1_deletebook(request, bookId):
    Book.objects.filter(id=bookId).delete()
    return redirect('books.lab10_part1_listbooks')

# Lab 10 Part 2 – CRUD with Django forms

def lab9_part2_listbooks(request):
    books = Book.objects.all()
    return render(request, 'bookmodule/lab9_part2_listbooks.html', {'books': books})

def lab9_part2_addbook(request):
    obj = None
    authors = Author.objects.all()
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            obj = form.save()
            obj.authors.add(form.cleaned_data['author'])
            return redirect('books.lab9_part2_listbooks')
    else:
        form = BookForm(None)
    return render(request, 'bookmodule/lab9_part2_addbook.html', {'authors': authors, 'form': form})

def lab9_part2_editbook(request, bookId):
    book = Book.objects.get(id=bookId)
    authors = Author.objects.all()
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            obj = form.save()
            obj.authors.set([form.cleaned_data['author']])
            return redirect('books.lab9_part2_listbooks')
    else:
        form = BookForm(instance=book)
    return render(request, 'bookmodule/lab9_part2_editbook.html', {'authors': authors, 'form': form, 'book': book})

def lab9_part2_deletebook(request, bookId):
    Book.objects.filter(id=bookId).delete()
    return redirect('books.lab9_part2_listbooks')