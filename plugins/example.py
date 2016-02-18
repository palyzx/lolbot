# -*- coding: utf-8 -*-


class Plugin:
    vk = None
    keys = [u'примерплагина', u'тестовыйплагин']

    def __init__(self, vk):
        self.vk = vk
        print('Пример плагина')

    def call(self, msg):
        self.vk.respond(msg, {'message': u'Пример плагина'})