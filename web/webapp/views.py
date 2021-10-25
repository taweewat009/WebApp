from django.shortcuts import render, redirect, reverse
from database.models import *
from django.core.paginator import Paginator



def main(request):
    return render(request, 'main.html')

def comment(request):
    err_msg = None
    if request.method == 'POST':
        form = GuestbookForm(request.POST)
        if form.is_valid():
            form.save()
            data = Guestbook.objects.all().order_by('-date')
            return redirect(reverse('comment_view', kwargs={'pg':1}),{'data':data})
        else:
            err_msg = 'ข้อมูลผิดพลาด'
    else:
        form = GuestbookForm()
    
    return render(request, 'index.html',{'form':form, 'err_msg':err_msg})

def comment_view(request, pg):
    data = Guestbook.objects.all().order_by('-date')
    pgn = Paginator(data, 3)
    page = pgn.get_page(pg)

    return render(request, 'view-comment.html',{'page':page})