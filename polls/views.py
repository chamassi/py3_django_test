from django.shortcuts import render
from django.http import HttpResponse
import time
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
#from wiki.models import Article, ArticleRevision, URLPath   

from matplotlib.backends.backend_agg import FigureCanvasAgg

import matplotlib.pyplot
import matplotlib.pyplot as plt, mpld3
import numpy as np
import math as maths

from pylab import figure, axes, pie, title
from matplotlib.backends.backend_agg import FigureCanvasAgg


from django.template.response import TemplateResponse


# Create your views here.
def home(request):
    return render(request,'home.html')

def index(request):
    return render(request,'index.html')

        # -*- coding: utf-8 -*-

def my_render_callback(response):
    # Do content-sensitive processing

    do_post_processing()

def factorielleHTML(request):
    data =[int(request.GET.get('factoriel_data1')),int(request.GET.get('factoriel_data2')),
    int(request.GET.get('factoriel_data3')),int(request.GET.get('factoriel_data4')),
    int(request.GET.get('factoriel_data5')),int(request.GET.get('factoriel_data6')),
    int(request.GET.get('factoriel_data7')),int(request.GET.get('factoriel_data8')),
    int(request.GET.get('factoriel_data9')),int(request.GET.get('factoriel_data10'))]
    factoriels=[]

    debut=time.time()
    for data_in in data:
        factoResult=calculFactoriel(data_in)
        factoriels.append(factoResult)

    fin=time.time()
    duree=float(fin-debut)*1000

   #GRAPHIQUE DE DONNEES
    f = plt.figure()
    x = data

    
    logdata=[]
    for d in x :
        logdata.append(np.log10(d))

    #h = [0,1,2,3,5,6,4,2,1,0]
    plt.title('Fonctions  ')#tittre du graphique
    plt.xlim(0, calculMaximum(x))
    plt.ylim(0, calculMaximum(x))

    plt.xlabel('Taille des données ')
    plt.ylabel('Temps de calcul des algorithmes')
    plt.plot(x,factoriels,'r--', label="Factorielle") 
    plt.legend()    


    responsedata = mpld3.fig_to_html(f)


    # Create a response
    response = TemplateResponse(request,"factorielle.html",
    {'factoriel_data':data ,'responsedata':responsedata,'factorielle':factoriels,'duree':duree})
    
    # Register the callback
    #response.add_post_render_callback(response.write(responsedata))


    return response


def divEuclideHTML(request):
    return render(request,"divisionEuclide.html")


def maximumHTML(request):
    #calculMaximum([125,659,22,9,125,98,-569])
    maxdata=[float(request.GET.get('datamax_12')),float(request.GET.get('datamax_13')),float(request.GET.get('datamax_14')),float(request.GET.get('datamax_15')),
    float(request.GET.get('datamax_21')),float(request.GET.get('datamax_22')),float(request.GET.get('datamax_23')),float(request.GET.get('datamax_24')),
    float(request.GET.get('datamax_25')),float(request.GET.get('datamax_11'))]

    maxresult=calculMaximum(maxdata)

    print("max result ",maxresult)
    return render(request,'maximum.html',{'maxdata':maxdata,'maximum':maxresult})


def calculFactoriel(n):
    result=1
    for i in range(1,n+1):
        result=i*result
    return result

def calculMaximum(listedata):
    m=listedata[0]
    print ("Calcul Max - data ",listedata)
    for d in listedata:
        if d>m: m=d

    return m



def div_euclidienne(a,b):
    reste=a
    quotient=0



def testmatplotlib(request):
   f = plt.figure()
   x = np.arange(100)
   racinedata=[]
   expdata=[] 
   logdata=[]
   for d in x :
       expdata.append(np.exp(d-1)) 
       racinedata.append(np.sqrt(d-1))
       #expdata.append(np.exp(2*d/2))

       logdata.append(np.log10(d))

   #h = [0,1,2,3,5,6,4,2,1,0]
   plt.title('Fonctions  ')#tittre du graphique
   plt.xlim(0, 80)
   plt.ylim(0, 800)
   plt.xlabel('Taille des données ')
   plt.ylabel('Temps de calcul des algorithmes')
   
   plt.plot(expdata, 'g^', label="Exponentielle")
   plt.plot(racinedata,'g--', label="Racine carré")#, ,
   plt.plot(x,x,'r--', label="Linéaire") 
   plt.plot(x,x**2,'bs', label="Carré") 
   plt.plot(x,logdata,'b_', label="Logarithme base 10")


   #bar1 = plt.bar(x,h,width=1.0,bottom=0,color='Green',alpha=0.65,label='Legend')
   plt.legend()
     
   responsedata = mpld3.fig_to_html(f)
    
   return HttpResponse(responsedata)

from django.http import HttpResponse
from django.shortcuts import render
from matplotlib import pylab
from pylab import *
import PIL, PIL.Image  
from io import StringIO, BytesIO
import numpy
import io 

def showimage(request):
    # Construct the graph
    t = arange(0.0, 2.0, 0.01)
    s = sin(2*pi*t)
    plot(t, s, linewidth=1.0)
 
    xlabel('time (s)')
    ylabel('voltage (mV)')
    title('About as simple as it gets, folks')
    grid(True)
 
    # Store image in a string buffer
    buffer = StringIO()
    canvas = pylab.get_current_fig_manager().canvas
    canvas.draw()
    pilImage = PIL.Image.frombytes("RGB", canvas.get_width_height(), canvas.tostring_rgb())
    #pilImage.save(buffer.tostring_rgb(), "PNG")
    pylab.close()
 
    # Send buffer in a http response the the browser with the mime type image/png set
    return HttpResponse(buffer, content_type="image/png")