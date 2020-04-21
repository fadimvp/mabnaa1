from django.urls import path 


from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('about',views.about,name='about'),
    path('invmabna',views.invmabna,name='invmabna'),
    path('indexar',views.index_ar,name='indexar'),
    path('contactus',views.contactus,name='contactus'),
    path('contactusar',views.contactusar,name='contactusar'),
    path('postmabna',views.post_mabna,name='postmabna'),
    path('postmabnaar',views.post_mabnaar,name='postmabnaar'),





]