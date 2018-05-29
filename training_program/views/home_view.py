from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from edc_base.view_mixins import EdcBaseViewMixin
from edc_dashboard.view_mixins.app_config_view_mixin import AppConfigViewMixin


class HomeView(EdcBaseViewMixin, AppConfigViewMixin, TemplateView):

    app_config_name = 'training_program'
    template_name = 'training_program/home.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            navbar_item_selected='home',
            ANONYMOUS_ENABLED=settings.ANONYMOUS_ENABLED)
        return context