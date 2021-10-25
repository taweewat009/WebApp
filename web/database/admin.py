from django.contrib import admin
from .models import Guestbook, Post

# Register your models here.
class DesginPostAdmin(admin.ModelAdmin):
    list_display=["name","author","category"]
    list_per_page=3
    list_filter=["category","author"]
    search_fields=["name","category"]

admin.site.register(Guestbook)
admin.site.register(Post, DesginPostAdmin)