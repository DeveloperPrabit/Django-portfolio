from django.shortcuts import render
from .models import ContactInfo, Section, Document
from collections import defaultdict

def index(request):
    sections = Section.objects.all()
    documents = Document.objects.all()
    contact_info_list = ContactInfo.objects.all()  

    grouped_sections = defaultdict(list)
    for sec in sections:
        grouped_sections[sec.section_type].append(sec)

    return render(request, 'portfolio/index.html', {
        'grouped_sections': grouped_sections,
        'documents': documents,
        'contact_info_list': contact_info_list,  
    })
