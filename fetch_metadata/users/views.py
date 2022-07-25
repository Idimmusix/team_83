
from django.shortcuts import HttpResponse, render
from .forms import user_Upload_Form
from django.contrib import messages

# Create your views here.
def uploadFile(request):
    if request.method == 'POST':
        form = user_Upload_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('the file is uploaded')
        
    else:
        form = user_Upload_Form()
    
    return render(request, 'users/userUpload.html', {'form': form })


