from django.contrib import admin
from .models import Course,Staff,Student,Attendance,Evaluation

# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    list_display = ['cid','course','duration']

class StaffAdmin(admin.ModelAdmin):
    list_display = ['stid','stname','cid']

class StudentAdmin(admin.ModelAdmin):
    list_display = ['cid','stuid','stuname']

class AttendanceAdmin(admin.ModelAdmin):
    list_display = ['stuid','stid','date','duration']

class EvaluationAdmin(admin.ModelAdmin):
    list_display = ['stuid','stid','examdate']

admin.site.register(Course,CourseAdmin)
admin.site.register(Staff,StaffAdmin)
admin.site.register(Student,StudentAdmin)
admin.site.register(Attendance,AttendanceAdmin)
admin.site.register(Evaluation,EvaluationAdmin)

admin.site.site_header='Student Evaluation System'

