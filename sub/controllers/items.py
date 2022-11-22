from cement import Controller, ex
from PomoBot import main as start_
from PomoBot.src.Configs import configs as cfg
from multiprocessing import Process
import asyncio
import os


class Items(Controller):
    class Meta:
        label = 'items'
        stacked_type = 'embedded'
        stacked_on = 'base'
    token = os.environ['TOKEN']
    client_ = cfg.client
    
    @ex(help='start')
    def start(self):
        start_.main()
        pass

    @ex(help="show total guilds")
    def tot(self):
        loop = asyncio.get_event_loop()
        print(cfg.client.guilds)
        pass
        