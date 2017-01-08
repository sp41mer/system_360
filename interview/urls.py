from django.conf.urls import url

from interview.view import EstimateUserListView

urlpatterns = [
    url(r'estimate_list/$', EstimateUserListView.as_view(), name="estimate_list"),
]