# api key: pk_535f59986b2d4d5a9c7682117dbb81bf
from django.shortcuts import render, redirect
import requests
import json
from .models import Stock
from django.contrib import messages
from .forms import StockForm

# Create your views here.


def home(request):
    if request.method == 'POST':
        ticker = request.POST['ticker']

        api_request = requests.get(
            f"https://cloud.iexapis.com/stable/stock/{ticker}/quote?token=pk_535f59986b2d4d5a9c7682117dbb81bf")

        try:
            api = json.loads(api_request.content)

        except Exception as e:
            api = 'Error....'
        return render(request, 'home.html', {'api': api})
    else:
        return render(request, 'home.html', {'ticker': 'Enter ticker symbol in Search Box'})


def about(request):
    return render(request, 'about.html', {})

# if tab indentation error occure then for VScode go to View->Command Pallet->Convert Indentation to Spaces


def add_stock(request):
    if request.method == 'POST':
        form = StockForm(request.POST or None)

        if form.is_valid():
            form.save()
            messages.success(request, ('Stock has been added'))
            return redirect('add_stock')

    else:
        ticker = Stock.objects.all()

        output = []  # If we not save the api data in list

        for ticker_item in ticker:

            api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + str(
                ticker_item) + "/quote?token=pk_535f59986b2d4d5a9c7682117dbb81bf")

            try:
                api = json.loads(api_request.content)
                output.append(api)

            except Exception as e:
                api = 'Error....'

        return render(request, 'add_stock.html', {'ticker': ticker, 'output': output})


def delete(request, stock_id):
    item = Stock.objects.get(pk=stock_id)
    item.delete()
    messages.success(request, ('Stock has been deleted'))
    return redirect('delete_stock')


def delete_stock(request):
    ticker = Stock.objects.all()
    return render(request, 'delete_stock.html', {'ticker': ticker})
