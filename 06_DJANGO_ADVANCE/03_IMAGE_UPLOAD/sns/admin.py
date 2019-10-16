from django.contrib import admin
from .models import Posting

# Register your models here.


class PostingModelAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at','updated_at')
    list_display = ('id','content','create_at','updated_at')
    list_display_links = ('id','content')

admin.site.register(Posting)


