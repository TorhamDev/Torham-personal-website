from django.contrib import admin
from home.models import IndexPage, ProjectPage, AboutPage

# Register your models here.
admin.site.register(IndexPage)
admin.site.register(ProjectPage)
admin.site.register(AboutPage)
