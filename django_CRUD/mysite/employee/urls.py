from django.urls import path
from . import views
from .views import(
	tbl_empCreateView,
	tbl_empUpdateView,
	tbl_empDeleteView,
	)


urlpatterns = [
	path('', views.home, name="home"),
	path('employee/<int:emp_id>', views.details, name="details"),
	path('newEmployee/', tbl_empCreateView.as_view(), name="emp-create"),
	path('employee/<int:pk>/update/', tbl_empUpdateView.as_view(), name="emp-update"),
    path('employee/<int:pk>/delete/', tbl_empDeleteView.as_view(), name="emp-delete")
]