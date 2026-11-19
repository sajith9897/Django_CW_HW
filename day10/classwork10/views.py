from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .models import Book
from .forms import BookForm


# Display books with pagination
def book_list(request):
    books = Book.objects.all().order_by('id')

    paginator = Paginator(books, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'classwork10/book_list.html', {
        'page_obj': page_obj
    })


# Add new book
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()

    return render(request, 'classwork10/book_form.html', {
        'form': form,
        'heading': 'Add Book'
    })


# Edit existing book
def edit_book(request, id):
    book = get_object_or_404(Book, id=id)

    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)

        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)

    return render(request, 'classwork10/book_form.html', {
        'form': form,
        'heading': 'Edit Book'
    })


# Delete book
def delete_book(request, id):
    book = get_object_or_404(Book, id=id)

    if request.method == 'POST':
        book.delete()
        return redirect('book_list')

    return render(request, 'classwork10/book_delete.html', {
        'book': book
    })