from django.contrib import admin
from .models import Section, Document, ContactInfo, HeroSection

# Register existing models
admin.site.register(Section)
admin.site.register(Document)
admin.site.register(ContactInfo)

# Register HeroSection with custom display
@admin.register(HeroSection)
class HeroSectionAdmin(admin.ModelAdmin):
    list_display = ('title',)
