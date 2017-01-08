from django.views.generic import ListView
from core.mixins import AccessMixin
from core.models import User


class EstimateUserListView(ListView, AccessMixin):
    model = User

    def get_context_data(self, **kwargs):
        context = super(EstimateUserListView, self).get_context_data()
        user_ids_to_exclude = self.eval_user.already_estimated_users.all().values_list('id', flat=True)
        context['object_list'] = self.eval_user.estimated_users.exclude(id__in=user_ids_to_exclude)
        return context
