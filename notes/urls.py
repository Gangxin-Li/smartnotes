# -*- coding: utf-8 -*-
from django.urls import path
from . import views

urlpatterns=[
    path('notes',views.NodeListView.as_view()),
    path('notes/<int:pk>',views.NodeDetailView.as_view()),
    ]
