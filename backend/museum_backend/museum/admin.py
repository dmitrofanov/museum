from django.contrib import admin
from .models import Person, PersonPhoto, Group

class PersonPhotoInline(admin.TabularInline):
    model = PersonPhoto
    extra = 1

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']
    search_fields = ['title', 'description']

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['rank', 'last_name', 'first_name', 'middle_name', 'birth_year']
    list_filter = ['gender', 'groups']
    search_fields = ['last_name', 'first_name']
    filter_horizontal = ['groups']
    inlines = [PersonPhotoInline]

@admin.register(PersonPhoto)
class PersonPhotoAdmin(admin.ModelAdmin):
    list_display = ['person', 'caption', 'is_main']
    list_filter = ['is_main']