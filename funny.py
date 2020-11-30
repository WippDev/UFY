import discord
from discord.ext import commands
import asyncio
import aiohttp
from datetime import datetime, timedelta
from random import choice
import random
import datetime
import re


color = 0xabffcf
numbers = ("1️⃣", "2⃣", "3⃣", "4⃣", "5⃣",
		   "6⃣", "7⃣", "8⃣", "9⃣", "🔟")

from data import Data



class Fun(commands.Cog):
    @commands.command()
    async def test1(self , ctx):
        em = discord.Embed(color = color)
        em.add_field(name = "Cog tested - OK- Funny" , value = "made by $wip")
        await ctx.send(embed = em)

    def __init__(self, client , theme_color):
        self.client = client
        self.polls = []
        self.theme_color = theme_color


    @commands.command()
    async def ping(self, ctx):
            await ctx.send(f'Pong! Ping: {round(self.client.latency * 1000)}ms')
    
  
    #added by me 
    @commands.command()
    async def gay(self ,ctx, *, member: discord.Member = None):
      member = member if member else ctx.author
      embed = discord.Embed(title="Gay machine", description=f"You are {random.randint(1,100)}% gay :rainbow:", color=color)
      embed.set_author(name=member.display_name, icon_url=member.avatar_url)
      embed.set_footer(text=f"Requests by {member}", icon_url=member.avatar_url)
      await ctx.send(embed=embed)

    @commands.command(aliases=["av"])
    async def avatar(self, ctx, member: discord.Member = None):
      if not member:  
        member = ctx.message.author  # set member as the author
      embed = discord.Embed(colour=color )
                
      embed.set_image(url=member.avatar_url)

      await ctx.send(embed=embed)

    @commands.command()
    async def afk(self, ctx, *, reason=None):
        embed = discord.Embed(color=self.theme_color)

        if str(ctx.guild.id) not in Data.server_data:
            Data.server_data[str(ctx.guild.id)] = Data.create_new_data()

        data = Data.server_data[str(ctx.guild.id)]

        # Error messages
        if reason is None:
            embed.add_field(name='Warning', value='Please specify a reason.')

        for afk_user_entry in data["afks"]:
            afk_user_id = str(afk_user_entry["user"])

            if str(ctx.author.id) == afk_user_id:
                embed.add_field(name='Warning', value='You are already AFK.')
                break

        if len(embed.fields) == 0:
            afk_entry = {
                "user": str(ctx.author.id),
                "reason": reason
            }

            Data.server_data[str(ctx.guild.id)]["afks"].append(afk_entry)
            await ctx.send(f"**{ctx.author}** is now AFK because **{reason}**")
            return

        await ctx.send(embed=embed)



def setup(client):
    client.add_cog(Fun(client))
    print("Mod cog is loading")