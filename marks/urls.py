from django.conf.urls import url
from marks.views import WeightCreateView, ProfessionalismMarkCreateView, ControlMarkCreateView, \
    CommunicationMarkCreateView, ClientOrientationMarkCreateView, EfficiencyMarkCreateView, EvolutionMarkCreateView, \
    LeadershipMarkCreateView, TeamworkMarkCreateView

urlpatterns = [
    url(r'weight/add/$', WeightCreateView.as_view(), name="add_weight"),
    url(r'professionalism/add/$', ProfessionalismMarkCreateView.as_view(), name="add_professionalism_mark"),
    url(r'control/add/$', ControlMarkCreateView.as_view(), name="add_control_mark"),
    url(r'communication/add/$', CommunicationMarkCreateView.as_view(), name="add_communication_mark"),
    url(r'client_orientation/add/$', ClientOrientationMarkCreateView.as_view(), name="add_client_orientation_mark"),
    url(r'efficiency/add/$', EfficiencyMarkCreateView.as_view(), name="add_efficiency_mark"),
    url(r'evolution/add/$', EvolutionMarkCreateView.as_view(), name="add_evolution_mark"),
    url(r'leadership/add/$', LeadershipMarkCreateView.as_view(), name="add_leadership_mark"),
    url(r'teamwork/add/$', TeamworkMarkCreateView.as_view(), name="add_teamwork_mark"),

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