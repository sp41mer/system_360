from django.conf.urls import url

from core.views import Main360System

urlpatterns = [
    url(r'test/(?P<pk>\d+)$', Main360System.as_view(), name="test"),

    # url(r'teacher/add/$', TeacherCreateView.as_view(), name="add_teacher"),
    # url(r'teacher/(?P<pk>\d+)/update/$', TeacherUpdateView.as_view(), name="update_teacher"),
    #
    # url(r'student/(?P<group>\d+)/all/$', StudentListView.as_view(), name="all_students"),
    # url(r'student/add/$', StudentCreateView.as_view(), name="add_student"),
    # url(r'student/(?P<pk>\d+)/update/$', StudentUpdateView.as_view(), name="update_student"),
    #
    # url(r'subject/(?P<type>\d+)/all/$', SubjectListView.as_view(), name="all_subjects"),
    # url(r'subject/add/$', SubjectCreateView.as_view(), name="add_subject"),
    # url(r'subject/(?P<pk>\d+)/update/$', SubjectUpdateView.as_view(), name="update_subject"),
    #
    # url(r'group/all/$', GroupListView.as_view(), name="all_groups"),
]