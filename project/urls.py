
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from study import views

router = routers.DefaultRouter()
router.register('courses',views.CoursesViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/', include(router.urls)),

    path('api/student/', views.StudentCreateListView.as_view()),
    path('api/student/<int:pk>/', views.StudentRetrieveUpdateDestroyAPIView.as_view()),
    path('api/mentor/', views.MentorListCreateAPIView.as_view()),
    path('api/mentor/<int:pk>/', views.MentorRetrieveUpdateDestroyAPIView.as_view()),
]
