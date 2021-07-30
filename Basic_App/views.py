from django.shortcuts import render,redirect
from django.views.generic import (
TemplateView,ListView,CreateView,DeleteView,DetailView,UpdateView)
from Basic_App.models import home,Shop,Checkout,Categori
from Basic_App.form import Checkoutform
from django.db.models import Q
from django.core.paginator import Paginator


# Create your views here.
class indexlist(ListView):

    model=home

    template_name='indexhelper.html'
    context_object_name='pos'
    paginate_by = 1
    queryset = home.objects.all()


class indexDetailView(DetailView):
    model=home
    queryset = home.objects.all()
    template_name='product-details.html'
    context_object_name='pos'
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['author-list'] = home.objects.all()
        return context
class indsercelist(ListView):

    model=home
    queryset = home.objects.all()
    template_name='indexhelper.html'
    context_object_name='pos'
    def get_queryset(self):
        search=self.request.GET.get('q')
        if search:
            pos=self.queryset.filter(
        Q(title__icontains=search)|Q(price__icontains=search)|Q(posted_on__icontains=search)

            )
        else:
            pos = self.model.objects.none()
        return pos


class Shoplist(ListView):

    paginate_by = 3
    template_name='shop.html'
    model=Shop
    def get_queryset(self):
        search=self.request.GET.get('q')
        if search:
            pos=self.model.objects.filter(
            Q(Category__icontains=search)

            )
        else:
            pos= self.model.objects.none()
        return pos

    def get_context_data(self, **kwargs):
        context = super(Shoplist, self).get_context_data(**kwargs)
        context['pos'] = Shop.objects.order_by('posted_on')
        context['postt']=Categori.objects.all()

        return context

class ShopDetailView(DetailView):
    model=Shop
    queryset = Shop.objects.all()
    template_name='shop-product-details.html'
    context_object_name='pos'
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['author-list'] = home.objects.all()
        return context


class CartDetailView(DetailView):
    model=Shop
    queryset = Shop.objects.all()
    template_name='cart.html'
    context_object_name='pos'
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['author-list'] = home.objects.all()
        return context
class indexCartDetailView(DetailView):
    model=home
    queryset = home.objects.all()
    template_name='cart.html'
    context_object_name='pos'
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['author-list'] = home.objects.all()
        return context
def checkout(request):
    if request.method=='POST':
        form=Checkoutform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Basic_App:index')
    else:
        form=Checkoutform()
    return render(request,"checkout.html",{'form':form})

def shop(request):
    return render(request,"shop.html")
