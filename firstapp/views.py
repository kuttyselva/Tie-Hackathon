from django.shortcuts import render
from django.http import HttpResponse
from django_tables2.tables import Table
import csv
import pandas as pd

# Create your views here.
def index(request):
    path='E:/udemy/first_project/firstapp/wea.csv'
    data = pd.read_csv(path)
    data_html = data.to_html()
    context = {'loaded_data': data_html}
    print(data)
    return render(request, "index.html", context)
    # df_table = Table(data.to_dict(orient='list'))
    # context = {'df_table': df_table}
    # print(context['df_table'])
    # return render(request, "index.html", context)

def help(request):
    return HttpResponse("hii")
