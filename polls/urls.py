from django.urls import path, re_path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('testmatplotlib', views.testmatplotlib, name='testmatplotlib'),
    path('factorielleHTML', views.factorielleHTML, name='factorielleHTML'),
    path('maximumHTML', views.maximumHTML, name='maximumHTML'),
    path('home', views.home, name='home'), 
    path('divEuclideHTML', views.divEuclideHTML, name='divEuclideHTML'), 
    
    #re_path(r'^_Matplotlib/Bar/$', include('visualization.views.GraphsViewBar')),
]
