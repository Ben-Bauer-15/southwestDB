from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt
from html.parser import HTMLParser
import re



class MyParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag == 'button':
            for attr in attrs:
                if attr[0] == 'aria-label' and 'Wanna Get Away' in attr[1]:
                    print(attr[1])

    def handle_data(self, data):
        # print(data)
        pass
    

def index(request):
    return HttpResponse('Hello world!')


@csrf_exempt
def test(request):
    if request.method == "POST":    
        print(request.POST)
        return HttpResponse("Success")

    else:
        print("error")
        return HttpResponse("error")


@csrf_exempt
def parserTest(request):
    if request.method == 'POST':
        parser = MyParser()

        parser.feed(request.POST['data'])


        return HttpResponse("Success!")
