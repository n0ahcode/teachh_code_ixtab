from django.shortcuts import render
from .models import CodeModel,Tag
from .forms import CodeModelForm,SearchForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django_filters.views import FilterView
from .filters import ItemFilter


def index(request):
    searchform = SearchForm
    codes = CodeModel.objects.all()
    context = {
    'searchform':searchform,
    'codes':codes,
    }
    if request.method == 'POST':
        str = request.POST['search']
        search_word = CodeModel.objects.filter(title__contains=str)
        context['search_word'] = search_word
    return render(request,'app/index.html',context)


def contribution(request):
    code_form = CodeModelForm
    context = {
        'code_form':code_form,
    }

    return render(request,'app/contribution.html',context)


def add(request):
    form = CodeModelForm(request.POST)
    form.save()
    return HttpResponseRedirect(reverse('index'))




def event(request,id):
    codes = CodeModel.objects.all().filter(id=id)

    context = {
    'codes':codes,
    }
    return render(request,'app/event.html',context)


class ItemFilterView(FilterView):
    model = CodeModel
    filterset_class = ItemFilter
    queryset = CodeModel.objects.all().order_by('-date')
    strict = False

    paginate_by = 10



    def get(self,request,**kwargs):
        if request.GET:
            request.session['query'] = request.GET
        else:
            request.GET = request.GET.copy()
            if 'query' in request.session.keys():
                for key in reqeust.session['query'].keys():
                    request.GET[key] = request.session['query'][key]

        return super().get(request,**kwargs)                
