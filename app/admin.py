from django.contrib import admin
from .models import Tag,CodeModel


@admin.register(CodeModel)
class CodeModelAdmin(admin.ModelAdmin):
    pass









admin.site.register(Tag)
