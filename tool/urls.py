from django.urls import path
from .views import HomePageView, AvailableToolsView, AddToolsView, ToolsEditView, ToolsDeleteView, ToolsDetailView, \
    AllToolsView, MyToolsView, UserToolsListView, BorrowToolView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('tools/available/', AvailableToolsView.as_view(), name='available'),
    path('tools/new/', AddToolsView.as_view(), name='add_tools'),
    path('tools/<int:pk>/', ToolsDetailView.as_view(), name='detail_tools'),
    path('tools/<int:pk>/edit', ToolsEditView.as_view(), name='edit_tools'),
    path('tools/<int:pk>/delete', ToolsDeleteView.as_view(), name='delete_tools'),
    path('tools/all/', AllToolsView.as_view(), name='all_tools'),
    path('tools/mytools/', MyToolsView.as_view(), name='my_tools'),
    path('tools/<int:pk>/owner/', UserToolsListView.as_view(), name='users_tools'),
    path('tools/<int:pk>/borrowed/', BorrowToolView.as_view(), name='borrow_tool')
]
