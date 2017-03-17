#coding:utf8
from django.shortcuts import render,render_to_response
# from django.http import HttpResponse,HttpResponseRedirect
# import common.file_processing as cfp
# import common.read_office as o
# import common.time_correlation as tt
# from datastore.mongo_init import *
# from models import *
from django.db import connection
# import common.randomTools as rt
# import tools.morrisjs as m
from django.contrib import auth
# from datastore.sd import sll
import requests,sys,os,time,re
from PIL import Image
from selenium import webdriver
from bs4 import BeautifulSoup
# Create your views here.
def index(request):
    # m = request.GET.get('msg')
    return render(request, 'index.html')
def ugv(request):
    return render(request, 'ugv.html')
def uav(request):
    return render(request, 'uav.html')
def ucav(request):
    return render(request, 'ucav.html')
def usv(request):
    return render(request, 'usv.html')
def uuv(request):
    return render(request, 'uuv.html')
def rov(request):
    return render(request, 'rov.html')
def auv(request):
    return render(request, 'auv.html')
def us(request):
    return render(request, 'us.html')
def search(request):
    k = request.GET['s']
    context = {}
    filepath = sys.path[0] + '/static/images/' + k
    if os.path.isfile(filepath + '.jpg'):
        context['key'] = k
        return render(request, 'result.html', context)
    else:
        url = 'https://en.wikipedia.org/wiki/%s'%(k)
        # print url
        r = requests.get(url)
        r.encoding = 'utf-8'
        doc = r.text
        print doc[:100]
        if doc.find('Wikipedia does not have an article with this exact name') > 0:
            return render(request, 'notfound.html')
        else:
            # screenshot4page(url,filepath)
            # take_screenshot(url,filepath + '.png')
            h = savepage(url)
            context['key'] = k
            context['html'] = h
            return render(request, 'result.html', context)
def screenshot4page(url,filepath):
    driver = webdriver.PhantomJS()
    print url
    driver.get(url)
    driver.maximize_window()
    #
    driver.save_screenshot(filepath + '.png')
    im = Image.open(filepath + '.png')
    im.save(filepath + '.jpg')
    os.remove(filepath + '.png')
def take_screenshot(url, save_fn="capture.png"):
    browser = webdriver.Firefox() # Get local session of firefox
    browser.maximize_window()
    browser.get(url) # Load page
    browser.execute_script("""
        (function () {
            var y = 0;
            var step = 100;
            window.scroll(0, 0);

            function f() {
                if (y < document.body.scrollHeight) {
                    y += step;
                    window.scroll(0, y);
                    setTimeout(f, 100);
                } else {
                    window.scroll(0, 0);
                    document.title += "scroll-done";
                }
            }

            setTimeout(f, 1000);
        })();
    """)

    for i in xrange(30):
        if "scroll-done" in browser.title:
            break
        time.sleep(10)

    browser.save_screenshot(save_fn)
    browser.close()
def savepage(url):
    r = requests.get(url)
    r.encoding = 'utf-8'
    doc = r.text
    pagesoup = BeautifulSoup(doc)
    content = pagesoup.find(id='content')
    for x in content.findAll("span", {"class": "mw-editsection"}):
        x.extract()
    content.find(id='siteSub').extract()
    content.find(id='jump-to-nav').extract()
    p = content.prettify()
    return p