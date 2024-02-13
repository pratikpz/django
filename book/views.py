from django.shortcuts import render,redirect,HttpResponse
from .models import Book
from .forms import BookCreate
# Create your views here.
def library(request):
    shelf = Book.objects.all()
    return render(request,'library.html',{'pratik':shelf})

def upload(request):
    upload=BookCreate()
    if request.method=='POST':
        upload=BookCreate(request.POST,request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('library')
        else:
            return HttpResponse("Something went wrong.Please reload the page")
    else:
        return render(request,'uploadForm.html',{'upload_form': upload})
 