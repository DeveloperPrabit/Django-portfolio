from django.contrib import admin
from .models import Section, Document, ContactInfo, HeroSection

admin.site.register(Section)
admin.site.register(Document)
admin.site.register(ContactInfo)

@admin.register(HeroSection)
class HeroSectionAdmin(admin.ModelAdmin):
    list_display = ('title',)

