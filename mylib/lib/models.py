
# Create your models here.
from django.db import models
from datetime import datetime


# Create your models here.
# class Abstract_1(models.Model):
#     book_name=models.CharField(max_length=40)
#     author_name=models.CharField(max_length=30)
#     edition=models.CharField(max_length=40, blank=True, null=True)
#
#     class Meta:
#         abstract=True

class Add_Book(models.Model):
    book_name = models.CharField(max_length=40)
    author_name = models.CharField(max_length=30)
    edition = models.CharField(max_length=40, blank=True, null=True)
    price = models.IntegerField()
    quantity = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.book_name) + '[' + str(self.id) + ']'


class student(models.Model):
    student_name = models.CharField(max_length=50)
    Branch_name = models.CharField(max_length=50)
    rollno = models.CharField(max_length=40)

    def __str__(self):
        return str(self.student_name) + '[' + str(self.id) + ']'


class Issue(models.Model):
    student_details = models.ForeignKey(student, on_delete=models.CASCADE)
    book_details = models.ForeignKey(Add_Book, on_delete=models.CASCADE)
    issue_date = models.DateTimeField(default=datetime.now, blank=True)
    submit_date = models.DateTimeField( blank=True)
    fine = models.IntegerField(default=0)
    is_submitted = models.BooleanField(default=False)

    #
    # def expiry_date(self):
    #     return datetime.today().date()+timedelta(days=15)
    #
    # def save(self,*args,**kwargs):
    #     self.submit_date = self.expiry_date()
    #     return super(student,self).save(*args, **kwargs)
