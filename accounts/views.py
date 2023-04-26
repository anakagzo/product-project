from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from accounts.models import Acc



# Create your views here.
@login_required
def create_acc(request):
    if request.method == 'POST':
        print('oke')
        if request.POST['title'] and request.POST['body'] and request.FILES['icon'] and request.FILES['image']:
            account = Acc()
            account.title = request.POST['title']
            account.body = request.POST['body']
            account.icon = request.FILES['icon']
            account.image = request.FILES['image']
            account.pub_date = timezone.datetime.now()
            print('ok')
            if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
                account.url = request.POST['url']
            else:
                account.url = 'http://' + request.POST['url']

            account.save()
            return redirect('home')
        else:
            print('okay')
            return render(request, 'signup.html', {'error': "some fields are empty"})
    else:
        return render(request, 'create.html')

@login_required(login_url='/signup')
def pro_detail(request, product_id):
    product=get_object_or_404(Acc,pk=product_id)
    return render(request, 'detail.html', {'blog':product})

