
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views import View
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.db import connection

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
        return render(request, 'login.html')

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