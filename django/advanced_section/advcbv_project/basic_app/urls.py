from django.urls import path
from . import views

app_name='basic_app'

# url for class_based view
urlpatterns = [
    # path('',views.HomeView.as_view(),name="home"),
    path('schools/',views.SchoolListView.as_view(),name='school_list'),
    path('schools/<int:pk>/',views.SchoolDetailView.as_view(),name='school_detail'),
    path('schools/create/',views.SchoolCreateView.as_view(),name='school_create'),
    path('schools/update/<int:pk>/',views.SchoolUpdateView.as_view(),name='school_update'),
    path('schools/delete/<int:pk>/',views.SchoolDeleteView.as_view(),name='school_delete'),

    # path('',views.CBView.as_view(),name="home"),
]

# url for function_based view

# urlpatterns = [
#     path('',views.home,name="home"),
# ]

