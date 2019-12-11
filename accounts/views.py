from django.shortcuts import render

# Create your views here.
def register_view(request):
    if request.method == "POST":
        print("Called post method")
        return render(request,'kalpataruapp/register.html')
    else:
        print("Called get method")
        return render(request,'kalpataruapp/register.html')

