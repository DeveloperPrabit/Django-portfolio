from django.shortcuts import render, redirect
from .models import Section, Document, ContactInfo
#from .forms import ContactForm

def index(request):
    sections = Section.objects.all()
    documents = Document.objects.all()
    contact_info = ContactInfo.objects.first()  # Expecting only one record
    return render(request, 'portfolio/index.html', {
        'sections': sections,
        'documents': documents,
        'contact_info': contact_info,
    })

#def submit_contact(request):
#    if request.method == 'POST':
#        form = ContactForm(request.POST)
#        if form.is_valid():
#            form.save()
#    return redirect('index')
