import random
import vk_api


def messages(request):
    user_vk = request.session.get('user_vk', None)
    password = request.session.get('password', None)
    friends = {}
    if user_vk and password:
        vk_session = vk_api.VkApi(
            user_vk,
            password,
        )
        try:
            vk_session.auth(reauth=True)
        except vk_api.AuthError as error_msg:
            return {
                'user_vk': user_vk,
                'password': password,
                'friends':
                    [
                        {
                            'first_name':
                                'Похоже, что имя и пароль не правильные. '
                        },
                    ]
                }

        with vk_api.VkRequestsPool(vk_session) as pool:
            friends = pool.method(
                'friends.get',
                {
                    'fields': 'photo_200_orig, nickname, ',
                },

            )
        friends = friends.result['items']
        random.shuffle(friends)
        friends = friends[:5]

    return {
        'user_vk': user_vk,
        'password': password,
        'friends': friends
    }

