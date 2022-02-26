from django.shortcuts import render, redirect

from online_library.web.forms import CreateProfileForm, AddBookForm, EditProfileForm, EditBookForm
from online_library.web.models import Profile, Book


def get_profile():
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]

    return None


def create_profile(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = CreateProfileForm()
    context = {
        'form': form,
        'no_profile': True,
    }
    return render(request, 'home-no-profile.html', context)


def show_index(request):
    profile = get_profile()
    if not profile:
        return redirect('create profile')
    books = Book.objects.all()
    book_count = len(books)
    books_matrix = []
    # for i in range(len(books)):
    #     books_matrix[i].append([i])
    #     for j in books:
    #         books_matrix[i].append(j)
    context = {
        'profile': profile,
        'books': books,
        'book_count': book_count
        # 'books_matrix': books_matrix,
    }

    return render(request, 'home-with-profile.html', context)


def add_book(request):
    profile = get_profile()
    if request.method == 'POST':
        form = AddBookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = AddBookForm()
    context = {
        'form': form,
        'profile': profile,
    }
    return render(request, 'add-book.html', context)


def edit_book(request, pk):
    book = Book.objects.get(pk=pk)
    profile = get_profile()
    if request.method == 'POST':
        form = EditBookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = EditBookForm(instance=book)
    context = {
        'form': form,
        "book": book,
        'profile': profile,
    }
    return render(request, 'edit-book.html', context)


def book_details(request, pk):
    book = Book.objects.get(pk=pk)
    profile = get_profile()

    context = {
        'book': book,
        'profile': profile,
    }
    return render(request, 'book-details.html', context)


def profile(request):
    profile = get_profile()
    books = Book.objects.all()

    context = {
        'profile': profile,
        'books': books,
    }
    return render(request, 'profile.html', context)


def edit_profile(request):
    profile = get_profile()
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = EditProfileForm(instance=profile)
    context = {
        'form': form,
        "profile": profile,
    }
    return render(request, 'edit-profile.html', context)


def delete_profile(request):
    instance_profile = get_profile()
    books = Book.objects.all()
    Profile.delete(instance_profile)
    books.delete()
    return redirect('create profile')


