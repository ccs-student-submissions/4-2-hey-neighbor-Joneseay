from django.urls import path
from .views import HomePageView, AvailableToolsView, AddToolsView, ToolsEditView, ToolsDeleteView, ToolsDetailView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('tools/<available>/', AvailableToolsView.as_view(), name='available')

]