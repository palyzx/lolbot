# -*- coding: utf-8 -*-

import random


class Plugin:
    vk = None
    keys = [u'рандом', u'ранд', 'random', 'rand', 'dice', 'кубик']

    def __init__(self, vk):
        self.vk = vk
        print('Рандом')

    def call(self, msg):
        args = msg['body'].split()
        num = 0
        try:
            if len(args) > 2 and len(args) < 4:
                if args[2] < 0:
                    num = random.randint(int(args[2]), 0)
                else:
                    num = random.randint(0, int(args[2]))
            elif len(args) > 3:
                if int(args[2]) < int(args[3]):
                    num = random.randint(int(args[2]), int(args[3]))
                else:
                    num = random.randint(int(args[3]), int(args[2]))
            else:
                num = random.randint(1, 6)

            self.vk.respond(msg, {'message': str(num)})
        except:
            print('Опять ничисла пихаит :C')
            return