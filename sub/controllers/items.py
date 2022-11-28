from cement import Controller, ex
from ..PomoBot.src.boot import start
from ..PomoBot import main as boot
from ..PomoBot.src.Configs import configs as cfg
import nextcord
import multiprocessing
import threading
import time
import asyncio
import os, sys


class Items(Controller):
    class Meta:
        label = 'items'
        stacked_type = 'embedded'
        stacked_on = 'base'
    token = os.environ['TOKEN']
    thrd = None
    data = None

    @ex(help='start')
    def start(self):
        #Must improve this
        os.system("pm2 start sub/PomoBot/main.py --name bot --interpreter python")
        pass

    @ex(help="show total guilds")
    def tot(self):
        print(self.data)
        pass

    @ex(help="kill thread")
    def kill(self):
        os.system("pm2 kill")
        pass
        
    @ex(help="go")    
    def kick(self):
        boot.main()
        return