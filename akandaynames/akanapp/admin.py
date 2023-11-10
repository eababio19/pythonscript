from django.contrib import admin
from .models import AkanName

@admin.register(AkanName)
class AkanNameAdmin(admin.ModelAdmin):
    list_display = ('date_of_birth', 'gender', 'akan_name')

# You can customize the admin interface further by adding more configurations.
