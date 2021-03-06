from django.urls import path
from . import views

urlpatterns = [
    # Home and About
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    # Finch list and detail
    path('finches/', views.finches_index, name='index'),
    path('finches/<int:finch_id>/', views.finches_detail, name='detail'),
    # Finch create , edit and delete
    path('finches/create/', views.FinchCreate.as_view(), name='finches_create'),
    path('fiches/<int:pk>/update/',
         views.FinchUpdate.as_view(), name='finches_update'),
    path('finches/<int:pk>/delete/',
         views.FinchDelete.as_view(), name='finches_delete'),
    # Finch feeding

    path('finches/<int:finch_id>/add_feeding/',
         views.add_feeding, name='add_feeding'),
    # Finch photos
    path('finches/<int:finch_id>/add_photo/',
         views.add_photo, name='add_photo'),
    #     path('photos/<int:pk>/delete/', views.PhotoDelete.as_view(),
    #          name='photos_delete'),

    path('finches/<int:finch_id>/photos/<int:photo_id>/delete/',
         views.photos_delete, name='photos_delete'),


    # Toy list and detail
    path('toys/', views.ToyList.as_view(), name='toys_index'),
    path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toys_detail'),
    # Toy create, update, delete
    path('toys/create/', views.ToyCreate.as_view(), name='toys_create'),
    path('toys/<int:pk>/update/',
         views.ToyUpdate.as_view(), name='toys_update'),
    path('toys/<int:pk>/delete/',
         views.ToyDelete.as_view(), name='toys_delete'),

    # Finch and Toy association
    path('finches/<int:finch_id>/assoc_toy/<int:toy_id>/',
         views.assoc_toy, name='assoc_toy'),
    # Signup
    path('accounts/signup/', views.signup, name='signup'),


]
