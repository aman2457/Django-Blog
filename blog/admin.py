


# Register your models here.
from django.contrib import admin
from .models import Post, Comment

from django_summernote.admin import SummernoteModelAdmin


class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('text',)

admin.site.register(Post,PostAdmin)
admin.site.register(Comment)
