from django.urls import path
from home import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name="home"),
    path("login", views.userLogin, name="user_login"),
    path("register", views.userRegister, name="user_register"),
    path("logout", views.logoutUser, name="logout_user"),
    path("todo_list", views.todoList, name="todo_list"),
    path("update/<int:id>", views.updateList, name="update_list"),
    path("delete/<int:id>", views.deleteList, name="delete_list"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
