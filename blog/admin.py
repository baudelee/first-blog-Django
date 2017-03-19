from django.contrib import admin

# Register your models here.
# -*v*- Add admin settings by Baude

from .models import Post

admin.site.register(Post)
