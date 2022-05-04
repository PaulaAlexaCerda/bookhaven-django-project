from django.urls import path
from .views import login_view 

app_name = "identity"
urlpatterns = [
    path('custom-login/', login_view, name="custom-login"),
    
]
