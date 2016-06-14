# -*- coding: utf-8 -*-
# Класс с некоторыми доп. методами 

import vk_api


class VkPlus:
    api = None

    def __init__(self, login, password, app_id=-1):
        try:
            if app_id == -1:
                self.api = vk_api.VkApi(login, password)  
            else:
                self.api = vk_api.VkApi(login, password, app_id)  

            self.api.authorization() # Авторизируемся
        except vk_api.AuthorizationError as error_msg:
            print(error_msg)
            return None

    # values передаются все, кроме user_id/chat_id
    # Поэтому метод и называется respond, ваш кэп
    # Сделано для упрощения ответа. В пагине или другом коде 
    # не нужно "думать" о том, откуда пришло сообщение:
    # из диалога, или из беседы (чата, конференции).
    def method(self, key, data=None):

        for attempt in range(10):
            if attempt > 0:
                print (u'Attepts $'+str(attempt))

            try:
                return self.api.method(key, data)      # тут может быть проблема с тем, что data = None. Тогда if'ом разделить.
                                            # но тут .api.method ! =)
            except ConnectionError as e:
                if e.errno != errno.ECONNRESET:
                    print(u'Exeption at vkservice at attempt '+str(attempt)+u' :')
                    print(e)
                    break
                print(u'104 Connection reset by peer. Attempt: '+str(attempt))                    
            else:
                break
        else:
            print(u'Exeption at vkservice (last): ')
            print(e)
            socket.send(b'error')
            self.exit = True 

    def respond(self, to, values):
        if 'chat_id' in to:
            values['chat_id'] = to['chat_id']
        else:
            values['user_id'] = to['user_id']

        self.method('messages.send', values) # теперь вместо self.api.method() используем self.method() . Соотвественно везде где было .api.method()
                                            # меняем на .method()

        

    def markasread(self, id):
        values = {
            'message_ids': id
        }
        self.method('messages.markAsRead', values)
