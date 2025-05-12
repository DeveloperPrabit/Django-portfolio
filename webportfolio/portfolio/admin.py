from django.contrib import admin
from .models import Section, Document
from .models import ContactInfo

admin.site.register(Section)
admin.site.register(Document)
#admin.site.register(Contact)
admin.site.register(ContactInfo)

