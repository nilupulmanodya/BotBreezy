from django.db import models

# Create your models here.
class CareerInfo(models.Model):
    course_label = models.CharField(max_length=50, blank=True, null=True)
    course_des = models.CharField(max_length=10000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'career_info'

    def __str__(self):
        return self.course_label


class CourseInfo(models.Model):
    course_name = models.CharField(max_length=50, blank=True, null=True)
    info = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'course_info'
    
    def __str__(self):
        return self.course_name



class EntryInfo(models.Model):
    course_label = models.CharField(max_length=50, blank=True, null=True)
    course_des = models.CharField(max_length=10000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'entry_info'

    def __str__(self):
        return self.course_label

class EventInfo(models.Model):
    event_label = models.CharField(max_length=50, blank=True, null=True)
    event_des = models.CharField(max_length=10000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'event_info'
    def __str__(self):
        return self.event_label

class EventRegistrations(models.Model):
    event_name = models.CharField(max_length=500)
    student_reg_no = models.CharField(max_length=10)
    is_sent_email = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'event_registrations'

    def __str__(self):
        return self.student_reg_no


class FacultyInfo(models.Model):
    fac_lbl_name = models.CharField(max_length=500, blank=True, null=True)
    fac_info = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'faculty_info'
    def __str__(self):
        return self.fac_lbl_name


class HostelInfo(models.Model):
    hos_info_name = models.CharField(max_length=50, blank=True, null=True)
    hos_des = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hostel_info'
    def __str__(self):
        return self.hos_info_name


class SportsInfo(models.Model):
    sport_name = models.CharField(max_length=50, blank=True, null=True)
    sport_des = models.CharField(max_length=6000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sports_info'

    def __str__(self):
        return self.sport_name


class StaffInfo(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    info = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'staff_info'
    def __str__(self):
        return self.name

class Students(models.Model):
    reg_no = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'students'
    def __str__(self):
        return self.reg_no

class TestTable(models.Model):
    column1_int = models.IntegerField(blank=True, null=True)
    column_2 = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test_table'
    def __str__(self):
        return self.column1_int


class UniInfoDes(models.Model):
    des_name = models.CharField(max_length=50, blank=True, null=True)
    des = models.CharField(max_length=900, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'uni_info_des'
    def __str__(self):
        return self.des_name