from django.shortcuts import render
from .models import Section, Document, ContactInfo, HeroSection
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

    # Get the hero section content (title and subtitle)
    hero_section = HeroSection.objects.first()

    # Fetch all documents
    documents = Document.objects.all()

    # Render context to template
    return render(request, 'portfolio/index.html', {
        'grouped_sections': grouped_sections_dict,
        'contact_info': contact_info,
        'documents': documents,
        'hero_section': hero_section,
    })


def section_detail(request, section_type):
    sections = Section.objects.filter(section_type=section_type)
    contact_info = ContactInfo.objects.first()
    return render(request, f'portfolio/sections/{section_type}.html', {
        'sections': sections,
        'section_type': section_type,
        'contact_info': contact_info
    })
