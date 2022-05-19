from django.db import models

# Create your models here.
from django.db.models import Sum


class Course(models.Model):
    cid=models.IntegerField(primary_key=True)
    mycourse=[('java','java'),('python','python'),('PHP','PHP')]
    course=models.CharField(choices=mycourse,max_length=30)
    myduration = [('2 months', '2 months'), ('3 months', '3 months'), ('6 months', '6 months')]
    duration=models.CharField(choices=myduration,max_length=30)

    def __str__(self):
        return f'{self.cid}-{self.course}-{self.duration}'

class Staff(models.Model):
    stid=models.IntegerField(primary_key=True)
    stname=models.CharField(max_length=30)
    cid = models.ForeignKey(Course,default=111,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.stid}-{self.stname}{self.cid}'


class Student(models.Model):
    stuid=models.IntegerField(primary_key=True)
    stuname=models.CharField(max_length=30)
    cid=models.ForeignKey(Course,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.stuid}-{self.stuname}{self.cid}'

class Attendance(models.Model):
    stuid=models.ForeignKey(Student,on_delete=models.CASCADE)
    stid=models.ForeignKey(Staff,on_delete=models.CASCADE)
    date=models.DateField()
    myduration = [('2 hours', '2 hours'), ('3 hours', '3 hours'), ('6 hours', '6 hours')]
    duration = models.CharField(choices=myduration, max_length=30)

class Evaluation(models.Model):
    stuid = models.ForeignKey(Student, on_delete=models.CASCADE)
    stid = models.ForeignKey(Staff, on_delete=models.CASCADE)
    # totalduration=Attendance.objects.filter(stuid=stuid).aggregate(Sum(F'duration'))
    examdate=models.DateField()

