from Quiz import views
from django.urls import path,include

app_name = 'quiz'

urlpatterns = [
    path('',views.QuizSel,name='qt'),
]
