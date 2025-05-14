from django.shortcuts import render
from collections import defaultdict
from .models import Section, Document, ContactInfo

def index(request):
    sections = Section.objects.all()
    documents = Document.objects.all()
    contact_info = ContactInfo.objects.first()

    grouped_sections = defaultdict(list)
    for sec in sections:
        grouped_sections[sec.section_type].append(sec)

    return render(request, 'portfolio/index.html', {
        'grouped_sections': grouped_sections,
        'documents': documents,
        'contact_info': contact_info,
    })
