from django.http import HttpResponseRedirect
from django.views.generic import TemplateView


class VkComView(TemplateView):
    title = 'friends'
    template_name = "vk_com/vk_com.html"

    def get(self, request, *args, **kwargs):
        request.session['user_vk'] = request.session.get('user_vk') or \
                                     request.GET.get('user_vk', 'FF')
        return super(VkComView, self).get(self, request, *args, **kwargs)


class LoginVK(TemplateView):
    template_name = "vk_com/login.html"
