from django.shortcuts import render
from django.http import HttpResponse
from .form import regform
from .form1 import sms_form
from .models import *
import urllib.request
import urllib.parse
import json

apikey = 'JZDcZ3WbxmQ-XBdd4fIFGAPaVcEW1bgQ94nnRrH8xv'
sender = 'TXTLCL'
#def contact(request,name,age):
 #   data= "Many more happy returns of the day {} {}".format(name,age)
  #  return HttpResponse(data)


def sendSMS(apikey, numbers, sender, message):
    data = urllib.parse.urlencode({'apikey': apikey, 'numbers': numbers,
                                   'message': message, 'sender': sender})
    data = data.encode('utf-8')
    request = urllib.request.Request("https://api.textlocal.in/send?/")
    f = urllib.request.urlopen(request, data)
    fr = f.read()
    return fr
def contactview(request):
    form = sms_form(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            Name = form.cleaned_data['name']
            Number = form.cleaned_data['number']
            Number = f'91{str(Number)}'
            Message = form.cleaned_data['message']
            Message = f"FROM: {Name}\n{Message}"
            try:
                res = sendSMS(apikey,Number,sender,Message)
                res = json.loads(res)
                if res['status'] == 'success':
                    msg = "Message sent successfully...!"
                    return render(request, 'api.html', {'FORM': form,'MSG':msg})
                else:
                    msg = f"ERROR:  {res['errors'][0]['message']}"
                    return render(request, 'api.html', {'FORM': form,'MSG':msg})
            except Exception as Ex:
                msg = f"SERVER ERROR: {Ex} "
                return render(request,'api.html',{'FORM':form,'MSG':msg})
    msg  = "Could not send message something went wrong...!"
    return render(request,'api.html',{'FORM':form,'MSG':msg})





    #return render(request, 'api.html',{'FORM':form})

# Create your views here.
def contactview1(request):
    if request.method == 'POST':
        form=regform(request.POST)
        if form.is_valid():
            obj=pagecontact()
            obj.name=form.cleaned_data['name']
            obj.email=form.cleaned_data['email']
            obj.cat=form.cleaned_data['catagary']
            obj.sub=form.cleaned_data['sub']
            obj.body=form.cleaned_data['body']
            obj.save()
            #print(obj.name,obj.email)

            data="registration of candidate {} done successfully".format(obj.name)

            return HttpResponse(data)
        else:
            error1="something went wrong"
            form=regform()
            return render(request,'contact.html',{'myform':form,'ERROR':error1})
    # form = regform()
    # return render(request, 'contact.html', {'myform': form})


# def contactForm(request):
#     if request.method == 'POST':
#
#         form = pagecontactForm(request.POST)
#         if form.is_valid():
#             name=request.POST.get['name']
#             email=request.POST.get['email']
#             print("valid")
#
#

            # data="registration of candidate {} done successfully".format(rform.cleaned_data['name'])
            #
            # return HttpResponse(data)
            #
            #
    form = regform()
    return render(request, 'contact.html', {'myform': form})