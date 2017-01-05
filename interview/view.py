from django.views.generic import ListView
from core.mixins import AccessMixin
from core.models import User


class EstimateUserListView(ListView, AccessMixin):
    model = User

    def get_context_data(self, **kwargs):
        context = super(EstimateUserListView, self).get_context_data()
        context['object_list'] = self.eval_user.estimated_users.all()
        return context
