from django.views.generic import ListView, CreateView, DetailView, TemplateView
from django.views.generic.edit import UpdateView, DeleteView
from .models import Tool


class HomePageView(TemplateView):
    model = Tool
    template_name = 'home.html'


class AvailableToolsView(ListView):
    model = Tool
    template_name = 'available_tools.html'


class AddToolsView(CreateView):
    model = Tool
    template_name = 'add_tools.html'
    fields = ['name', 'type', 'work_field', 'manufacturer', 'replacement_cost', 'URL', 'condition', 'borrowed', 'owner']


class ToolsDetailView(DetailView):
    model = Tool
    template_name = 'tool_detail.html'


class ToolsEditView(UpdateView):
    model = Tool
    template_name = 'edit_tools.html'
    fields = ['name', 'type', 'work_field', 'manufacturer', 'replacement_cost', 'URL', 'condition', 'borrowed', 'owner']


class ToolsDeleteView(DeleteView):
    model = Tool
    template_name = 'delete_tools.html'

