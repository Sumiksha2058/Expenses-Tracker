from django.urls import path
from .views import expense_list, add_expense, category_list, add_category

urlpatterns = [
    path('', expense_list, name='expense_list'),
    path('add/', add_expense, name='add_expense'),
    path('categories/', category_list, name='category_list'),
    path('categories/add/', add_category, name='add_category'),
]
