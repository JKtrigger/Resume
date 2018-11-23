from django.shortcuts import render
from django.views.generic import TemplateView


class AboutMeView(TemplateView):
    template_name = "title_page/title_page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Добавление текста в контекст

        context['bottom_left_link'] = '/vk_api_friends/'
        context['bottom_left_title'] = 'Идеи'
        context['bottom_left_text'] = 'Идеи проектов со ссылкой'

        context['bottom_middle_link'] = ''
        context['bottom_middle_title'] = 'Уроки'
        context['bottom_middle_text'] = 'История разработки Идей'

        context['bottom_right_link'] = ''
        context['bottom_right_title'] = 'Обратная связь'
        context['bottom_right_text'] = 'Способы связаться, социальные сети'

        return context


class AboutProject(AboutMeView):
    template_name = "about_project/about_project.html"


def handler404(request, exception):
    return render(request, 'bad_http_code/404.html', status=404)
