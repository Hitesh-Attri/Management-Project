from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Add_Book,  student ,Issue


# Register your models here.
# admin.site.register(Add_Book)
admin.site.register(student)
admin.site.register(Issue)


# @admin.register(student)
# class Student_admin(admin.ModelAdmin):
#     list_display = ['id','branch_name','roll_no']
#
# @admin.register(Issue)
# class Issue_book_admin(admin.ModelAdmin):
#     list_display = ['id','student_detail','book_detail', 'issue_date' ,'submit_date','fine']

@admin.register(Add_Book)
class Add_book_admin(admin.ModelAdmin):
    list_display = ['id', 'book_name', 'author_name', 'edition', 'price','quantity']
