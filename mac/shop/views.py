from django.http import HttpResponse
from django.shortcuts import render
from . models import Product,Contact
from math import ceil
def index(request):
    product=Product.objects.all()
    allprods=[]
    catprods=Product.objects.values('category')
    cats={item['category'] for item in catprods}
    print(cats)
    for cat in cats:
        prod=Product.objects.filter(category=cat)
        print(prod)
        n = len(prod)

        nslides = n // 4 + ceil((n / 4) - (n // 4))
        if n>1:
            allprods.append([prod,range(1,nslides),nslides])
        else:
            pass

    # cats={}



    # params={'no_of_slides':nslides,"range":range(1,nslides),"product":product}
    params={'allprods':allprods}
    return render(request,"shop/index.html",params)
def about(request):
    return render(request,"shop/about.html")
def contact(request):
    if request.method =='POST':
        print(request)
        email=request.POST.get('email',"")
        message=request.POST.get('message',"")
        phone=request.POST.get('phone',"")
        # phone=request.Post.get('phone','')
        contact=Contact(email=email,message=message,phone=phone)
        contact.save()
    return render(request,"shop/contact.html")
def tracker(request):
    return render(request,'shop/tracker.html')
def search(request):
    return render(request,'shop/search.html')
def productview(request,id):
    product=Product.objects.filter(product_id=id);
    print("hello",product)

    return render(request,'shop/productview.html',{'product':product[0]})
def search(request):

    return render(request,'shop/search.html')

def checkout(request):
    return HttpResponse("we are on checkout page")
def cart(request):

    return render(request,'shop/cart.html')