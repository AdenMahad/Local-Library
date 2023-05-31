from django.shortcuts import render,redirect
from .models import Book,Author,BookInstance,Genre
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,authenticate
from django.utils.decorators import method_decorator



# Create your views here.
@login_required
def index(request):
    
    #generate count for some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    #Available books (status= 'a')
    num_instances_available = BookInstance.objects.filter(status__exact = 'a').count()

    #The 'all()' is implied by default.
    num_authors = Author.objects.count()
    # create the context of all the variables you gathered
    num_visits = request.session.get('num_visits',0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_books': num_books,
        'num_instances':num_instances,
        'num_instance_availablity':num_instances_available,
        'num_authors':num_authors,
        'num_visits': num_visits
    }
    # Render the HTML template index.html with all the variables in the context dictionary
    return render(request,"catalog/index.html", context=context)
    

@method_decorator(login_required,name='dispatch')
class BookListView(generic.ListView):
    model = Book  # the model you are working on
    paginate_by = 10 
    template_name = 'catalog/book_list.html' # template name 
    queryset = Book.objects.all()  # quering the database
    context_object_name = 'book_list'  # template variable name

@method_decorator(login_required,name='dispatch')
class BookDetailView(generic.DetailView):
    
    model = Book
    paginate_by = 10

@method_decorator(login_required,name='dispatch')
class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 10
    template_name = 'catalog/author_list.html'
    queryset = Author.objects.all()
    context_object_name = 'author_list'

@method_decorator(login_required,name='dispatch')
class AuthorDetailView(generic.DetailView):
    model = Author

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username = username, password = password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


    

