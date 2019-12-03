
from django.urls import path
from .views import CoursesListView, CoursesDetailView, LessonView

urlpatterns = [
    path('', CoursesListView.as_view(), name='courses'),
    path('<int:pk>', CoursesDetailView.as_view(), name='course_detail'),
    path('lesson/<int:pk>', LessonView.as_view(), name = 'lesson'),
    #path('enrollment', EnrollmentOnCourseView.as_view(), name='enrollment'),

]