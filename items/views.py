#  Items views

# Django
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# Models
from items.models import Item

# forms
from items.forms import SellerForm

# Role
from rolepermissions.checkers import has_role, get_user_roles

# cloudinary custom functions
from items.cloudinary_lib import CloudinaryFunctions


@login_required(login_url='login')
def view_item(request):
    if request.method == 'GET':
        is_seller = has_role(request.user, 'seller')
        items = Item.objects.all()

        if len(items) == 0:
            return render(request, 'items/view_item.html', {'is_seller': is_seller, 'error': 'There is nothing here'})

    return render(request, 'items/view_item.html', {'items': items, 'is_seller': is_seller})


@login_required(login_url='login')
def view_seller(request):
    if request.method == 'POST':
        form = SellerForm(request.POST, request.FILES)
        if form.is_valid():
            form_data = form.cleaned_data

            if item_exist(request, form_data['title']):
                return render(request, 'items/view_seller.html', {'form': form, 'error': 'You already have this ad'})

            result = CloudinaryFunctions.upload(form_data['picture'])

            Item.objects.create(
                title = form_data['title'],
                description = form_data['description'],
                price = form_data['price'],
                picture = {
                  'url': result['secure_url'],
                  'id': result['public_id'],
                },
                tags = form_data['tags'],
                classification = form_data['classification'],
                user=request.user
            )

            return redirect('seller_my_items')

    else:
        form = SellerForm()


    if request.method == 'GET':
        is_buyer = has_role(request.user, 'buyer')
        if is_buyer:
            return redirect('items')

    return render(request, 'items/view_seller.html', {'form': form})


@login_required(login_url='login')
def view_my_items(request):
    if request.method == 'GET':
        is_buyer = has_role(request.user, 'buyer')
        if is_buyer:
            return redirect('items')

    items = check_my_items(request.user.id)

    if not items:
        return render(request, 'items/view_my_items.html', {'error': "You don't have ads yet"})
    else:
        return render(request, 'items/view_my_items.html', {'items': items})

    return render(request, 'items/view_my_items.html')


@login_required(login_url='login')
def view_edit(request, id):
    if request.method == 'GET':
        is_buyer = has_role(request.user, 'buyer')
        if is_buyer:
            return redirect('items')

        item = get_item(id)

        if not Item.objects.filter(user_id=request.user.id).filter(id=id):
            return redirect('seller_my_items')

        if not item:
            return redirect('seller_my_items')

        form_data = {
            'title': item.title,
            'description': item.description,
            'price': item.price,
            'picture': item.picture,
            'tags': item.tags,
            'classification': item.classification
        }

        form = SellerForm(form_data)

    if request.method == 'POST':
        form = SellerForm(request.POST, request.FILES)

        if form.is_valid():
            form_data = form.cleaned_data
            item = get_item(id)

            if not item:
                return render(request, 'items/view_edit.html', {'id': id, 'form': form, 'error': 'Id does not exists'})

            result = CloudinaryFunctions.update(form_data['picture'], item.picture['id'])

            item.title = form_data['title']
            item.description = form_data['description']
            item.price = form_data['price']
            item.picture = {
                'url': result['secure_url'],
                'id': result['public_id'],
            }
            item.tags = form_data['tags']
            item.classification = form_data['classification']
            item.save()

            return redirect('seller_my_items')

    return render(request, 'items/view_edit.html', {'id': id, 'form': form})


@login_required(login_url='login')
def delete(request, id):
    is_buyer = has_role(request.user, 'buyer')
    if is_buyer:
        return redirect('items')

    if request.method == 'GET':
        item = get_item(id)

        if not item:
            return redirect('seller_my_items')

        if Item.objects.filter(user_id=request.user.id).filter(id=id):
            result = CloudinaryFunctions.delete(item.picture['id'])
            item.delete()

    return redirect('seller_my_items')


def get_item(item_id):
    # Get specific item by id
    try:
        item = Item.objects.get(id=item_id)
    except Item.DoesNotExist:
        item = False

    return item


def item_exist(request, title):
    return Item.objects.filter(title=title).filter(user_id=request.user.id).exists()


def check_my_items(user_id):
    # Get all items from this user
    items = Item.objects.filter(user_id=user_id)

    if len(items) == 0:
        return False
    else:
        return items
