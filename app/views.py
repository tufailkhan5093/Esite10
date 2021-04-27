from django.shortcuts import render,redirect
from django.views import View
from django.views.generic import ListView
from .models import Product,Cart,OrderPlaced,Customer
from .forms import UserRegistrationform,CustomerProfileform
from django.contrib import messages
from django.db.models import Q
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# def home(request):
#  return render(request, 'app/home.html')

class ProductView(View):
    def get(self,request):
        topwear=Product.objects.filter(category='TW')
        bottomwear=Product.objects.filter(category='BW')
        mobiles=Product.objects.filter(category='M')
        laptops=Product.objects.filter(category='L')
        cart_quantity=0
        if request.user.is_authenticated:
            cart=Cart.objects.filter(user=request.user)
            
            if cart:
                for i in range(len(cart)):
                    cart_quantity=cart_quantity+1
                
            else:
                cart_quantity=0
        return render(request,'app/home.html',{'topwear':topwear,'bottomwear':bottomwear,'mobiles':mobiles,'quantity':cart_quantity,'laptops':laptops})

# def product_detail(request):
#  return render(request, 'app/productdetail.html')

class ProdcutDetail(View):
    def get(self,request,id):
        product=Product.objects.get(pk=id)
        item_in_cart=False
        if request.user.is_authenticated:
            item_in_cart=Cart.objects.filter(Q(product=product.id) & Q(user=request.user))
        
        if request.user.is_authenticated:
            cart=Cart.objects.filter(user=request.user)
            cart_quantity=0
            if cart:
                for i in range(len(cart)):
                    cart_quantity=cart_quantity+1
                
            else:
                cart_quantity=0
        return render(request,'app/productdetail.html',{'product':product,'item_in_cart':item_in_cart,'quantity':cart_quantity})

@login_required
def add_to_cart(request):
    user=request.user
    prod_id=request.GET.get('prod_id')
    product=Product.objects.get(pk=prod_id)
    Cart(user=user,product=product).save()
    return redirect('/cart')

@login_required
def show_cart(request):
    if request.user.is_authenticated:
        user=request.user
        
        amount=0.0
        shipping_amount=150.0
        total_amout=0.0
        cart=Cart.objects.filter(user=user)

        

        cart_product=[p for p in Cart.objects.all() if p.user==user]
        
      
        if cart_product:
            for p in cart_product:
                tempamount=(p.quantity *p.product.discount_price)
                amount=amount+tempamount
                total_amout=amount+shipping_amount
    if request.user.is_authenticated:
            cart=Cart.objects.filter(user=request.user)
            cart_quantity=0
            if cart:
                for i in range(len(cart)):
                    cart_quantity=cart_quantity+1
                
            else:
                cart_quantity=0
            return render(request,'app/addtocart.html',{'carts':cart,'total_amount':total_amout,'amount':amount,'quantity':cart_quantity})
    else:
        return render(request,'app/emptycart.html')
@login_required
def pluscart(request):
    if request.method=="GET":
        prod_id=request.GET['prod_id']
        c=Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity+=1
        c.save()
        amount=0.0
        shipping_amount=150.0
        total_amout=0.0
        cart_product=[p for p in Cart.objects.all() if p.user==request.user]
      
        if cart_product:
            for p in cart_product:

                tempamount=(p.quantity *p.product.discount_price)
                amount=amount+tempamount
                total_amout=amount+shipping_amount
               
            data={'quantity':c.quantity,'amount':amount,'total_amount':amount+shipping_amount}
            return JsonResponse(data)

@login_required
def minuscart(request):
    if request.method=="GET":
        prod_id=request.GET['prod_id']
        c=Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity-=1
        c.save()
        amount=0.0
        shipping_amount=150.0
        total_amout=0.0
        cart_product=[p for p in Cart.objects.all() if p.user==request.user]
      
        if cart_product:
            for p in cart_product:

                tempamount=(p.quantity *p.product.discount_price)
                amount=amount+tempamount
                total_amout=amount+shipping_amount
               
            data={'quantity':c.quantity,'amount':amount,'total_amount':amount+shipping_amount}
            return JsonResponse(data)
@login_required
def removecart(request):
    if request.method=="GET":
        prod_id=request.GET['prod_id']
        c=Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        print("deleted objec t",c)
        c.delete()
        amount=0.0
        shipping_amount=150.0
        total_amout=0.0
        
        cart_product=[p for p in Cart.objects.all() if p.user==request.user]
      
        if cart_product:
            for p in cart_product:
                tempamount=(p.quantity *p.product.discount_price)
                amount+=tempamount
                print(total_amout)
            data={'amount':amount,'total_amount':amount+shipping_amount}
            print(data)
            return JsonResponse(data)
        else:
            amount=0.0
            shipping_amount=150.0
            total_amout=0.0
            
            data={'amount':amount,'total_amount':amount+shipping_amount}
            print(data)
            return JsonResponse(data)

@login_required
def buy_now(request):
 return render(request, 'app/buynow.html')



def address(request):
    add=Customer.objects.filter(user=request.user)
    return render(request,'app/address.html',{'add':add,'active':'btn-primary'})

@login_required
def orders(request):
    op=OrderPlaced.objects.filter(user=request.user)
    if request.user.is_authenticated:
            cart=Cart.objects.filter(user=request.user)
            cart_quantity=0
            if cart:
                for i in range(len(cart)):
                    cart_quantity=cart_quantity+1
                
            else:
                cart_quantity=0
    return render(request, 'app/orders.html',{'op':op,'quantity':cart_quantity})



def mobile(request,data=None):
    if data==None:
        mobiles=Product.objects.filter(category='M')
    elif data=='Samsung' or data=='Huawei':
        mobiles=Product.objects.filter(category='M').filter(brand=data)
    elif data=='below':
        mobiles=Product.objects.filter(category='M').filter(discount_price__lt=10000)
    elif data=='above':
        mobiles=Product.objects.filter(category='M').filter(discount_price__gt=10000)
    cart_quantity=0
    if request.user.is_authenticated:
            cart=Cart.objects.filter(user=request.user)
            cart_quantity=0
            if cart:
                for i in range(len(cart)):
                    cart_quantity=cart_quantity+1
                
            else:
                cart_quantity=0
    return render(request, 'app/mobile.html',{'mobiles':mobiles,'quantity':cart_quantity})

def laptop(request,data=None):
    if data==None:
        mobiles=Product.objects.filter(category='L')
    elif data=='Hp' or data=='Dell':
        mobiles=Product.objects.filter(category='L').filter(brand=data)
    elif data=='below':
        mobiles=Product.objects.filter(category='L').filter(discount_price__lt=40000)
    elif data=='above':
        mobiles=Product.objects.filter(category='L').filter(discount_price__gt=40000)
    cart_quantity=0
    if request.user.is_authenticated:
            cart=Cart.objects.filter(user=request.user)
            
            if cart:
                for i in range(len(cart)):
                    cart_quantity=cart_quantity+1
                
            else:
                cart_quantity=0
    return render(request, 'app/laptop.html',{'mobiles':mobiles,'quantity':cart_quantity})

def login(request):
 return render(request, 'app/login.html')

# def customerregistration(request):
#  return render(request, 'app/customerregistration.html')

class customerregistration(View):
    def get(self,request):
        form=UserRegistrationform()
        return render(request,'app/customerregistration.html',{'form':form})
    def post(self,request):
        form=UserRegistrationform(request.POST)
        if form.is_valid():
            messages.success(request,'Congratulations!! Registered Successfully..')
            form.save()
        return render(request,'app/customerregistration.html',{'form':form})

@login_required
def checkout(request):
    add=Customer.objects.filter(user=request.user)
    cart_item=Cart.objects.filter(user=request.user)
    amount=0.0
    shipping_amount=150.0
    total_amout=0.0
    cart_product=[p for p in Cart.objects.all() if p.user==request.user]
      
    if cart_product:
        for p in cart_product:

            tempamount=(p.quantity *p.product.discount_price)
            amount=amount+tempamount
            total_amout=amount+shipping_amount
    
    if request.user.is_authenticated:
            cart=Cart.objects.filter(user=request.user)
            cart_quantity=0
            if cart:
                for i in range(len(cart)):
                    cart_quantity=cart_quantity+1
                
            else:
                cart_quantity=0
    return render(request, 'app/checkout.html',{'add':add,'totalamount':total_amout,'cartitem':cart_item,'quantity':cart_quantity})

@login_required
def paymentdone(request):
    user=request.user
    custid=request.GET.get('custid')
    print(custid)
    customer=Customer.objects.get(id=custid)
    print(customer)
    cart=Cart.objects.filter(user=request.user)
    for c in cart:
        OrderPlaced(user=user,customer=customer,product=c.product,quantity=c.quantity).save()
        c.delete()
    return redirect('orders')


def topwear(request,data=None):
    if data==None:
        product=Product.objects.filter(category='TW')
    elif data=='above':
        product=Product.objects.filter(category='TW').filter(discount_price__gt=500)
    elif data=='below':
        product=Product.objects.filter(category='TW').filter(discount_price__lt=500)
    cart_quantity=0
    if request.user.is_authenticated:
            cart=Cart.objects.filter(user=request.user)
            cart_quantity=0
            if cart:
                for i in range(len(cart)):
                    cart_quantity=cart_quantity+1
                
            else:
                cart_quantity=0
    
    return render(request,'app/topwear.html',{'products':product,'active':'btn-primary','quantity':cart_quantity})

def bottomwear(request,data=None):
    if data==None:
        product=Product.objects.filter(category='BW')
    elif data=='above':
        product=Product.objects.filter(category='BW').filter(discount_price__gt=500)
    elif data=='below':
        product=Product.objects.filter(category='BW').filter(discount_price__lt=500)
    cart_quantity=0
    if request.user.is_authenticated:
            cart=Cart.objects.filter(user=request.user)
            cart_quantity=0
            if cart:
                for i in range(len(cart)):
                    cart_quantity=cart_quantity+1
                
            else:
                cart_quantity=0
    
    return render(request,'app/bottomwear.html',{'products':product,'active':'btn-primary','quantity':cart_quantity})

@method_decorator(login_required,name='dispatch')
class ProfileView(View):
    def get(self,request):
        form=CustomerProfileform()
        return render(request,'app/profile.html',{'form':form,'active':'btn-primary'})

    def post(self,request):
        form=CustomerProfileform(request.POST)
        usr=request.user
        if form.is_valid():
            name=form.cleaned_data['name']
            locality=form.cleaned_data['locality']
            city=form.cleaned_data['city']
            state=form.cleaned_data['state']
            zipcode=form.cleaned_data['zipcode']
            reg=Customer(user=usr,name=name,locality=locality,city=city,state=state,zipcode=zipcode)
            reg.save()
            messages.success(request,'Congragulations! Profile Updated Successfully')
        return render(request,'app/profile.html',{'form':form,'active':'btn-primary'})
    
class Search(ListView):
    model=Product
    template_name="app/search.html"
    paginate_by=5

    def get_queryset(self):
        title=self.request.GET.get("title","")
        print(title)
        queryset=Product.objects.filter(title__icontains=title)
        print(queryset)
        return queryset

