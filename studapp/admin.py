from django.contrib import admin
from .models import Course,Staff,Student

# Register your models here.
admin.site.register(Course)
admin.site.register(Staff)
admin.site.register(Student)


admin.site.site_header='Student Evaluation System'

