from django.shortcuts import render,redirect, get_object_or_404
from .models import Vendor,Product
from django.http import JsonResponse
from .models import Product
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from .models import Product, Wishlist
#from django.contrib.auth.views import LogoutView

def index(request):
    return render(request, 'index.html')

def submit_vendor(request):
    if request.method == 'POST':
        name = request.POST.get('vendor-name')
        email = request.POST.get('vendor-email')
        product = request.POST.get('vendor-product')
        Vendor.objects.create(name=name, email=email, product=product)
        return render(request, 'success.html')
    return render(request, 'index.html')

def vendor_products(request):
   # vendor = get_object_or_404(Vendor, pk=vendor_id)
    products = Product.objects.all()
    return render(request, 'vendor_products.html', {'products': products})

def product_details(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'product_details.html', {'product': product})

def submit_vendor(request):
    if request.method == 'POST':
        name = request.POST.get('vendor_name')
        email = request.POST.get('vendor_email')
        product = request.POST.get('vendor_product')
        # Create a new Vendor object with the provided data
        Vendor.objects.create(name=name, email=email, product=product)
        return JsonResponse({'message': 'Vendor application submitted successfully!'})
    return JsonResponse({'error': 'Invalid request method'}, status=400)

def submit_form(request):
    if request.method == 'POST':
        # Retrieve form field values from request.POST
        name = request.POST.get('vendor_name')
        email = request.POST.get('vendor_email')
        product = request.POST.get('vendor_product')

        # Check if form fields are not empty
        if name and email and product:
            # Print or log the form data for debugging purposes
            print("Name:", name)
            print("Email:", email)
            print("Product:", product)

            # Process the form data as needed
            # For example, save it to the database, send emails, etc.

            # Return a success response
            return JsonResponse({'message': 'Form submitted successfully!'})
        else:
            # If any form field is empty, return an error response
            return JsonResponse({'error': 'All form fields are required'}, status=400)
    else:
        # If request method is not POST, return an error response
        return JsonResponse({'error': 'Invalid request method'}, status=400)
    

def logout_success(request):
    return render(request, 'logout_success.html')


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})

def add_to_wishlist(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, pk=product_id)
        # Add the product to the wishlist
        Wishlist.objects.create(product=product, user=request.user)
        return redirect('wishlist')  # Redirect to the wishlist page


from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def wishlist(request):
    wishlist_items = Wishlist.objects.filter(user=request.user)
    return render(request, 'wishlist.html', {'wishlist_items': wishlist_items})
@login_required
def dashboard(request):
    return render(request, 'dashboard.html')
@login_required
def profile(request):
    user = request.user
    return render(request, 'profile.html', {'user': user})
@login_required
def update_profile(request):
    if request.method == 'POST':
        form = CustomUserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('update_success')
    else:
        form = CustomUserUpdateForm(instance=request.user)
    return render(request, 'update_profile.html', {'form': form})

def update_success(request):
    return render(request, 'update_success.html')


def customer_home(request):
    return render(request, 'customer_home.html')




def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})

@login_required
def add_interest(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    
    # Check if the user has already marked interest for this product
    existing_interest = Interest.objects.filter(user=request.user, product=product).exists()
    if existing_interest:
        # Redirect with a message indicating that the user has already marked interest
        return redirect('product_details', product_id=product_id)

    # Create a new interest instance
    interest = Interest.objects.create(user=request.user, product=product)
    
    # Mark the interest as "interested" for the user
    interest.interested_users.add(request.user)
    
    # Redirect to the product details page
    return redirect('product_details', product_id=product_id)
    
@login_required
def remove_interest(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        # Check if the user has expressed interest
        existing_interest = Interest.objects.filter(user=request.user, product=product).first()
        if existing_interest:
            # Remove the interest
            existing_interest.delete()
        return redirect('product_details', product_id=product_id)
    return redirect('product_details', product_id=product_id)
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save
            if product.has_document and 'document_file' in request.FILES:
                product.document_file = request.FILES['document_file']
            product.save()
            return redirect('customer_products')
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})
