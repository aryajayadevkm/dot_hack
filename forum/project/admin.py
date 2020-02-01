from django.contrib import admin
from project.models import Projects, ProjectQueue
# Register your models here.


class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'short_description', 'description', 'created_by', 'price', 'status', 'timestamp')
    search_fields = ['id', 'short_description']

    def created_by(self, model):
        return model.created_by.username


class ProjectQueueAdmin(admin.ModelAdmin):
    list_display = ('id', 'project', 'interested_devs', 'dev_price', 'acceptance', 'timestamp')
    search_fields = ['id', 'project', 'acceptance']

    def project(self, model):
        return model.project.name

    def interested_devs(self, model):
        return model.interested_devs.username


admin.site.register(Projects, ProjectsAdmin)
admin.site.register(ProjectQueue, ProjectQueueAdmin)