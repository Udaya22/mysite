from django.urls import path
from polls import views

app_name = 'polls'

urlpatterns = [
    path('',views.index,name='index'),
    path('<int:pk>/detail',views.DetailView.as_view(),name='detail'),
    path('<int:pk>/result',views.ResultsView.as_view(),name='result'),
    path('<int:qid>/vote',views.vote,name='vote'),
]