# from django.urls import path
# from app import views

# urlpatterns = [
#     path('',views.index,name='index'),
#     path('about',views.about,name='about'),
#     path('contact',views.contact,name='contact'),
#     path('insert',views.insertData,name='insertData'),
#     path('update/<id>',views.updateData,name='updateData'),
#     path('delete/<id',views.deleteData,name='deleteData'),
# ]



from django.urls import path
from app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('insert/', views.insertData, name='insertData'),
    path('update/<int:id>/', views.updateData, name='updateData'),
    path('delete/<int:id>/', views.deleteData, name='deleteData'),
]

