from django.shortcuts import render


# Create your views here.
def index(request):
    data_structures = ['Array', 'Linked list', 'Stack', 'Queue', 'Tree', 'Trie', 'Hash table', 'Heap', 'Graph']
    return render(request, 'list_items.html', {'items': data_structures})


def card_list(request):
    cards = [
        {'name': 'Picture 1', 'location': 'static/images/1.png'},
        {'name': 'Picture 2', 'location': 'static/images/2.png'},
        {'name': 'Picture 3', 'location': 'static/images/3.png'},
        {'name': 'Picture 4', 'location': 'static/images/4.png'},
    ]
    return render(request, 'card_list.html', {'cards': cards})


def table_list(request):
    items = [
        {'id': 1, 'name': 'Item 1', 'price': 10.99},
        {'id': 2, 'name': 'Item 2', 'price': 5.99},
        {'id': 3, 'name': 'Item 3', 'price': 12.99},
        {'id': 4, 'name': 'Item 4', 'price': 8.99},
        {'id': 5, 'name': 'Item 5', 'price': 15.99}
    ]
    return render(request, 'table_list.html', {'items': items})
