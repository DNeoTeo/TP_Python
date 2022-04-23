from Logger import Logs
import discord
from discord import logging
from discord.ext import commands

class MyCmdBot(commands.Bot):
    log : Logs
    config :list
    def __init__(self, conf,*, loop=None, **options):
        self.config = conf
        super().__init__(loop=loop, **options)

    def addHandlerConsole(self, logger :logging.Logger, level :int, format :str):
        handler_c = logging.StreamHandler()
        handler_c.setLevel(level)
        handler_c.setFormatter(logging.Formatter(format))
        logger.addHandler(handler_c)
        
    def addHandlerFile(self, logger :logging.Logger, filename :str, level :int, format :str):
        handler_f = logging.FileHandler(filename=filename, encoding='utf-8', mode='a')
        handler_f.setLevel(level)
        handler_f.setFormatter(logging.Formatter(format))
        logger.addHandler(handler_f)

    #def send_bot_help():


