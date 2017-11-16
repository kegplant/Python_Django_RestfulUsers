from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from models import Users
# the index function is called when root is visited
def index(request):#minimum
    context={
        'users':Users.objects.all()
    }
    #return HttpResponse(response)
    return render(request,'restful_user/index.html',context)
def update(postData,id):
    print 'updating'
    user=Users.objects.get(id=id)
    user.first_name=postData['first_name']
    user.last_name=postData['last_name']
    user.email=postData['email']
    user.save()
    return
def show(request,id):
    if request.method=='POST':
        update(request.POST,id)
        return redirect('/users')#directly return update(request.id)?
    else:
        print 'get show'
        user=Users.objects.get(id=id)
        context={
            'user':user
        }
        return render(request,'restful_user/show.html',context)
def edit(request,id):
    #prepopulate field?
    print 'editting'
    user=Users.objects.get(id=id)
    context={
        'user':user
    }
    return render(request,'restful_user/edit.html',context)
def new(request):
    print 'new user page'
    return render(request,'restful_user/new.html')
def create(request):
    if request.method=='POST':
        fname=request.POST['first_name']
        lname=request.POST['last_name']
        email=request.POST['email']
        Users.objects.create(first_name=fname,last_name=lname,email=email)
    return redirect('/users')
def destroy(request,id):
    print "destroying"
    Users.objects.get(id=id).delete()
    return redirect('/users')