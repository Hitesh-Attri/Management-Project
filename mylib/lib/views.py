import datetime
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView
from datetime import timedelta
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
#

from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView


# Create your views here.
class Admin_book_Control_api(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None):
        id = pk
        if id is not None:
            stu = Add_Book.objects.filter(id=id)
        else:
            stu = Add_Book.objects.all()
        serializer = Add_book_serializer(stu, many=True)
        print(stu)
        print(serializer.data)
        return Response({'data': serializer.data})

    def post(self, request):

        serializer = Add_book_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'data created'})
        return Response(serializer.errors)

    def put(self, request, pk):
        id = pk
        stu = Add_Book.objects.get(pk=id)
        serializer = Add_book_serializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'data is updated'})
        return Response(serializer.errors)

    def patch(self, request, pk):
        id = pk
        stu = Add_Book.objects.get(pk=id)
        serializer = Add_book_serializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'data patched partially'})
        return Response(serializer.errors)

    def delete(self, request, pk):
        id = pk
        stu = Add_Book.objects.get(pk=id)
        stu.delete()
        return Response({'msg': ' data deleted'})


class Student_Record_Control_api(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None):
        id = pk
        if id is not None:
            stu = student.objects.filter(id=id)
        else:
            stu = student.objects.all()
        serializer = Student_serializer(stu, many=True)
        print(stu)
        print(serializer.data)
        return Response({'data': serializer.data})

    def post(self, request):

        serializer = Student_serializer(data=request.data)



        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'data created'})
        return Response(serializer.errors)

    def put(self, request, pk):
        id = pk
        stu = student.objects.get(pk=id)
        serializer = Student_serializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'data is updated'})
        return Response(serializer.errors)

    def patch(self, request, pk):
        id = pk
        stu = student.objects.get(pk=id)
        serializer = Student_serializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'data patched partially'})
        return Response(serializer.errors)

    def delete(self, request, pk):
        id = pk
        stu = student.objects.get(pk=id)
        stu.delete()
        return Response({'msg': ' data deleted'})


class IssueBook(APIView):
    def post(self, request):
        # it is used to request from frontend 'postman'
        stu_id = request.data['stu_id']
        book_id = request.data['book_id']

        stu_obj = student.objects.get(id=stu_id)
        book_obj = Add_Book.objects.get(id=book_id)

        issue_book_obj = Issue(
            student_details=stu_obj,
            book_details=book_obj,
            issue_date=datetime.datetime.now(),
            submit_date=datetime.datetime.now() + timedelta(days=7)
        )
        issue_book_obj.save()
        return Response({'msg': ' Book issued successfully.'})


class SubmitIssueBook(APIView):
    def post(self, request):
        issue_book_id = request.data['id']
        issue_book_obj = Issue.objects.get(id=issue_book_id)
        submit_date = issue_book_obj.submit_date.date()
        today_date = datetime.today().date()

        check_date = (today_date - submit_date)
        if check_date.days > 0:
            fine = 10 * check_date.days
            issue_book_obj.fine = fine

        issue_book_obj.is_submitted = True
        issue_book_obj.save()

        return Response({'msg': str(submit_date)})


class User_Login(APIView):
    def post(self, request):
        user_name = request.data['username']
        password_nmae = request.data['password']

        user_obj = User.objects.filter(username=user_name).first()
        if not user_obj:
            return Response({'msg': 'User not found.'})

        if user_obj.check_password(password_nmae):
            return Response({'msg': 'login successfully.'})
        return Response({'msg': 'login failed, password wrong.'})


class User_change_password(APIView):
    def post(self, request):
        user_name = request.data['username']
        current_password = request.data['currentpassword']
        new_password = request.data['newpassword']
        user_obj = User.objects.filter(username=user_name).first()
        if not user_obj:
            return Response({'msg': 'user not found'})
        if user_obj.check_password(current_password):
            user_obj.set_password(new_password)
            user_obj.save()
            return Response({'msg': 'password changed successfully'})


class Register_User(APIView):
    def post(self, request):
        try:
            first_name = request.data['first_name']
            last_name = request.data['last_name']
            email = request.data['email']
            password = request.data['password']
            username = first_name +" " + last_name
            user = User.objects.create_user(
                username=username,
                first_name=first_name,
                last_name=last_name,
                email=email,
                password=password,
            )
            print(user)
            user.save()
            return Response({'msg': username + 'created successfully'})
        except Exception as e:
            return Response({'msg': str(e)})



class testing(APIView):
    def post(self, request):
        try:
            print(request.data)
            print(request.data['data']);
            oldData = request.data['data']
            newData = 'this is new data testing done'
            # return Response({'oldData':oldData,'newData':newData})
            return Response({'oldData': oldData, 'newData':newData})
        except Exception as e:
            return Response({'msg': str(e)})


class User_update(APIView):
    def post(self, request):
        try:
            username = request.data['username']
            password_nmae = request.data['password']
            first_name = request.data['first_name']
            last_name = request.data['last_name']
            user = User.objects.get(username=username)
            if user.check_password(password_nmae):
                user.first_name = first_name
                user.last_name = last_name
                user.save()
                # else:
                return Response({'msg': 'user update successfully.'})
            return Response({'msg': 'password wrong.'})
        except Exception as e:
            return Response({'msg': str(e)})
