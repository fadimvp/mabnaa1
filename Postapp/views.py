from django.shortcuts import render

# Create your views here
def home (request ):


    context = {

    }
    return render(request,'indexv2.html',context)

def about (request ):


    context = {

    }
    return render(request,'about.html',context)


def contactus(request):

    context={

    }
    return render(request,'contactus.html',context)

def contactusar(request):

    context={

    }
    return render(request,'mabna_ar/contactusar.html',context)


def invmabna(request):

    context={

    }
    return render(request,'invmabna.html',context)

def index_ar(request):

    context={

    }
    return render(request,'mabna_ar/indexar.html',context)

def post_mabna(request):

    context={

    }
    return render(request,'postmabna.html',context)

def post_mabnaar(request):

    context={

    }
    return render(request,'mabna_ar/postmabaar.html',context)
