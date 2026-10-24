from django.urls import path
from. import views


urlpatterns = [
    path('',views.glava),
    path('kyrgyzstan/dom-i-sad/', views.dom_i_sad),
]
