from django.shortcuts import render,HttpResponse,redirect

from django.contrib.auth import authenticate,login,logout
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms
import cv2
from Evaluator.models import ForwardedData
from Customer.models import Contact
from MyAdmin.models import User
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect

from django.contrib.auth.decorators import login_required

def AdminDashboard(request):
    if request.user.is_anonymous:
        return redirect('/admin')
    return render(request,'adminDashboard.html')

def AdminLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
    
        if user is not None and user.is_superuser:
            login(request, user)
            # Redirect to admin dashboard 
            return render(request,'adminDashboard.html')
        else:
           messages.error(request, 'Invalid Credentials!!')
           messages.error(request, 'Please check your username or password')
           return render(request, 'adminLogin.html', {'error_message': 'Invalid credentials'})
    else:
        return render(request, 'adminLogin.html')

def feedback(request):
    return render(request, 'feedback.html')
@login_required
def CreateNewEvaluator(request):
    if request.method == 'POST':
        # Retrieve the data from the form
        username = request.POST.get('username')
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username is already in use. Please choose another username.')
            return redirect('CreateNewEvaluator')  
        
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        job_position = request.POST.get('job_position')

        # Create a new User instance
        user = User.objects.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password
        )

        # Save additional details in the default User model
        user.job_position = job_position
        user.save()

       
        messages.success(request, 'Registration Successful!')
        return redirect('RegistrationSuccessful') 

    return render(request, 'RegistrationSuccessfull.html')


def RegistrationSuccessful(request):
    return render(request, 'RegistrationSuccessfull.html')


def delete_request(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id)
    if request.method == 'POST':
        contact.delete()
        return redirect('AdminDashboard') 
    return render(request, 'deleteRequest.html', {'contact': contact})


def delete_user(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    if request.method == 'POST':
        user.delete()
        messages.success(request, 'User has been deleted successfully.')
        return redirect('manageEvaluator') 
   
    return render(request, 'deleteEvaluator.html', {'user': user})


def Forward_data(request, contact_id):
    data = Contact.objects.get(id=contact_id)

    forward_data = ForwardedData(
        name=data.name,
        website_name=data.webName,
        website_url=data.url
    )
    forward_data.save()

    
    return redirect(request,'forwardSuccessfull.html')


def forward_request(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id)
    evaluators = User.objects.all()  # list all users as evaluators

    if request.method == 'POST':
        evaluator_username = request.POST.get('evaluator')
        due_date = request.POST.get('due_date')
        desc=request.POST.get('desc')

        evaluator = get_object_or_404(User, username=evaluator_username)
        forwarded_data = ForwardedData.objects.create(
            username=evaluator.username,
            website_name=contact.webName,
            website_url=contact.url,
            description=desc,
            due_date=due_date,
            assigned_evaluator=evaluator
        )
        return redirect('forwardSuccess') 
    return render(request, 'forwardReq.html', {'contact': contact, 'evaluators': evaluators})


def forwardSuccess(request):
    return render(request, 'forwardSuccessfull.html')


def editUser(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    predefined_job_positions = ['UX/UI Expert', 'UI/UX Designer', 'Internee', 'Other']

    if request.method == 'POST':
        new_username = request.POST.get('username')

        # Check if the new username is unique among users except the one being edited
        if User.objects.filter(username=new_username).exclude(id=user_id).exists():
            # Handle the case where the new username is not unique
            messages.error(request, 'Username is not unique. Please choose a different username.')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

        # Continue with the update if the username is unique
        user.username = new_username
        
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.email = request.POST.get('email')
        user.job_position=request.POST.get('job_position')
        user.password=request.POST.get('password')
        user.save()
        messages.success(request, 'User updated successfully.')

        # Redirect back to the referring page (the page where the form was submitted)
        return redirect('manageEvaluator') 

    # If it's a GET request, render the form with the user's data
    return render(request, 'editUser.html', {'user': user, 'job_positions': predefined_job_positions})


def AssignTask(request):
    evaluators=ForwardedData.objects.all()
    return render(request,'assignTask.html',{'evaluators': evaluators})

def delete_forwarded_data(request, data_id):
    forwarded_data = get_object_or_404(ForwardedData, pk=data_id)
    if request.method == 'POST':
        forwarded_data.delete()
        messages.success(request, 'Project has been deleted successfully.')
        return redirect('assignTask.html') 
   
    return render(request, 'deleteProject.html')

def ViewRequest(request):
    contacts = Contact.objects.all()
    return render(request, 'viewRequest.html', {'contacts': contacts})

def ViewRequestDetails(request,contact_id):
    contact = Contact.objects.get(id=contact_id)
    return render(request, 'viewContactDetails.html', {'contact': contact})

def ManageEvaluator(request):
    users = User.objects.filter(is_superuser=False)
    return render(request, 'manageEvaluator.html', {'users': users})
    
def Adminlogout(request):
    logout(request)
    return render(request,'adminLogin.html')

