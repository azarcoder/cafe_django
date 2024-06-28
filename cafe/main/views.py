from django.shortcuts import render, redirect
from .models import Coffee,Customers, Order
from django.contrib import messages
from .forms import LoginForm, UserRegisterationForm

cart_total = 0

def main(request):
    product = Coffee.objects.all()
    return render(request, 'index.html', {'coffee' : product, 'cart_total' : cart_total})

def signup(request):
    if request.method == 'POST':
        form = UserRegisterationForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Registered Successfully')
            except Exception as e:
                messages.error(request, f"An error occurred {e}")
    else:
        form = UserRegisterationForm()
    
    return render(request, 'userSignup.html', {'form': form})


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            try:
                user = Customers.objects.get(name = username, password = password)
                if user:
                    request.session['user_name'] = username
                    messages.success(request, 'Login successful!')
                    return redirect('main')
            except Customers.DoesNotExist:
                messages.error(request, 'Invalid username or password')

    else:
        form = LoginForm()
    
    return render(request, 'userLogin.html', {'form': form})

def logout(request):
    request.session.clear()
    messages.success(request, 'Logout Successfully')
    return redirect('main')

def Buy(request,id):
    product = Coffee.objects.get(id = id)
    if request.method == 'POST':
        return render(request, 'buypage.html', {'coffee': product})
    else:
        return render(request, 'buypage.html', {'coffee': product})
        

def buying(request,id):
    if request.method == 'POST':
        coffee = Coffee.objects.get(id = id)
        count = int(request.POST['count'])
        if coffee.totalCount >= count:
            try:
                username = request.session.get('user_name')
                if username:
                    user = Customers.objects.get(name = username)
                    order = Order.objects.create(customer = user, coffee = coffee, quantity = count)
                    coffee.totalCount -= count
                    if coffee.totalCount == 0:
                        coffee.availability = False
                    order.save()
                    coffee.save()
                    messages.success(request, 'Ordered Successfully')
                    return redirect('buy', id=coffee.id)
                else:
                    messages.error(request, 'Kindly login before making order')
                    return redirect('buy', id=coffee.id)
            except Customers.DoesNotExist:
                messages.error(request, 'Customer data not found in database')
                return redirect('buy', id=coffee.id)
        else:
            messages.error(request, f'Sorry :( Only {coffee.totalCount} available!')
            return redirect('buy', id=coffee.id)

def order(request):
    try:
        username = request.session.get('user_name')
        if username:
            customer = Customers.objects.get(name=username)
            orders = Order.objects.filter(customer=customer)
            return render(request, 'orderPage.html', {'orders': orders})
        else:
            messages.error(request, 'Please login to check your orders')
            return redirect('main')
    except Customers.DoesNotExist:
        messages.error(request, 'Customer data not found')
        return redirect('main')
    except Order.DoesNotExist:
        messages.info(request, 'No orders found for this customer')
        return render(request, 'orderPage.html', {'orders': []}) 
    except Exception as e:
        messages.error(request, f'Error: {e}')
        return redirect('main')