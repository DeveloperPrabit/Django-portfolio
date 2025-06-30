from django.shortcuts import render
from .models import Section, Document, ContactInfo
from collections import defaultdict

def index(request):
    # Group sections by their type
    grouped_sections = defaultdict(list)
    sections = Section.objects.all()
    for section in sections:
        grouped_sections[section.section_type].append(section)

    # Convert defaultdict to regular dict for template use
    grouped_sections_dict = dict(grouped_sections)

    # Get the first contact info entry (assuming single entry logic)
    contact_info = ContactInfo.objects.first()

    # Fetch all documents
    documents = Document.objects.all()

    # Render context to template
    return render(request, 'portfolio/index.html', {
        'grouped_sections': grouped_sections_dict,
        'contact_info': contact_info,
        'documents': documents,
    })
