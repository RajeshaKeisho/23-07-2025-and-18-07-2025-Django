from django.shortcuts import render, redirect, get_object_or_404
from .models import Item
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from .forms import ItemForm
from django.urls import reverse_lazy

def item_list(request):
    items = Item.objects.all()
    return render(request, 'myapp/item_list.html', {'items': items})

def item_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'myapp/item_detail.html', {'item': item})

def item_create(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('fbv_item_list')
    else:
        form = ItemForm()
    return render(request, 'myapp/item_create.html', {'form': form})

def item_update(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('fbv_item_detail', pk=item.pk)
    else:
        form = ItemForm(instance=item)
    return render(request, 'myapp/item_form.html', {'form': form})

def item_delete(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('fbv_item_list')
    return render(request, 'myapp/item_confirm_delete.html', {'item': item})
# Create your views here.
# CBV:
class ItemListView(ListView):
    model = Item
    template_name = 'myapp/item_list.html'
    context_object_name = 'items'

class ItemDetailView(DetailView):
    model = Item
    template_name = 'myapp/item_detail.html'
    context_object_name = 'item'

class ItemCreateView(CreateView):
    model = Item
    form_class = ItemForm
    template_name = 'myapp/item_create.html'
    success_url = reverse_lazy('item_list_cbv')

class ItemUpdateView(UpdateView):
    model = Item
    form_class = ItemForm
    template_name = 'myapp/item_form.html'
    success_url = reverse_lazy('item_list_cbv')

class ItemDeleteView(DeleteView):
    model = Item
    template_name = 'myapp/item_confirm_delete.html'
    success_url = reverse_lazy('item_list_cbv')