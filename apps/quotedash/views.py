from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt
from .models import User,UserManager,Quotes,QuoteManager
from django.db.models import Count

def index(request):
    return render(request, 'quotedash/index.html')

def login(request):
    if User.objects.filter(email = request.POST['email']):
        user = User.objects.get(email=request.POST['email'])
        if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
            user = User.objects.get(email=request.POST['email'])
            request.session['userid'] = user.id
            request.session['first_name'] = user.first_name
            request.session['email'] = user.email
            # messages.error(request, "Successfully registered (or logged in)!")
            return redirect('/dashboard')
        else:
            messages.error(request, "Invalid Email or Password")
            return redirect('/')
    else:
        messages.error(request, "Invalid Email or Password")
        return redirect('/')

def register(request):
    # request.session['first_name'] = request.POST['first_name']
    # request.session['last_name'] = request.POST['last_name']
    # request.session['email'] = request.POST['email']

    errors = User.objects.validator(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')


    hashed = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
    User.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'], password = hashed)
    user = User.objects.get(email=request.POST['email'])
    request.session['userid'] = user.id
    request.session['first_name'] = user.first_name
    request.session['email'] = user.email
    print(request.session['first_name'])
    return redirect('/dashboard')


def dashboard(request):
    if 'userid' not in request.session:
        return redirect('/')
    user = User.objects.get(id=request.session['userid'])
    allQuotes = Quotes.objects.all()
    quotesLiked = Quotes.objects.exclude(liked_by=user)

  




    context = {
        'quotesLiked':quotesLiked,
        'user':user,
        'allQuotes':allQuotes,
    }
    return render(request, 'quotedash/dashboard.html',context)



def logout(request):
    request.session.clear()
    return redirect('/') 

def addquote(request):
    errors = Quotes.objects.quoteValidator(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/dashboard')
    user= User.objects.get(id=request.POST['userid'])
    Quotes.objects.create(author=request.POST['author'],quote=request.POST['quote'],posted_by=user,likecount=1)
    quote = Quotes.objects.last()
    quote.liked_by.add(user)


    return redirect('/dashboard')

def viewpostedby(request,id):
    if 'userid' not in request.session:
        return redirect('/')
    user = User.objects.get(id=id)
    usersquotes = Quotes.objects.filter(posted_by = user)
    context = {
        'usersquotes' : usersquotes,
        'user':user,
    }

    return render(request, 'quotedash/userquotes.html',context)  

def editmyaccountpage(request,id):
    if 'userid' not in request.session:
        return redirect('/')
    sessionEmail = request.session['email']
    usercheck = User.objects.get(id=id)
    usercheckEmail = usercheck.email
    if usercheckEmail != sessionEmail:
        return redirect('/')
    

    user = User.objects.get(id=id)
    context = {
        'user':user,
    }
    
    return render(request, 'quotedash/editaccount.html',context) 


def editaccount(request):
    if 'userid' not in request.session:
        return redirect('/')
    


    id = request.POST['userid']
    errors = User.objects.editvalidator(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/editmyaccountpage/'+str(id))
    user = User.objects.get(id=id)
    user.first_name = request.POST['first_name']
    user.last_name = request.POST['last_name']
    user.email = request.POST['email']
    user.save()
    request.session['email'] = user.email
    messages.error(request, "Change completed!")
    return redirect('/editmyaccountpage/'+str(id))

def like(request):
    request.POST['quoteid']
    user= User.objects.get(id=request.POST['userid'])
    quote = Quotes.objects.get(id=request.POST['quoteid'])
    quote.liked_by.add(user)
    quote.likecount +=1
    quote.save()

    return redirect('/dashboard')

def deletequote(request,id):
    quote = Quotes.objects.get(id=id).delete()

    return redirect('/dashboard')





