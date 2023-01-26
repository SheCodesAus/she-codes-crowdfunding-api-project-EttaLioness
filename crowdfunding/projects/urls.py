from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('projects/', views.ProjectList.as_view()),
    path('projects/<int:pk>/', views.ProjectDetail.as_view()),
    path('pledges/', views.PledgeList.as_view()),
    path('pledges/<int:pk>/', views.PledgeDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

# Including format_suffix_patterns is an optional choice that provides a simple, 
# DRY way to refer to a specific file format for a URL endpoint. 
# It means our API will be able to handle URls such as http://example.com/api/items/4.json rather 
# than just http://example.com/api/items/4.