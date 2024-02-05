from django.shortcuts import render,HttpResponse,redirect
from datetime import date
from Customer.models import Contact

from django import forms
# Create your views here.

def Home(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def services(request):
    return render(request,"services.html")

def show_form(request):
    return render(request, 'contact.html')

def ContactUs(request):
    if request.method == "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        url=request.POST.getlist('url')
        webName=request.POST.get('webName')
        desc=request.POST.get('desc')
        
        contact=Contact(name=name, url=url ,email=email , webName=webName , desc=desc)
        contact.save()
        return render(request,"successful_request.html")
    return render(request,"contact.html")

'''
from .forms import ContactForm

def ContactUs(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            webName = form.cleaned_data['webName']
            desc = form.cleaned_data['desc']
            urls = form.cleaned_data['urls']

            # Create a new Contact object
            contact = Contact(name=name, email=email, webName=webName, desc=desc)
            contact.save()

            # Create URL objects and associate them with the Contact
            for url in urls:
                new_url = URL(url=url)
                new_url.save()
                contact.urls.add(new_url)

            contact.save()  # Save the Contact with associated URLs

            return redirect('success')  # Redirect to a success page
    else:
        form = ContactForm()
        
    return render(request, 'contact.html', {'form': form})
 '''
def view_saved_data(request):
    # Retrieve all Customer_contact objects from the database
    request = Contact.objects.all()

    # Pass the data to the template
    context = {'Contact': Contact}
    
    return render(request, 'viewdata.html', context)
      