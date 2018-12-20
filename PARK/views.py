from django.shortcuts import render
#from django.http import HttpResponse
from PARK.forms import NewUserForms

# Create your views here.
def index(request):
          return render(request,'pages/index.html')

def users(request):
          form =NewUserForms()

          if request.method=="POST":
                    form=NewUserForms(request.POST)

                    if form.is_valid():
                              domain=form.cleaned_data['select']
                              form.save(commit=True)
                              return index(request)
                    else:
                              print("ERROR FORM INVALID")
                                  
          return render(request,'pages/form_page.html',{'form':form})    
                                 

                             

