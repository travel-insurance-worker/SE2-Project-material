import os
import time
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views import View
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.db import connection
import pyodbc
class Sign_out(View):
    def post(self, request, *args, **kwargs):
        emailAddress = request.POST.get('emailAddress', None)
        print(emailAddress)
        conn = pyodbc.connect('Driver={SQL Server Native Client 11.0};'
                              'Server=DESKTOP-V4CEGG4;'
                              'Database=Futuristic_Travel;'
                              'Trusted_Connection=yes;')

        cursor = conn.cursor()
        query = 'UPDATE [Futuristic_Travel].[DBO].Customer SET status = \'Inactive\' WHERE EmailAddress = ?'
        data = (str(emailAddress))
        res = cursor.execute(query, data)
        conn.commit()
        cursor.close()
        return redirect('..')
class Redirect_to_login(View):
    def post(self, request, *args, **kwargs):
        context = {}
        emailAddress = request.POST.get('emailAddress', None)
        old_pass = request.POST.get('old_pass', None)
        new_pass = request.POST.get('new_pass', None)
        with connection.cursor() as cursor:
            cursor.execute("select * from [Futuristic_Travel].[dbo].Customer where EmailAddress = '%s'" % emailAddress)
            row = cursor.fetchall()
            cursor.close()

        ID = list()
        FirstName = list()
        LastName = list()
        NationalCode = list()
        BirthDate = list()
        EmailAddress = list()
        MembershipDay = list()
        status = list()
        BankCardNumber = list()
        Shaba = list()
        Password = list()
        for i in row:
            ID.append(i[0])
            FirstName.append(i[1])
            LastName.append(i[2])
            NationalCode.append(i[3])
            BirthDate.append(i[4])
            EmailAddress.append(i[5])
            MembershipDay.append(i[6])
            status.append(i[7])
            BankCardNumber.append(i[8])
            Shaba.append(i[9])
            Password.append(i[10])
        print(emailAddress)

        if not EmailAddress or Password[0] != old_pass:
            return redirect('../ChangePassword')

        else:
            conn = pyodbc.connect('Driver={SQL Server Native Client 11.0};'
                                  'Server=DESKTOP-V4CEGG4;'
                                  'Database=Futuristic_Travel;'
                                  'Trusted_Connection=yes;')

            cursor = conn.cursor()
            query = 'UPDATE [Futuristic_Travel].[DBO].Customer SET Password = ?, status = \'Inactive\' WHERE EmailAddress = ?'
            data = (str(new_pass), str(EmailAddress[0]))
            res = cursor.execute(query, data)
            conn.commit()
            cursor.close()
            print(query)
            print(new_pass)
            print(Password)
            return redirect('../login')

class Change_pass_page(View):
    def post(self, request, *args, **kwargs):
        return render(request, 'ChangePassword.html')
    def get(self, request, *args, **kwargs):
        return render(request, 'ChangePassword.html')

class Redirect_to_home(View):
    def post(self, request, *args, **kwargs):
        context = {}
        username = request.POST.get('username', None)
        pass_entered = request.POST.get('pass', None)
        with connection.cursor() as cursor:
            cursor.execute("select * from [Futuristic_Travel].[dbo].Customer where EmailAddress = '%s'" % username)
            row = cursor.fetchall()
            cursor.close()

        firstName = list()
        status = list()
        password = list()
        emailAddress = list()
        for i in row:
            firstName.append(i[1])
            status.append(i[7])
            password.append(i[10])
            emailAddress.append(i[5])

        context = {
            "firstName": firstName,
            "status": status,
            "password": password,
            "emailAddress": emailAddress,
        }
        pass_context = {}
        print(emailAddress)
        if not emailAddress or password[0] != pass_entered:
            pass_context['is_pass_true'] = False
            pass_context['not_yet_entered'] = False
            return render(request, 'login.html', pass_context)

        if emailAddress:
            conn = pyodbc.connect('Driver={SQL Server Native Client 11.0};'
                                  'Server=DESKTOP-V4CEGG4;'
                                  'Database=Futuristic_Travel;'
                                  'Trusted_Connection=yes;')

            cursor = conn.cursor()
            query = 'UPDATE [Futuristic_Travel].[DBO].Customer SET status = \'Active\' WHERE EmailAddress = ?'
            data = (str(emailAddress[0]))
            res = cursor.execute(query, data)
            conn.commit()
            cursor.close()
            return render(request, 'firstPage.html', context)
        else:
            return redirect('../login')


class Show_firstPage(View):
    template_name = 'firstPage.html'

    def get(self, request, *args, **kwargs):
        return render(request, 'firstPage.html')


class Forget_page(View):
    template_name= 'forgot.html'
    def get(self, request, *args, **kwargs):
        return render(request, 'forgot.html')

class Login_page(View):
    template_name = 'login.html'

    def get(self, request, *args, **kwargs):
        context = {}
        context['not_yet_entered'] = True
        return render(request, 'login.html', context)

    def signin(request):
        if request.method == 'GET':
            get_username = request.GET['username']
            get_password = request.GET['pass']

            with connection.cursor() as cursor:
                cursor.execute("select * from [Futuristic_Travel].[dbo].Customer where Username= %s ",[get_username])
                row = cursor.fetchall()
                cursor.close()

            print("success")

            return HttpResponse(200)

class tempPage(View):
    template_name = 'tempPage.html'

    def get(self, request, *args, **kwargs):
        return render(request, 'tempPage.html')


class Main_page(View):
    template_name = 'Futuristic-Travel.html'

    def get(self, request, *args, **kwargs):
        with connection.cursor() as cursor:
            cursor.execute("select * from [Futuristic_Travel].[dbo].Travel")
            row = cursor.fetchall()
            cursor.close()

        idList = list()
        customerIDList = list()
        initialPointList = list()
        destinationList = list()
        flightNumberList = list()
        seatNumberStartList = list()
        seatNumberEndList = list()
        priceList = list()
        purchaseDateList = list()
        flightDateList = list()
        flightTimeList = list()
        numberofTicketList = list()
        statusList = list()
        print(row)
        for i in row:
            idList.append(i[0])
            customerIDList.append(i[1])
            initialPointList.append(i[2])
            destinationList.append(i[3])
            flightNumberList.append(i[4])
            seatNumberStartList.append(i[5])
            seatNumberEndList.append(i[6])
            priceList.append(i[7])
            purchaseDateList.append(i[8])
            flightDateList.append(i[9])
            flightTimeList.append(i[10])
            numberofTicketList.append(i[11])
            statusList.append(i[12])
        Dict ={
            "ID": idList,
            "CustomerID": customerIDList,
            "InitialPoint": initialPointList,
            "Destination": destinationList,
            "FlightNumber": flightNumberList,
            "SeatNumberStart": seatNumberStartList,
            "SeatNumberEnd": seatNumberEndList,
            "Price": priceList,
            "PurchaseDate": purchaseDateList,
            "FlightDate": flightDateList,
            "FlightTime": flightTimeList,
            "NumberofTicket": numberofTicketList,
            "status": statusList
        }

        return render(request, self.template_name,Dict)

    def CancelFunc(request):
        if request.method == 'GET':
            bankCard = request.GET['bankNum']
            with connection.cursor() as cursor1:
                cursor1.execute("UPDATE [Futuristic_Travel].[dbo].Customer SET  [Futuristic_Travel].[dbo].Customer.BankCardNumber =  %s WHERE [Futuristic_Travel].[dbo].Customer.ID = '1911332431' ",[bankCard])
                cursor1.close()
            with connection.cursor() as cursor2:
                cursor2.execute("UPDATE [Futuristic_Travel].[dbo].Travel SET  [Futuristic_Travel].[dbo].Travel.status ='CANCLE' WHERE [Futuristic_Travel].[dbo].Travel.ID = '2012191' ")
                cursor2.close()
            print("trip is canceled")
            print(bankCard)

            return HttpResponse(200)
    def ChangeFunc(request):
        if request.method == 'GET':
            bankCard = request.GET['bankNum']
            with connection.cursor() as cursor1:
                cursor1.execute("UPDATE [Futuristic_Travel].[dbo].Customer SET  [Futuristic_Travel].[dbo].Customer.BankCardNumber =  %s WHERE [Futuristic_Travel].[dbo].Customer.ID = '1911332431' ",[bankCard])
                cursor1.close()
            with connection.cursor() as cursor2:
                cursor2.execute("UPDATE [Futuristic_Travel].[dbo].Travel SET  [Futuristic_Travel].[dbo].Travel.status ='CHANGE' WHERE [Futuristic_Travel].[dbo].Travel.ID = '2012191' ")
                cursor2.close()
            print("trip is changed")
            print(bankCard)

            return HttpResponse(200)