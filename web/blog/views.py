from django.shortcuts import render
from database.models import Category
from .models import Blogs
from django.core.paginator import Paginator , EmptyPage , InvalidPage

# Create your views here.
def index(request):
    categories = Category.objects.all()
    blog = Blogs.objects.all()
    lastest = Blogs.objects.all().order_by('-pk')[:4]


    #pagination การแบ่งเพจ
    paginator = Paginator(blog, 4)
    try:
        page = int(request.GET.get('page','1'))
    except:
        page = 1
    try:
        blogperpage = paginator.page(page)
    except (EmptyPage,InvalidPage):
        blogperpage = paginator.page(paginator.num_pages)


    return render(request, 'index.html',{'categories':categories, 'blog':blogperpage, 'lastest':lastest,
                                        'page':page})