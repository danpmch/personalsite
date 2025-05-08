from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from .models import Topic, Article

admin.site.register(Topic)
admin.site.register(Article, MarkdownxModelAdmin)
