import random
from machine.plugins.base import MachineBasePlugin
from machine.plugins.decorators import listen_to


class AgreePlugin(MachineBasePlugin):
    @listen_to(regex=r'어때요?|괜찮(.)요?')
    def agree(self, msg):
        candidates = [
            'ㅇㅇ',
            '조습니다',
            'ㅇㅇ 조습니다',
            '헐 ㅇㅇ',
            '너무 좋다',
            '1)왜 그런지랑 2)뭐가 좋은지, 알려주시면 판단하기 좋을 것 같아요'
        ]

        response = random.choice(candidates)
        msg.say(response, as_user=True)
