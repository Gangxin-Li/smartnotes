from django.shortcuts import render
from .models import Notes
from django.http import Http404
from django.views.generic import ListView,DetailView
# Create your views here.

class NodeListView(ListView):
    model = Notes
    context_object_name = "notes"
    template_name = "notes_list.html"

# def list(request):
#     all_notes = Notes.objects.all()
#     return render(request, 'notes_list.html',{'notes':all_notes})

class NodeDetailView(DetailView):
    model = Notes
    context_object_name = "note"
    template_name = "notes_detail.html"

# def detail(request, pk):
#     try:
#         note = Notes.objects.get(pk=pk)
#     except Notes.DoesNotExist:
#         raise Http404("note does not exist!")
#     return render(request,'notes_detail.html',{'note':note})