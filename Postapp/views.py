from django.shortcuts import render
from  Postapp.models import Home

# Create your views here
def home (request ):


    context = {

    }
    return render(request,'mabna_en/index.html',context)

def about (request ):


    context = {

    }
    return render(request,'about.html',context)

def owl(request):
    context={

    }
    return render(request,'owl.html',context)
def contactus(request):

    context={

    }
    return render(request,'mabna_en/contactus.html',context)

def contactusar(request):

    context={

    }
    return render(request,'mabna_ar/contactusar.html',context)


def invmabna(request):

    context={

    }
    return render(request,'invmabna.html',context)

def index_ar(request):
    form = Home.objects.all()
 

    context = {
        'form':form,

    }
    return render(request,'mabna_ar/indexar.html',context)

def post_mabna(request):

    context={

    }
    return render(request,'mabna_en/postmabna.html',context)

def post_hotels(request):

    context={

    }
    return render(request,'hotels.html',context)

def post_asmer(request):

    context={

    }
    return render(request,'asmer.html',context)



def post_mabnaar(request):

    context={

    }
    return render(request,'mabna_ar/postmabaar.html',context)
def post_hotelsar(request):

    context={

    }
    return render(request,'mabna_ar/hotelsar.html',context)

def post_asmerar(request):

    context={

    }
    return render(request,'mabna_ar/asmerar.html',context)

def all_project(request):
    context={

    }
    return render(request,'mabna_en/allproject_en.html',context)