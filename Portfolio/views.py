from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponseRedirect
from .forms import EnquiryForm
from .models import Enquiry

def contact_me(request):
    form = EnquiryForm(request.POST, request.FILES)
    if form.is_valid():
        first_name = form.data.get('first_name')
        last_name = form.data.get('last_name')
        email = form.data.get('email')
        company = form.data.get('company')
        enqury = Enquiry(first_name=first_name, last_name=last_name, email=email, company=company)
        enqury.save()
        return HttpResponseRedirect(reverse('portfolio'))
    return render(request, 'contact.html', {'form':form})

def portfolio(request):
    return render(request, 'portfolio.html')

