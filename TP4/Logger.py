from discord.ext import commands
import discord
import logging

from DBot import MyCmdBot


class Logs (logging.Logger):
    def __init__(self, bot : MyCmdBot, level: int) -> None:
        super().__init__(bot.user, level)

    def addHandlerConsole(bot :commands.Bot, level :int, format :str):
        handler_c = logging.StreamHandler()
        handler_c.setLevel(level)
        handler_c.setFormatter(logging.Formatter(format))
        bot.log.addHandler(handler_c)
        
    def addHandlerFile(bot :commands.Bot, filename :str, level :int, format :str):
        handler_f = logging.FileHandler(filename=filename, encoding='utf-8', mode='a')
        handler_f.setLevel(level)
        handler_f.setFormatter(logging.Formatter(format))
        bot.log.addHandler(handler_f)
        
    def logdebug(self, msg):
        logging.debug(msg)

    def loginfo(self, msg):
        logging.info(msg)

    def logwarn(self, msg):
        logging.warn(msg)
    
    def logerror(self, msg):
        logging.error(msg)
