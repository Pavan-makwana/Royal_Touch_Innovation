from django.shortcuts import render, redirect, get_object_or_404
from .google_sheets import save_to_sheet
from .models import Category, Product
from .forms import ProductRequestForm
from django.contrib import messages




def home(request):
    products = Product.objects.all()
    return render(request, "store/home.html", {"products": products})

def products(request):
    products = Product.objects.all()
    categories = Category.objects.prefetch_related("products")
    return render(request, "store/products.html", {
        "categories": categories,
        "products": products
    })
    

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, "store/product_detail.html", {"product": product})


def request_product(request, id):
    # Fetch all active products for the dropdown
    all_products = Product.objects.filter()
    # Fetch specific product for auto-selection
    product_obj = get_object_or_404(Product, id=id)

    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        product = request.POST.get("product", "").strip()
        quantity = request.POST.get("quantity", "").strip()
        phone = request.POST.get("phone", "").strip()
        # Add these to match your new form requirements
        email = request.POST.get("email", "").strip()
        message = request.POST.get("message", "").strip()

        # Validation logic using existing variable names
        if not name or not product or not quantity or not phone or not email:
            messages.error(request, "All fields are required.")
            return render(request, "store/request_form.html", {
                "product": product_obj,
                "all_products": all_products
            })

        # Basic phone check
        if not phone.isdigit() or len(phone) < 10:
            messages.error(request, "Please enter a valid phone number.")
            return render(request, "store/request_form.html", {
                "product": product_obj,
                "all_products": all_products
            })

        # Save to sheet
        save_to_sheet(name, product, quantity, phone, email, message)
        return redirect("request_success")

    # Pass BOTH variables to fix the dropdown and auto-fill
    return render(request, "store/request_form.html", {
        "product": product_obj,
        "all_products": all_products
    })


def confirmation(request):
    return render(request, "store/confirmation.html")

def request_success(request):
    return render(request, "store/request_success.html")

def privacy_policy(request):
    return render(request, "store/privacy_policy.html")

def terms_conditions(request):
    return render(request, "store/terms_conditions.html")

def contact(request):
    return render(request, 'store/contact.html')

def about(request):
    return render(request, 'store/about.html')
