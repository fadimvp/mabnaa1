from django.urls import path 


from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('postmabna',views.post_mabna,name='postmabna'),
    path('asmer',views.post_asmer,name='asmer'),
    path('hotels',views.post_hotels,name='hotels'),


    path('about',views.about,name='about'),
    path('invmabna',views.invmabna,name='invmabna'),
    path('indexar',views.index_ar,name='indexar'),
    path('contactus',views.contactus,name='contactus'),
    path('contactusar',views.contactusar,name='contactusar'),
    path('postmabnaar',views.post_mabnaar,name='postmabnaar'),
    path('asmerar',views.post_asmerar,name='asmerar'),
    path('hotelsar',views.post_hotelsar,name='hotelsar'),








]