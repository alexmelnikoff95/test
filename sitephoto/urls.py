from django.urls import path
from sitephoto.views import PhotoList, BlogList, PhotoDetail, BaseView, BlogDetail, AboutView, ConnectionCreate, \
    ConnectionUpdate, ConnectionDelete

urlpatterns = [
    path('', BaseView.as_view(), name='base_view'),
    path('photo/', PhotoList.as_view(), name='photo_list'),
    path('blog/', BlogList.as_view(), name='blog_list'),
    path('about/', AboutView.as_view(), name='about'),
    path('connection/', ConnectionCreate.as_view(), name='connection'),
    path('connection/<int:pk>/', ConnectionUpdate.as_view(), name='update'),
    path('connection/delete/<int:pk>/', ConnectionDelete.as_view(), name='delete'),
    path('<slug:slug>/', PhotoDetail.as_view(), name='photo_detail'),
    path('blog/<slug:slug>/', BlogDetail.as_view(), name='blog_detail'),
]
