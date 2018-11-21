

def messages(request):
    return {
        'user_vk': request.session.get('user_vk', '***'),
        'leave': False
    }

