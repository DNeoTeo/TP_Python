from discord.ext import commands 
import discord
import requests
import socket
from PyQt5.Qt import QUrl, QDesktopServices
import webbrowser
from DBot import MyCmdBot
import logging

class Messages(commands.Cog):
    def __init__(self, bot :MyCmdBot) -> None:
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        self.bot.log.loginfo(f"{self.bot.user} has connected to Discord! cmd_pref = {self.bot.command_prefix}")

    @commands.Cog.listener()
    async def on_member_join(self, member : discord.Member):
        note_bot_channel = self.bot.get_channel(964418174265225297)
        await note_bot_channel.send(content=f"Bienvenue {member.display_name} dans mon serveur de note personnel !")
        self.bot.log.logwarn(f"{member.display_name} à rejoint le serveur avec ces {member.roles}")
        

    @commands.Cog.listener()
    async def on_message(self, message : discord.Message):
        if message.author == self.bot.user:
            self.bot.log.logdebug(f"Messages in {message.channel.name} of {message.author.display_name} : {message.content}")
            return
        else :
            self.bot.log.loginfo(f"Messages in {message.channel.name} of {message.author} : {message.content}")
        if(message.content.startswith(self.bot.command_prefix+'REC') and len(message.content.split())>=5): #1 = test si on a tous les arguments de la commande
            resultserv = self.bot.__query(message.content.split()[1], message.content.split()[2], message.content.split()[3], message.content.split()[4]) #("localhost:8000", "Yo8mHbm1zZXT5dFNqbSAwaoGBFbXcCMs", "149.62.158.51", "None")
            print(str(resultserv["IP"]) + " | " +
            str(resultserv["Organization"]) + " | "+
            str(resultserv["Country"]) + " | "+
            str(resultserv["Latitude"]) + " | "+
            str(resultserv["Longitude"]))
            url = "https://www.openstreetmap.org/?mlat=%s&mlon=%s#map=12" % (resultserv["Latitude"],resultserv["Longitude"])
            webbrowser.open(url)

    def __query(self, hostname, api_key, ip_loc, dns_loc):
        if(dns_loc != "None" and ip_loc == "None"):
            ip_loc = socket.gethostbyname(dns_loc)
        url = "http://%s/ip/%s?key=%s" % (hostname,ip_loc,api_key)
        print(url)
        r = requests.get(url)
        if r.status_code == requests.codes.NOT_FOUND:
            print("Error", "IP not found")
            return
        elif r.status_code == requests.codes.OK:
            return r.json()

    @commands.command(name="ping", pass_context=True)
    async def cmd_ping(self, ctx):
        await ctx.send("PONG")

    @commands.command(name="hello", pass_context=True)
    async def cmd_hello(self, ctx):        
        await ctx.send('Hello World!')
                
    @commands.command(name="del", pass_context=True)
    async def cmd_del(self, ctx):
        if(len(ctx.message.content.split()) > 1):
            number = int(ctx.message.content.split()[1])
        else :
            number = 1
        current_messages = await ctx.message.channel.history(limit=number+1).flatten()
        msg_del = ""
        for msg in current_messages:
            msg_del += msg.content+" | "
            await msg.delete()
        self.bot.log.logwarn(f"Suppression de {number} messages : {msg_del}")

def setup(bot):
    bot.add_cog(Messages(bot))



    