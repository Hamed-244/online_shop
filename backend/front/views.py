from django.shortcuts import render
from admin_panel.models import Category, Product, ProductImage, OrderItem, ShippingAddress, Feedback, Order, Payment
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.db.models import Count, Sum


def home(request):
    categorys = Category.objects.all()
    products = Product.objects.all()[0:10]
    if request.user.is_authenticated :
        order_items = OrderItem.objects.filter(order__user=request.user)
    else :
        order_items = []
    count_product_in_order_item = order_items.count() if order_items else 0
    total_price = sum(item.total_price() for item in order_items)

    return render(request, 'html/index.html',{
        'categorys': categorys,
        'products': products,
        'order_items': order_items,
        'count_product_in_order_item': count_product_in_order_item,
        'total_price': total_price,
    })


def store(request):
    products = Product.objects.all()
    categorys = Category.objects.all()
    if request.user.is_authenticated :
        order_items = OrderItem.objects.filter(order__user=request.user)
    else :
        order_items = []
    count_product_in_order_item = order_items.count() if order_items else 0
    total_price = sum(item.total_price() for item in order_items)
    total_price = sum(item.total_price() for item in order_items)

    category_product_count = {}
    for category in categorys:
        category_product_count[category.name] = products.filter(category=category).count()

    return render(request, 'html/store.html', {
        'products': products,
        'categorys': categorys,
        'category_product_count': category_product_count,
        'order_items': order_items,
        'count_product_in_order_item': count_product_in_order_item,
        'total_price': total_price,
    })


def product_detail(request, slug):
    product = Product.objects.get(slug=slug)
    product_images = ProductImage.objects.filter(product=product)
    related_products = Product.objects.filter(category__in=product.category.all()).exclude(id=product.id)
    if request.user.is_authenticated :
        order_items = OrderItem.objects.filter(order__user=request.user)
    else :
        order_items = []
    count_product_in_order_item = order_items.count() if order_items else 0
    total_price = sum(item.total_price() for item in order_items)
    total_price = sum(item.total_price() for item in order_items)

    return render(request, 'html/product.html', {
        'product': product,
        'product_images': product_images,
        'related_products': related_products,
        'order_items': order_items,
        'count_product_in_order_item': count_product_in_order_item,
        'total_price': total_price,
    })


def store_category(request, category_name):
    category = Category.objects.get(name=category_name)
    products_filter = Product.objects.filter(category=category)
    products = Product.objects.all()
    categorys = Category.objects.all()
    if request.user.is_authenticated :
        order_items = OrderItem.objects.filter(order__user=request.user)
    else :
        order_items = []
    count_product_in_order_item = order_items.count() if order_items else 0
    total_price = sum(item.total_price() for item in order_items)
    total_price = sum(item.total_price() for item in order_items)

    category_product_count = {}
    for category in categorys:
        category_product_count[category.name] = products.filter(category=category).count()

    return render(request, 'html/store_search_by_categoty.html', {
        'products': products_filter,
        'categorys': categorys,
        'category_product_count': category_product_count,
        'order_items': order_items,
        'count_product_in_order_item': count_product_in_order_item,
        'total_price': total_price,
    })


@login_required
def add_to_cart(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        product = get_object_or_404(Product, id=product_id)
        product.amount -=1
        product.save()
        order_qs = Order.objects.filter(user=request.user, status='pending')
        if order_qs.exists():
            order = order_qs[0]
        else:
            order = Order.objects.create(user=request.user)
        OrderItem.objects.create(
            product=product,
            order=order,
            quantity=1,
        )
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})


@login_required
def remove_from_cart(request):
    if request.method == 'POST':
        order_item_id = request.POST.get('order_item_id')
        order_item = get_object_or_404(OrderItem, id=order_item_id, order__user=request.user)
        product = order_item.product
        product.amount +=1
        product.save()
        order_item.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})


@login_required
def checkout(request):
    order_items = OrderItem.objects.filter(order__user=request.user)
    order_items_che = OrderItem.objects.filter(order__user=request.user).values('product__name').annotate(total=Count('product'), price=Sum('product__price'))
    total_price = sum(item.total_price() for item in order_items)
    return render(request, 'html/checkout.html', {
        'order_items': order_items_che,
        'total_price': total_price,
    })

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
@login_required
def place_order(request):
    if request.method == 'POST':
        data = request.POST
        shippingaddress = ShippingAddress.objects.create(
            user=request.user,
            title=data.get('first_name') + ' ' + data.get('last_name'),
            address_line1=data.get('address_line1'),
            address_line2=data.get('address_line2'),
            city=data.get('city'),
            state=data.get('state'),
            postal_code=data.get('postal_code')
        )
        order = Order.objects.create(
            user=request.user,
            shipping_address=shippingaddress,
        )

        payment = Payment.objects.create(
            order=order,
            amount=data.get('amount'),
            payment_method=data.get('payment_method')
        )

        feedback = Feedback.objects.create(
            order=order,
            rating=data.get('rating'),
            comment=data.get('notes'),
        )

        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'invalid method'})


@login_required
def show_order(request):
    orders = Order.objects.all()
    return render(request, 'html/show_order.html', {
        'orders': orders,
    })