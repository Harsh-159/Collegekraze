from django.shortcuts import render

# Create your views here.

def QuizSel(request):
    
    return render(request,'Quiz/sel.html',{'form':form})
