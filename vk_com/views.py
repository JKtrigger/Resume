from django.http import HttpResponseRedirect
from django.views.generic import TemplateView


class VkComView(TemplateView):
    title = 'friends'
    template_name = "vk_com/vk_com.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bottom_left_link'] = '/vk_api_friends/'
        context['bottom_left_title'] = 'Регистрация во Вконтакте'
        context['bottom_left_text'] = 'вы прямо здесь'

        context['bottom_middle_link'] = ''
        context['bottom_middle_title'] = 'Уроки'
        context['bottom_middle_text'] = 'pending...'

        context['bottom_right_link'] = ''
        context['bottom_right_title'] = 'Обратная связь'
        context['bottom_right_text'] = 'pending...'
        context['logout_link'] = 'forgot_me'
        context['logout_text'] = 'забыть меня'

        return context

    def post(self, request, *args, **kwargs):
        request.session['user_vk'] = (
                request.session.get('user_vk', None) or
                request.POST.get('user_vk', None)
        )
        request.session['password'] = (
                request.session.get('password', None) or
                request.POST.get('password', None)
        )
        return super(VkComView, self).get(self, request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        request.session['user_vk'] = (
                request.session.get('user_vk', None) or
                request.POST.get('user_vk', None)
        )
        if not request.session['user_vk']:
            return HttpResponseRedirect('/vk_api_friends/login')
        return super(VkComView, self).get(self, request, *args, **kwargs)


class LoginVK(TemplateView):
    template_name = "vk_com/login.html"


def forgot_me(request):
    """  Обрботка запросса на удаление уч., данных из словаря сессии """
    if "user_vk" in request.session:
        request.session.pop("user_vk")
    if "password" in request.session:
        request.session.pop("password")
    return HttpResponseRedirect('/vk_api_friends/login')
