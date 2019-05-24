from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.views.generic import ListView, CreateView, DetailView, TemplateView
from django.views.generic.edit import UpdateView, DeleteView
from .models import Tool


class HomePageView(TemplateView):
    model = Tool
    template_name = 'home.html'


class AvailableToolsView(ListView):
    model = Tool
    template_name = 'available_tools.html'

    queryset = Tool.objects.filter(borrowed=True)


class AddToolsView(LoginRequiredMixin, CreateView):
    model = Tool
    template_name = 'add_tools.html'
    fields = ['name', 'type', 'work_field', 'manufacturer', 'replacement_cost', 'URL', 'condition', 'borrowed']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ToolsDetailView(DetailView):
    model = Tool
    template_name = 'tool_detail.html'


class ToolsEditView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model = Tool
    template_name = 'edit_tools.html'
    fields = ['name', 'type', 'work_field', 'manufacturer', 'replacement_cost', 'URL', 'condition', 'borrowed', 'owner']

    def test_func(self):
        obj = self.get_object()
        return obj.owner == self.request.user


class ToolsDeleteView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    model = Tool
    template_name = 'delete_tools.html'

    def test_func(self):
        obj = self.get_object()
        return obj.owner == self.request.user

class AllToolsView(ListView):
    model = Tool
    template_name = 'all_tools.html'


class UserToolsListView(ListView):
    model = Tool
    template_name = 'users_tools.html'

    def get_queryset(self):
        return Tool.objects.filter(owner__id=self.kwargs['pk'])

class MyToolsView(LoginRequiredMixin, ListView):
    model = Tool
    template_name = 'my_tools.html'

    def get_queryset(self):
        return Tool.objects.filter(owner=self.request.user)


class BorrowToolView(LoginRequiredMixin, UpdateView):
    model = Tool
    template_name = 'edit_tools.html'
    fields = ['borrowed']


