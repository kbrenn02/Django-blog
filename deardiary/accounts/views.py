from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

# Create your views here.

# this method is called as a get request (you go to the link and get the signup page)
# and as a post request (because in the signup.html, the form element points to /accounts/signup)
# so we need to handle it differently if the method is called as a GET or POST
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST) #.POST is used to capture data sent via the post request (of submitting the form)
        if form.is_valid():
            user = form.save() #save the data to the database if the form is valid
            #still need to log the user in after they are successfully created
            login(request, user)
            return redirect('articles:list') #this redirects to the list of articles. 
            # the syntax is articles:list because list is the name of the url in the articles app
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form}) #the third variable is data we're sending to the view/template

def login_view(request): #login also has post(fill out form) or get requests(go to url)
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            #log in the user
            user = form.get_user()
            login(request, user)
            # check if the next field is in the request. If it is, redirect to that page
            # so if the user is coming from the create page, next=/articles/create and it will send them back there
            # if the user is coming straight to the login page, there is no next variable so it sends them to the article list
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('articles:list')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('articles:list')