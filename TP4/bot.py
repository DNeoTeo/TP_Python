import discord
import os
from discord.ext import commands
from DBot import MyCmdBot
import json
from argparse import ArgumentParser
import logging

def parse_args():
    parser = ArgumentParser()
    parser.add_argument("-c", "--config", help="Config file", required=True, dest="config")
    return parser.parse_args()

def getconfig(conf_file):
    with open(conf_file) as fconf :
        return json.load(fconf)

args = parse_args()
print(args)
config = getconfig(args.config)
default_intents = discord.Intents.default()
default_intents.members = True
bot_tp_py = MyCmdBot(config, command_prefix="!", intents=default_intents) #commands.Bot(command_prefix="!", intents=default_intents)


@bot_tp_py.command()
async def load(ctx, extension):
    bot_tp_py.load_extension(f'cogs.{extension}')

@bot_tp_py.command()
async def reload(ctx):
    print("loading...")
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            bot_tp_py.unload_extension(f'cogs.{filename[:-3]}')
            bot_tp_py.load_extension(f'cogs.{filename[:-3]}')

@bot_tp_py.command()
async def unload(ctx, extension):
    bot_tp_py.unload_extension(f'cogs.{extension}')


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot_tp_py.load_extension(f'cogs.{filename[:-3]}')

bot_tp_py.log = logging.getLogger(str(bot_tp_py.user))
bot_tp_py.log.setLevel(logging.DEBUG)
bot_tp_py.addHandlerConsole(bot_tp_py.log, int(config[0]["level"]), config[0]["formatter"] )
bot_tp_py.addHandlerFile(bot_tp_py.log, config[0]["bot_log"], int(config[0]["level"]), config[0]["formatter"] )
bot_tp_py.run(config[0]["TOKEN"])


#!REC localhost:8000 Yo8mHbm1zZXT5dFNqbSAwaoGBFbXcCMs 149.62.158.51 None