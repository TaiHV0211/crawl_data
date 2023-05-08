from django.urls import path,include

from . import views

urlpatterns = [
    path('', views.real_estate_list, name='real_estate_list'),
    path('view/<int:pk>', views.real_estate_view, name='real_estate_view_view'),
    path('real_estate_search', views.real_estate_search, name='real_estate_search'),
]


# path('view/<int:pk>', views.RealEstateView.as_view(), name='real_estate_view'),
# path('new', views.BookCreate.as_view(), name='book_new'),
# path('view/<int:pk>', views.RealEstateView.as_view(), name='real_estate_view'),
# path('edit/<int:pk>', views.BookUpdate.as_view(), name='book_edit'),
# path('delete/<int:pk>', views.BookDelete.as_view(), name='book_delete'),