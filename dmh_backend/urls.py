from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from questions import views as questions_views
from answers import views as answers_views

router = routers.DefaultRouter()
router.register('questions', questions_views.QuestionViewSet)
router.register('answers', answers_views.AnswerViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]