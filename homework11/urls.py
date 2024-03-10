from django.urls import re_path
from app.views import TaskListView, TaskCreateView, TaskDetailView, TaskUpdateView, TaskDeleteView

urlpatterns = [
    re_path(r'^$', TaskListView.as_view(), name='list'),
    re_path(r'^create/$', TaskCreateView.as_view(), name='create'),
    re_path(r'^(?P<pk>\d+)/$', TaskDetailView.as_view(), name='detail'),
    re_path(r'^(?P<pk>\d+)/edit/$', TaskUpdateView.as_view(), name='edit'),
    re_path(r'^(?P<pk>\d+)/delete/$', TaskDeleteView.as_view(), name='delete'),
]
