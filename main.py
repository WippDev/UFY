import discord
from discord.ext import commands
import json
import os
import random
import datetime
import asyncio 
from asyncio import sleep
import logging
import DiscordUtils
from discord.ext.commands import BucketType
from webserver import keep_alive 
from automod import AutoMod
from data import Data
from mod import Moderator
from serversettings import ServerSettings
from funny import Fun
THEME_COLOR = 0x919eff
from helpers import update_presence
from replit import db


x = ["https://", 'discord.gg']



prefix = '!'
client = commands.Bot(command_prefix = prefix , intents = discord.Intents.all())
client.author_id = 586531356272754709
client.add_cog(AutoMod(client, THEME_COLOR))

client.add_cog(Moderator(client, THEME_COLOR))

client.add_cog(ServerSettings(client, THEME_COLOR))

client.add_cog(Fun(client, THEME_COLOR))





mainshop = [{"name":"Watch","price":100,"description":"it shows the curent time"},
            {"name":"Laptop","price":1000,"description":"Work and earn "},
            {"name":"PC","price":10000,"description":"it geves you many every 160 seconds 3 times"}]





client.remove_command('help')

cogs = ["Music"]
theme_color = 0x919eff



async def status():
  while True:
    await client.wait_until_ready()
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f'{len(client.guilds)} Servers! ✅'))
    await sleep(40)
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f'my prefix {prefix}'))
    await sleep(15)
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"fire👀{len(client.commands)} commands"))
    await sleep(15)








@client.event
async def on_ready():
    
    print(f'{client.user} the bot is ready!')
    print("loading.... Cogs")

    if __name__ == "__main__":
      for cog in cogs:

        try:
          client.load_extension(cog)
          print(cog + "was loaded")
      
        except Exception as e:
          print(e)
    client.loop.create_task(Data.auto_update_data())
    client.loop.create_task(status())
    



@client.command()
async def help(ctx):
    embed = discord.Embed(color=0x85e0ff).add_field( name="<a:8411_WumpusHypesquad:781913762214576128> HELP IS HERE 📜", value="Page 1 | AUTO MOD" , )
    embed.add_field(name = "activateautomod" , value = f"`{prefix}activateautomod` , it activates automod in your server it `will nlock links `" , inline = False)
    embed.add_field(name = "stopautomod" , value = f"`{prefix}stopautomod` , will stop  automod in your server it ")
    embed.add_field(name = "payrespect" , value = f"`{prefix}enablerespects` , if you send `f` it will pay respect ")
    embed.add_field(name = "disablerespects" , value = f"`{prefix}disablerespects` , will turn payrespect off ")



    embed1 = discord.Embed(color=0x85e0ff).add_field( name="<a:8411_WumpusHypesquad:781913762214576128> Economy ", value="Page 2 | <:coin:782917209055035424> Economy" ,)
    embed1.add_field(name = 'ballance' , value = f'`{prefix}bal` , will show the curent ballance ' , inline = False)
    embed1.add_field(name = 'beg' , value = f'`{prefix}beg` , will give you some coins random you can win up to 100$')
    embed1.add_field(name = 'send' , value = f'`{prefix}send` + add a member , will give the member you tag coins ')
    embed1.add_field(name = 'bet' , value = f'`{prefix}bet` ,add a sume and will give you money  ')
    embed1.add_field(name = 'shop' , value = f'`{prefix}shop` ,will show the shop and all the items that you can buy and soon use ')
    embed1.add_field(name = 'buy' , value = f'`{prefix}buy` ,an item in the shop that is displayed  ')
    embed1.add_field(name = 'deposit' , value = f'`{prefix}deposit` ,+ add amount |will send the money in bank where people can;t stole ')
    embed1.add_field(name = 'withdraw' , value = f'`{prefix}withdraw` ,+ add amountwill take the money from bank and add them to the wallet  ')
    embed1.add_field(name = 'search' , value = f'`{prefix}search` ,searches for an item  ')
    embed1.add_field(name = 'hack' , value = f'`{prefix}hack` ,mention a user and will hack his account !  ')
    embed1.add_field(name = 'rob' , value = f'`{prefix}rob` ,robs someone you mention we don t recommand to mention admins! ')
    embed1.add_field(name = 'use' , value = f'`{prefix}use` ,and add a item if you have you can check doing `{prefix}bag`  ')

    embed2 = discord.Embed(color=0x85e0ff).add_field(name=" MODERATION | UTILITY ", value="Page 3 | moderation")
    embed2.add_field(name = "Kick" , value = f"`{prefix}kick` > *tag member and a reason if you want" , inline = False)
    embed2.add_field(name = "clear" , value = f"`{prefix}clear` > add the amoun of messages you want to clear !")
    embed2.add_field(name = "lockchannel" , value = f"`{prefix}lockchannel` > will lock the channel  !")
    embed2.add_field(name = "unlockchannel" , value = f"`{prefix}unlockchannel` > will unlock the channel  !")
    embed2.add_field(name = "embed" , value = f"`{prefix}embed` > add title and description  !")
    embed2.add_field(name = "reminder" , value = f"`{prefix}set_reminde` , will set a reminder based on the time you add [must have dms open]", inline = False)
 
    paginator = DiscordUtils.Pagination.CustomEmbedPaginator(ctx)
    embed3 = discord.Embed(color=0x85e0ff).add_field(name="MUSIC | FUN", value="Page 4")
    embed3.add_field(name = "play music" , value = f"`{prefix}play` , you need to be in a vocal chat", inline = False)
    embed3.add_field(name = "pause music" , value = f"`{prefix}pause` , you need to be in a vocal chat", inline = False)
    embed3.add_field(name = "stop music" , value = f"`{prefix}stop` , you need to be in a vocal chat", inline = False)
    embed3.add_field(name = "leave/disconect music" , value = f"`{prefix}disconnect` , you need to be in a vocal chat", inline = False)
    embed3.add_field(name = "quale music" , value = f"`{prefix}quale` , you need to be in a vocal chat", inline = False)
    embed3.add_field(name = "`yes` , `ufy` , `ok`, `no`" , value =f"`{prefix}yes` or ufy")
    paginator.add_reaction('⏪', "first")
    paginator.add_reaction('◀️', "back")
    paginator.add_reaction('❌', "delete")
    paginator.add_reaction('▶️', "next")
    paginator.add_reaction('⏩', "last")
    embeds = [embed ,embed1, embed2, embed3]
    await paginator.run(embeds)


@client.command(aliases=["b2c4"])
async def bal(ctx ,  member: discord.Member = None):
    if not member:  
        member = ctx.message.author


    await open_account(ctx.author)
    await open_account(member)

    user = member

    users = await get_bank_data()

    wallet_amt = users[str(user.id)]["wallet"]
    bank_amt = users[str(user.id)]["bank"]

    em = discord.Embed(title = f"{member}'s ballance" , color = 0x85e0ff )
    em.add_field(name = "Wallet ballance" , value =f"{wallet_amt} <:coin:782917209055035424> | ")
    em.add_field(name = "Bank ballance" , value =f"{bank_amt} <:coin:782917209055035424> |" )
    await ctx.send(embed = em)







#=====================S E A R C H || B O A R D =======================



@client.command(aliases = ['scout'])
@commands.cooldown(1, 45, BucketType.user)
async def look(ctx):
    await open_account(ctx.author)

    place_list = ["couch", "jacket", "underwear", "school", "air", "pocket", "face", "toilet","computer","attic","little kid","dog","car", 'videogame', 'flower', 'XD'  , 'pool']
    first_place = random.choice(place_list)
    place_list.remove(first_place)
    second_place =  random.choice(place_list)
    place_list.remove(second_place)
    third_place =  random.choice(place_list)
    await open_account(ctx.author)
    users = await get_bank_data()
    user = ctx.author
    
    await ctx.send(f"Where do you want to search:\n``{first_place}``, ``{second_place}``, or  ``{third_place}``?")
    def check(msg):  
        return msg.author == ctx.author and msg.channel.id == ctx.channel.id 

    try:
        msg = await client.wait_for('message', check = check, timeout = 12)
    except asyncio.TimeoutError:
        await ctx.send(f"You didnt pick a place! get rekt kid")
        return
    
    if msg.content.lower() in [first_place, second_place, third_place]:
        searched_money = random.randrange(5, 15)
    
        await ctx.send(f"You found {searched_money} <:coin:782917209055035424>  coins from ``{msg.content.lower()}``!")
                      
        users[str(user.id)]["wallet"] += searched_money
        with open("bank.json", "w") as f: 
            json.dump(users, f)
    
    else:
        await ctx.send(f"What are you THINKING man do you think {msg.content} is in the list??")

@look.error
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(f"You just search please wait {error.retry_after:.0f} seconds to search again")
#=====================L E A D || B O A R D =======================

@client.command(aliases = ['wrk'])
@commands.cooldown(1, 45, BucketType.user)
async def work(ctx):
  place_list = ['home'  , 'hacking' , 'Market', 'IT', 'Discord']
  first_place = random.choice(place_list)
  place_list.remove(first_place)
  second_place =  random.choice(place_list)
  place_list.remove(second_place)
  third_place =  random.choice(place_list)
  await open_account(ctx.author)
  users = await get_bank_data()
  user = ctx.author
  await ctx.send(f"Where do you want to work:\n``{first_place}``, ``{second_place}``, or  ``{third_place}``?")
  def check(msg):  
        return msg.author == ctx.author and msg.channel.id == ctx.channel.id 

  try:
        msg = await client.wait_for('message', check = check, timeout = 12)
  except asyncio.TimeoutError:
        await ctx.send(f"You didnt pick a place! get rekt kid")
        return
  if msg.content.lower() in [first_place]:
    await ctx.send("<:coin:782917209055035424> test aproved!!!")
  if msg.content.lower() in [second_place]:
    await ctx.send("<:coin:782917209055035424> test aproved - 2!!!")

  if msg.content.lower() in [third_place]:
      await ctx.send("<:coin:782917209055035424> test aproved - 3!!!")



  if msg not in first_place or second_place or third_place:
      await ctx.send("that was not in the list idiot")
  









@client.command(aliases = ["b"])
async def top(ctx,x = 10):
    users = await get_bank_data()
    top = {}
    total = []
    for user in users:

      name = int(user)
        

      total_amount = users[user]["wallet"] + users[user]["bank"]
      top[total_amount] = name
      total.append(total_amount)

    total = sorted(total,reverse=True)    
    
    em = discord.Embed(title = f"Top {x} Richest People" , description = "This is decided on the basis of raw money in the bank and wallet",color = 0x85e0ff)
    index = 1
    for amt in total:
        id_ = top[amt]
        member = client.get_user(id_)
        lol = member
        em.add_field(name = f"{index}. {lol}" , value = f"{amt} <:coin:782917209055035424> ",  inline = False)
        if index == x:
            break
        else:
            index += 1

    await ctx.send(embed = em)




#=====================L E A D || B O A R D =======================

# error handeling 
   #⛔️ error ⛔️ ======================================
@client.event
async def on_command_error(ctx , error):
    member = ctx.author.mention
    if isinstance(error, commands.CommandNotFound):
        em = discord.Embed(color = 0xffb361   , title = "> command not found  !")
        await ctx.send(embed = em)
        raise error 
    if isinstance(error,commands.MissingPermissions):
      em=discord.Embed(color = 0xffb361)
      em.set_author(name=f"Hey! {ctx.author.name}, You are not allowed to use this command ⛔️")
      await ctx.send(embed=em)
      await ctx.message.delete()
    elif isinstance(error,commands.MissingRequiredArgument):
      em=discord.Embed(color =0xffb361)
      em.set_author(name=f"Hey! {ctx.author.name}, You  need to enter all the required args.✅")
      await ctx.send(embed=em)
      await ctx.message.delete()
    else:
      raise error



#================================== I N V I T E || B O T ==========================

#invite bot
@client.command()
async def invite(ctx):
      embed = discord.Embed(title="UFY Support!",color = 0x85e0ff)
      embed.add_field(name="bot invite",value=f"[INVITE!](https://discord.com/api/oauth2/authorize?client_id=779001880339677194&permissions=8&scope=bot)")
      embed.set_author(name="Thanks for using Rogo!")
      embed.timestamp = datetime.datetime.now(datetime.timezone.utc)
      embed.set_author(icon_url = client.user.avatar_url, name = 'UFY' )
      await ctx.channel.send(embed=embed)      








#================================== I N V I T E || B O T ==========================





#==================================G I V E || A D M I N =========================
@client.command(pass_context=True)
async def vip(ctx , amount):
    if ctx.message.author.id == 586531356272754709:
  
        
      await open_account(ctx.author)


      users = await get_bank_data()
      user = ctx.author



      earnings = amount
      earnings = int(earnings)

      await ctx.send(f"> you give yourself  {earnings}<:coin:782917209055035424>  with succes !!")



      users[str(user.id)]["wallet"] += earnings

      with open("bank.json" , "w") as f:
          json.dump(users,f)


    else :
      await ctx.send("> This command can be used only by the bot owner !")
      return 











#==================================B A G  || C O M M A N D =========================
@client.command(name = "beg")
@commands.cooldown(1, 10, BucketType.user)
async def beg(ctx):
    member = ctx.author
    await open_account(ctx.author)


    users = await get_bank_data()
    user = ctx.author



    earnings = random.randrange(10)

    
    await ctx.send(f"{member.mention}you got {earnings} <:coin:782917209055035424> ")
     
    users[str(user.id)]["wallet"] += earnings

    with open("bank.json" , "w") as f:
      json.dump(users,f)
    




   


#custom error =========================================
@beg.error
async def beg_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        em = discord.Embed(color = 0x85e0ff)
        em.add_field(name = 'This command is ratelimited, please try again in {:.2f}s'.format(error.retry_after) , value = "made by $wip")
        await ctx.send(embed = em)
    else:
        raise error

#===================================D E P O S I T ===========================
@client.command()
async def dep(ctx , amount = None):
    await open_account(ctx.author)
    if amount == None:
        user = ctx.author

        users = await update_bank(ctx.author)
        total = users[str(user.id)]["wallet"]
        embed = discord.Embed(title = "Succes")
        embed.add_field(name = "Deposited all!" , value = "> finis")
        await ctx.send(embed = embed)
        await update_bank(ctx.author, -1*total)
        await update_bank(ctx.author, total, 'bank')
        await ctx.send(embed = embed)
        return
    
    bal = await update_bank(ctx.author)
    amount = int(amount)

    if amount>bal[0]:
        embed = discord.Embed(title = "Error")
        embed.add_field(name = "You don't have that much! " , value = "> finish")
        await ctx.send(embed = embed)
        return
    
    if amount<0:
        embed = discord.Embed(title = "Error")
        embed.add_field(name = "Add a positive amount ! " , value = "> finish")
        await ctx.send(embed = embed)
        return

    


    await update_bank(ctx.author, -1*amount)
    await update_bank(ctx.author, amount, 'bank')
    await ctx.send(f"You depsoited with succes {amount} coins")



# W I T H D R A W || XD

@client.command()
@commands.cooldown(1, 5, BucketType.user)
async def withdraw(ctx , amount = None):
    await open_account(ctx.author)
    if amount == None:
        embed = discord.Embed(title = "Error")
        embed.add_field(name = "Plase enter an amont!" , value = "> finis")
        await ctx.send(embed = embed)
        return
    
    bal = await update_bank(ctx.author)
    amount = int(amount)

    if amount>bal[1]:
        embed = discord.Embed(title = "Error")
        embed.add_field(name = "You don't have that much! " , value = "> finish")
        await ctx.send(embed = embed)
        return
    
    if amount<0:
        embed = discord.Embed(title = "Error")
        embed.add_field(name = "Add a positive amount ! " , value = "> finish")
        await ctx.send(embed = embed)
        return
    
    await update_bank(ctx.author , amount )
    await update_bank(ctx.author ,-1* amount , 'bank' )
    await ctx.send(f"You withdrw with succes {amount} coins !!")



    #send command =====================================================

@client.command()
async def send(ctx, member: discord.Member = None , * , amount = None):
    if not member:
        await ctx.send("> Add a real/ member !!")
    await open_account(ctx.author)
    await open_account(member)

    if amount == None:
        embed = discord.Embed(title = "Error")
        embed.add_field(name = "Plase enter an amont!" , value = "> code made by $wip")
        await ctx.send(embed = embed)
        return
    
    bal = await update_bank(ctx.author)
    amount = int(amount)

    if amount>bal[0]:
        embed = discord.Embed(title = "Error")
        embed.add_field(name = "You don't have that much! " , value = "> code made by $wip")
        await ctx.send(embed = embed)
        return
    
    if amount<0:
        embed = discord.Embed(title = "Error")
        embed.add_field(name = "Add a positive amount ! " , value = ">  code made by $wip")
        await ctx.send(embed = embed)
        return
    
    await update_bank(ctx.author, -1*amount , "wallet")
    await update_bank(member , amount, 'wallet')
    await ctx.send(f"You send with  `{amount}`<:coin:782917209055035424> with succes")

#====================================sHOP || SHOP ===============================================

@client.command()
async def shop(ctx):
    
    embed1 = discord.Embed(color=0x85e0ff).add_field( name="<a:8411_WumpusHypesquad:781913762214576128> SHOP 💸", value="Page 1 | Shop 1" , )
    for item in mainshop:
        name = item["name"]
        price = item["price"]
        desc = item["description"]
        embed1.add_field(name = name , value = f"`{price} <:coin:782917209055035424> ` | {desc}" , inline = False)
  
    embed2 = discord.Embed(color=0x85e0ff).add_field(name="Shop 2", value="Page 2 | FUN")
    embed2.add_field(name = "comming soon" , value = "value")
    paginator = DiscordUtils.Pagination.CustomEmbedPaginator(ctx)
    embed3 = discord.Embed(color=0x85e0ff).add_field(name="Shop 3", value="Comming soon")
    paginator.add_reaction('⏪', "first")
    paginator.add_reaction('◀️', "back")
    paginator.add_reaction('❌', "lock")
    paginator.add_reaction('▶️', "next")
    paginator.add_reaction('⏩', "last")
    embeds = [embed1, embed2, embed3]
    await paginator.run(embeds)






#====================================BUY || BUY ===============================================

@client.command()
async def buy(ctx,item,amount = 1):
    await open_account(ctx.author)

    res = await buy_this(ctx.author,item,amount)

    if not res[0]:
        if res[1]==1:
            await ctx.send("That Object isn't there!")
            return
        if res[1]==2:
            await ctx.send(f"You don't have enough money in your wallet to buy {amount} {item}")
            return


    await ctx.send(f"You just bought {amount} {item}")


@client.command()
async def bag(ctx):
    await open_account(ctx.author)
    user = ctx.author
    users = await get_bank_data()

    try:
        bag = users[str(user.id)]["bag"]
    except:
        bag = []


    em = discord.Embed(title = " > Bag" , description = "Here you can see your items and value ")
    for item in bag:
        name = item["item"]
        amount = item["amount"]

        em.add_field(name = name, value = amount)    

    await ctx.send(embed = em)    




    #================================= C O M P L I C A T E D || C O M M A N D =======================
async def buy_this(user,item_name,amount):
    item_name = item_name.lower()
    name_ = None
    for item in mainshop:
        name = item["name"].lower()
        if name == item_name:
            name_ = name
            price = item["price"]
            break

    if name_ == None:
        return [False,1]

    cost = price*amount

    users = await get_bank_data()

    bal = await update_bank(user)

    if bal[0]<cost:
        return [False,2]


    try:
        index = 0
        t = None
        for thing in users[str(user.id)]["bag"]:
            n = thing["item"]
            if n == item_name:
                old_amt = thing["amount"]
                new_amt = old_amt + amount
                users[str(user.id)]["bag"][index]["amount"] = new_amt
                t = 1
                break
            index+=1 
        if t == None:
            obj = {"item":item_name , "amount" : amount}
            users[str(user.id)]["bag"].append(obj)
    except:
        obj = {"item":item_name , "amount" : amount}
        users[str(user.id)]["bag"] = [obj]        

    with open("bank.json","w") as f:
        json.dump(users,f)

    await update_bank(user,cost*-1,"wallet")

    return [True,"Worked"]

#==========================S E L L || I T E M ========================================
@client.command()
async def sell(ctx,item,amount = 1):
    member = ctx.author
    await open_account(ctx.author)

    res = await sell_this(ctx.author,item,amount)

    if not res[0]:
        if res[1]==1:
            await ctx.send("That Object isn't there!")
            return
        if res[1]==2:
            await ctx.send(f"You don't have {amount} {item} in your bag.")
            return
        if res[1]==3:
            await ctx.send(f"{member.mention}You don't have {item} in your bag.")
            return

    await ctx.send(f"{member.mention} You just sold {amount} {item}.")

async def sell_this(user,item_name,amount,price = None):
    item_name = item_name.lower()
    name_ = None
    for item in mainshop:
        name = item["name"].lower()
        if name == item_name:
            name_ = name
            if price==None:
                price = 0.9* item["price"]
            break

    if name_ == None:
        return [False,1]

    cost = price*amount

    users = await get_bank_data()

    bal = await update_bank(user)


    try:
        index = 0
        t = None
        for thing in users[str(user.id)]["bag"]:
            n = thing["item"]
            if n == item_name:
                old_amt = thing["amount"]
                new_amt = old_amt - amount
                if new_amt < 0:
                    return [False,2]
                users[str(user.id)]["bag"][index]["amount"] = new_amt
                t = 1
                break
            index+=1 
        if t == None:
            return [False,3]
    except:
        return [False,3]    

    with open("bank.json","w") as f:
        json.dump(users,f)

    await update_bank(user,cost,"wallet")

    return [True,"Worked"]




#======================================U S E || I T E M ===========================

@client.command(name = "use")
@commands.cooldown(1, 160, BucketType.user)
async def use(ctx,item,amount = 1):
    member = ctx.author
    await open_account(ctx.author)
    users = await get_bank_data()
    user = ctx.author
    bag = users[str(user.id)]["bag"]

    res = await sell_this(ctx.author,item,amount)




    if not res[0]:
        if res[1]==1:
            await ctx.send("That Object isn't there!")
            return
        if res[1]==2:
            await ctx.send(f"You don't have {amount} item in your bag.")
            return
        if res[1]==3:
            await ctx.send(f"{member.mention}You don't have the item  in your bag.")
            return


    if item == 'watch':


      em = discord.Embed(title="Now is ", timestamp = datetime.datetime.utcnow())
      await ctx.send(embed = em)
      users[str(user.id)]['bag'].pop([i['item'] for i in users[str(user.id)]['bag']].index('watch', 0))

    if item == "pc":
      users[str(user.id)]['bag'].pop([i['item'] for i in users[str(user.id)]['bag']].index('pc', 0))
      user = ctx.author
      earnings = random.randrange(2000)

      if earnings < 500:
        em = discord.Embed(color = 0x85e0ff)
        em.add_field(name = "game starts"  , value = "if you can destory the boss you win 20000$")
        await ctx.send(embed = em)
        message = await ctx.send(f"⚔️ - Boss fight start be ready {user.mention}!")
        await asyncio.sleep(3)
        await message.edit(content="🔫 -Fighting the boss !")
        await asyncio.sleep(3)
        await message.edit(content="🧨 -the boss gave you supreme attack")
        await asyncio.sleep(3)
        await message.edit(content="💀 - he killed you ")
        await asyncio.sleep(3)
        return
       
        

      if earnings > 500:
        em = discord.Embed(color = 0x85e0ff)
        em.add_field(name = "game starts"  , value = "if you can destory the boss you win 20000$")
        await ctx.send(embed = em)
        message = await ctx.send(f"⚔️ - Boss fight start be ready {user.mention}!")
        await asyncio.sleep(3)
        await message.edit(content="🔫 -you damaged the boss !")
        await asyncio.sleep(3)
        await message.edit(content="🩸 -the boss is dying")
        await asyncio.sleep(3)
        await message.edit(content="💰 - you won ")
        await asyncio.sleep(3)

        await ctx.send(f"Success !! you haked the bank account ! and stole {earnings}$")
        users[str(user.id)]["wallet"] += earnings

        with open("bank.json" , "w") as f:
          json.dump(users,bag,f)
        
        









    if item == 'laptop':
      users[str(user.id)]['bag'].pop([i['item'] for i in users[str(user.id)]['bag']].index('laptop', 0))
     
      earnings = random.randrange(1500)
      if earnings < 100:
        em = discord.Embed(color = 0x85e0ff , title = "hacking the world bank you can win 1600$ or you can go to prison")
        await ctx.send(embed = em)
        message = await ctx.send("hacking bank cams")
        await asyncio.sleep(2)
        await message.edit(content="getting bank code ||162.117.823||")
        await asyncio.sleep(2)
        await message.edit(content="trying the security levels!")
        await asyncio.sleep(2)
        await message.edit(content="you found the bitcoin <:coin:782917209055035424> ")
        await asyncio.sleep(2)

      
        await ctx.send("you failed ! police got you and you did get anything")
        


      if earnings > 100:
        em = discord.Embed(color = 0x85e0ff , title = "hacking the world bank you can win 100000$ or you can go to prison")
        await ctx.send(embed = em)
        message = await ctx.send("hacking bank cams")
        await asyncio.sleep(2)
        await message.edit(content="getting bank code ||162.117.823||")
        await asyncio.sleep(2)
        await message.edit(content="trying the security levels!")
        await asyncio.sleep(2)
        await message.edit(content="you found the bitcoin$")
        await asyncio.sleep(2)
 
      
        await ctx.send(f"Success !! you haked the bank account ! and stole {earnings} <:coin:782917209055035424> ")
        users[str(user.id)]["wallet"] += earnings

        with open("bank.json" , "w") as f:
          json.dump(users,f)
        




  

     



async def counsume_item(user,item_name,amount= 1,price = 0):
    item_name = item_name.lower()
    name_ = None
    for item in mainshop:
        name = item["name"].lower()
        if name == item_name:
            name_ = name
            if price==None:
                price = 0.9* item["price"]
            break

    if name_ == None:
        return [False,1]

    cost = price*amount

    users = await get_bank_data()

    bal = await update_bank(user)


    try:
        index = 0
        t = None
        for thing in users[str(user.id)]["bag"]:
            n = thing["item"]
            if n == item_name:
                old_amt = thing["amount"]
                new_amt = old_amt - amount
                if new_amt < 0:
                    return [False,2]
                users[str(user.id)]["bag"][index]["amount"] = new_amt
                t = 1
                break
            index+=1 
        if t == None:
            return [False,3]
    except:
        return [False,3]    

    with open("bank.json","r") as f:
        json.dump(users,f)

    await update_bank(user,cost,"wallet")

    

    return [True,"Worked"]


@use.error
async def use_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        em = discord.Embed(color = 0x85e0ff)
        em.add_field(name = 'This command is ratelimited, please try again in {:.2f}s'.format(error.retry_after) , value = "made by $wip")
        await ctx.send(embed = em)
    else:
        raise error

 # ++++++++++++++++++++++ S L O T S ||  S L O T S    
@client.command()
@commands.cooldown(1, 20, BucketType.user)
async def slots(ctx,amount = None):
    await open_account(ctx.author)
    if amount == None:
        await ctx.send("lol you need to enter a valid amount")
        return

    bal = await update_bank(ctx.author)
    amount = int(amount)
    if amount>bal[0]:
        await ctx.send("You don't have that much money don't lie to me hoe")
        return

    if amount<0:
        await ctx.send("lmao only positive amount of  coins buddy")
        return

    if amount<50:
        await ctx.send("You can minimum slots **50 coins**")
        return

    if amount>2500:
        await ctx.send("Slotting so much money is not nice")
        return



    final = []
    for i in range(3):
        a = random.choice(["🎁","🔥","♦️" ,'🌪'])
        

        final.append(a)
        
        

    await ctx.send(str(final))

    if final[0] == final[1] or final[0] == final[2] or final[2] == final[1]:
        await update_bank(ctx.author,2*amount)
        await ctx.send(f"You won {amount} coins")

    else:
        await update_bank(ctx.author,-1*amount)
        await ctx.send(f"You lost {amount} coins")

@slots.error
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(f"You can use the slot machine again at `{error.retry_after:.0f}` seconds.")   




#======================================U S E || I T E M ===========================







#==========================use commands ========================


@client.command()
async def bet(ctx , amount):
    await open_account(ctx.author)


    users = await get_bank_data()
    user = ctx.author
    bal = await update_bank(ctx.author)


    amount = int(amount)
    if amount<50:
        em = discord.Embed(color = 0x85e0ff , title = 'You can minimum slots **50 coins**')
        await ctx.send(embed = em )
        return

  
    if amount>bal[0]:
        embed = discord.Embed(title = "Error" ,color = 0xffb361  )
        embed.add_field(name = "You don't have that much! " , value = "> finish")
        await ctx.send(embed = embed)
        return

    earnings = random.randint(-amount,amount)
    

    if earnings <-1:
        await update_bank(ctx.author, +1 * earnings)
        await ctx.send(f"> You lost {earnings} coins ")
     
        return
    elif earnings >1:
        await ctx.send(f"> You won  {earnings}$ !!")
        users[str(user.id)]["wallet"] += earnings



    

    with open("bank.json" , "w") as f:
        json.dump(users,f)




#========================================== U S E || I T E M =============================


#====================================sHOP || SHOP ===============================================
async def open_account(user):
    users = await get_bank_data()
     
    

    if str(user.id) in users:
        return False

    else :
        users[str(user.id)] = {}
        users[str(user.id)]["wallet"] = 0
        users[str(user.id)]["bank"] = 0
    
    with open("bank.json" , "w") as f:
        json.dump(users,f)
    
    return True

async def get_bank_data():
    with open("bank.json" , "r") as f:
        users = json.load(f)
    
    return users
    
async def update_bank(user,change = 0,mode = "wallet"):
    users = await get_bank_data()

    users[str(user.id)][mode] += change

    with open("bank.json" , "w") as f:
        json.dump(users,f)
    
    bal = [ users[str(user.id)]["wallet"] , users[str(user.id)]["bank"]]
    return bal  


# rob
@client.command(name = "rob")
@commands.cooldown(1, 40, BucketType.user)
async def rob(ctx , member:discord.Member):
    author = ctx.author
    await open_account(ctx.author)
    await open_account(member)


    bal = await update_bank(member)


    if bal[0]<40: 
        await ctx.send(F"{author.mention} his balanc is under 400 not worth it ")
        return

    earnings = random.randrange(0 ,40 )

    await update_bank(author, earnings)
    await update_bank(member, -1*earnings)

    await ctx.send(f"you robbed and got {earnings} coins!")

@rob.error
async def rob_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        em = discord.Embed(color = 0x85e0ff)
        em.add_field(name = 'This command is ratelimited, please try again in {:.2f}s'.format(error.retry_after) , value = "made by $wip")
        await ctx.send(embed = em)
    else:
        raise error



# C O M M A N D S =============================== | |C O M  MA N D S ===================

@client.command()
async def stats(ctx, guild: discord.Guild = None ):
    guild = ctx.guild if not guild else guild
    embed = discord.Embed(color = 0x85e0ff , title = f"<a:Goos:772133935005433856>{guild} || STATS  📊 " , description = "designd by $wip printed by UFY")
    embed.add_field(name = f" Server Description :" , value = guild.description , inline = False)
    embed.add_field(name = f" Member Count: " , value = guild.member_count , inline = False)
    embed.add_field(name = f" Channel Count:" , value = len(guild.channels), inline = False)
    embed.add_field(name = f" Role Count :" , value = len(guild.roles), inline = False)
    embed.add_field(name = f" Emoji limit :" , value = guild.emoji_limit , inline = False)
    embed.add_field(name = f" Server created :" , value = guild.created_at , inline = False)
    embed.add_field(name = f" Owner:" , value = guild.owner , inline = False)

    await ctx.send(embed = embed)

@client.command()
@commands.has_permissions(manage_messages = True)
async def set_reminder(ctx , time , *, remind):
    member = ctx.author
    em = discord.Embed(color = 0x85e0ff , title = "> Reminder set !")
    em.add_field(name = "Your reminder is " , value = remind)
    await ctx.send(embed = em)
    if time[-1].lower() == "h":
      await asyncio.sleep(int(time[:-1]) * 3600)
    if time[-1].lower() == "m":
       await asyncio.sleep(int(time[:-1]) * 60)
    try:
      em = discord.Embed(color = 0x85e0ff , title = "> Your reminder is :")
      em.add_field(name = remind , value = "command made by $wip processed and executed by UFY")
      await member.send(embed = em)
    except discord.Forbidden:
        return

#==============================K I C K || C O M M A N D =========================

@client.command(aliases=['k'])
@commands.has_permissions(kick_members = True)
async def remove_user(ctx,member:discord.Member,*,reason= "no reason provided" , guild: discord.Guild = None):
    guild = ctx.guild if not guild else guild
    em = discord.Embed(color = 0x85e0ff , title = f"> {member}  has been kicked from {guild}!")
    await ctx.send(embed = em)
    try:
      em = discord.Embed(color = 0x85e0ff , title = f"> {member} You have been kicked from {guild}!")
      em.add_field(name = reason , value = 'command made by $wip processed and executed by UFY')
      await member.send(embed = em)
      await member.kick(reason=reason)
      
   
    except:
      pass



    

@client.command()
async def info(ctx):
    embed1 = discord.Embed(color=0x85e0ff).add_field( name="> <a:8411_WumpusHypesquad:781913762214576128> UFY 📜", value="Page 1 | ABOUT" , )
    embed1.add_field(name = "🌐 -UFY is the global bot " , value = "using a data that can be used in everu server in the world" , inline = False)
    embed1.add_field(name = "🌐 -With functions for moderation and fun it gives you everything you need for your server " , value = "made by $wip" , inline = False)
    

    embed2 = discord.Embed(color=0x85e0ff).add_field( name="> <a:8411_WumpusHypesquad:781913762214576128> STATS 📜", value="Page 2 | States" , )
    embed2.add_field(name = "Servers" , value = f"{len(client.guilds)} servers" , inline = False)
    embed2.add_field(name = "Commands" , value = f"{len(client.commands)} commands" , inline = False)
    embed2.add_field(name = "Members" , value = f"watching {len(client.users)} members" , inline = False)
    embed2.add_field(name = "Ping" , value = f"{round(client.latency * 1000)}ms" , inline = False)
 
 
    
    paginator = DiscordUtils.Pagination.CustomEmbedPaginator(ctx)
    embed3 = discord.Embed(color=0x85e0ff).add_field(name="Close page", value="Page 3")
    paginator.add_reaction('⏪', "first")
    paginator.add_reaction('◀️', "back")
    paginator.add_reaction('❌', "delete")
    paginator.add_reaction('▶️', "next")
    paginator.add_reaction('⏩', "last")
    embeds = [embed1, embed2, embed3]
    await paginator.run(embeds)
    
 


#clear💬================💬============💬================💬====================
@client.command(aliases=['c'])
@commands.has_permissions(manage_messages = True)
async def clear(ctx,amount=2):
    await ctx.channel.purge(limit = amount)
    embed = discord.Embed(color = 0x85e0ff , title = "> UFY ")
    embed.set_author(name=f"I have cleared {amount} messages.") 
    await ctx.send(embed= embed, delete_after=5)

#embed maeker 
@client.command(aliases=["emb"])
@commands.has_permissions(manage_messages = True)
async def embed(ctx, title1 ,*, description):
  embed = discord.Embed(title = title1, color = 0x85e0ff)
  embed.add_field(name = "EMBED:" , value = description)
  await ctx.send(embed = embed)




@client.command()
async def hack(ctx , member:discord.Member):
  if not member:
    await ctx.send(f"{ctx.author.mention} mention  a member to hack ")
    return
  message = await ctx.send("hacking now geting ip")
  await asyncio.sleep(2)
  await message.edit(content="he's ip is ||162.117.823||")
  await asyncio.sleep(2)
  await message.edit(content="hacking his gmail!")
  await asyncio.sleep(2)
  await message.edit(content=f">his email is \n> {member.name}@gmail.com \npassword : {member.name}123")
  await asyncio.sleep(2)
  await message.edit(content="account hacked!")








@client.command()
async def ufy(ctx):
  em = discord.Embed(color = 0x85e0ff)
  em.add_field(name = "<a:7484_Alphabet_U:781997224535523349>| <a:7816_Alphabet_F:781997223365181482>|<a:8187_Alphabet_Y:781997199907225611> " , value = "I am a bored owner")
  await ctx.send(embed = em)

@client.command()
async def yes(ctx):
  em = discord.Embed(color = 0x85e0ff)
  em.add_field(name = "<a:Y_:781997199907225611> | <a:E_:782004893061742662> | <a:1844_Alphabet_S:782004871733313546> " , value = "I am a bored owner")
  await ctx.send(embed = em)

@client.command()
async def ok(ctx):
  em = discord.Embed(color = 0x85e0ff)
  em.add_field(name = "<a:O_:782006700512378882> | <a:K_:782006694640615484> " , value = "I am a bored owner")
  await ctx.send(embed = em)

@client.command()
async def no(ctx):
  em = discord.Embed(color = 0x85e0ff)
  em.add_field(name = "<a:N_:782007589533384715> | <a:O_:782006700512378882>  " , value = "I am a bored owner")
  await ctx.send(embed = em)
  
#A U T O || M O D E R A T I O N 




@client.event
async def on_member_join(member):
    guild: discord.Guild = member.guild
    channels = guild.channels

    if str(guild.id) not in Data.server_data:
        Data.server_data[str(guild.id)] = Data.create_new_data()
    data = Data.server_data[str(guild.id)]

    print(f"{member} has joined {guild} server...")

    join_role = guild.get_role(data["join_role"])
    if join_role is not None:
        await member.add_roles(join_role)

    # Welcome Message
    if data["welcome_msg"] is None:
        server_wlcm_msg = f"Welcome, {member.mention}, to the Official **{guild.name}** Server"
    else:
        server_wlcm_msg = data["welcome_msg"]
        server_wlcm_msg = server_wlcm_msg.replace(
            "[mention]", f"{member.mention}")

    # Welcome Channel
    wel_channel = None

    if data["welcome_channel"] is None:
        for channel in channels:
            if str(channel).find("welcome") != -1:
                wel_channel = channel
                break
    else:
        wel_channel = guild.get_channel(int(data["welcome_channel"]))

    try:
        await wel_channel.send(server_wlcm_msg)
    except AttributeError:
        print("DEBUG: No welcome channel has been set or found.")














@client.command(name="data")
async def data(ctx):
    is_owner = await client.is_owner(ctx.author)
    if is_owner or ctx.author.id == 586531356272754709:  # for real UFY
        data_file = discord.File("data.json")
        await ctx.send(file=data_file)


@client.command()
async def update(ctx , argument):
    if argument == "data":
        is_owner = await client.is_owner(ctx.author)
        if is_owner or ctx.author.id == 586531356272754709:
          em = discord.Embed(color = 0x88fcd0)
          em.add_field(name = "data has been updates with succes!" , value = "just the owner can run this command ")
          await ctx.send(embed = em)
          await Data.auto_update_data()
    else:
        await ctx.send("you can't run this command !")

   

#==========================================

@client.event
async def on_message(message: discord.Message):
 

    author: discord.Member = message.author
    channel: discord.TextChannel = message.channel
    guild: discord.Guild = message.guild
    # print(str(author), ": ", message.content)

    await client.process_commands(message)

    if str(guild.id) not in Data.server_data:
        Data.server_data[str(guild.id)] = Data.create_new_data()

    data = Data.server_data[str(guild.id)]

    if message.content.replace('!', '') == client.user.mention:
        pre = prefix
        await channel.send(f"The prefix in this server is `{pre}`")



    if data["pay_respects"] and message.content.strip().lower() == "f":
        await channel.send(f"**{author.display_name}** has paid their respects...")

    if data["active"] and str(author.id) not in data["users"]:
        if not str(channel.id) in data["channels"]:
            perms = author.permissions_in(channel)
            if not perms.administrator:
                if "http://" in message.content or "https://" in message.content:
                    if len(data["urls"]) > 0:
                        for url in data["urls"]:
                            if not url in message.content:
                                await channel.purge(limit=1)
                                msg1 = await channel.send(f"{author.mention}, you are not allowed to send links in this channel.")
                                await asyncio.sleep(2)
                                await msg1.delete()
                    else:
                        await channel.purge(limit=1)
                        msg2 = await channel.send(f"{author.mention}, you are not allowed to send links in this channel.")
                        await asyncio.sleep(3)
                        await msg2.delete()

                elif len(message.attachments) > 0:
                    await channel.purge(limit=1)
                    msg3 = await channel.send(f"{author.mention}, you are not allowed to send attachments in this channel.")
                    await asyncio.sleep(3)
                    await msg3.delete()

    previous_msg_sender_id = author.id

#invits tracker



@client.command(pass_context=True, name='status')
async def member_status(ctx, member: discord.Member):
    embed = discord.Embed(color = THEME_COLOR)
    embed.add_field(name = (str(member.status)) , value = 'test')
    embed.set_footer(text=f"Requested by {ctx.author}")
    embed.add_field(name="ID:", value=member.id , inline = False)
    embed.add_field(name="Display Name:", value=member.display_name , inline= False)
    await ctx.send(embed = embed)

@client.command()
async def tag(ctx, tag):
    if tag == "embed":
        em = discord.Embed(color = 0x919eff)
        em.add_field(value = f"[Embed_maker!](https://discordpy.readthedocs.io/en/latest/ext/commands/api.html?highlight=indents#help-commands)", name = "Docs \nEmbed" , inline = False)
        em.add_field(value = f"[Help_command](https://discordpy.readthedocs.io/en/latest/ext/commands/api.html?highlight=indents#help-commands)", name = "Docs \nHelp" , inline = False)
        em.add_field(value = f"[Embed_infos](https://discordpy.readthedocs.io/en/latest/search.html?q=embed)", name = "Docs \nHelp" , inline = False)
        await ctx.send(embed = em)
    if tag  == "db":
        em = discord.Embed(color = 0x919eff)
        em.add_field(value = f"[Data_base!](https://pypi.org/project/replit/)", name = "Docs \ndata - base repl.it" , inline = False)
        await ctx.send(embed = em)




@client.command()
async def listcogs(ctx):
	
		base_string = "```css\n"  # Gives some styling to the list (on pc side)
		base_string += "\n".join([str(cog) for cog in client.extensions])
		base_string += "\n```"
		await ctx.send(base_string)



@client.command()
async def test_db(ctx, text):
    member = ctx.author
    try:
        tempvar = db[member.id]
    except:
        db[member.id] = []
        tempvar = db[member.id]
    tempvar.append(text)
    db[member.id] = tempvar
    em = discord.Embed(color = 0x88fcd0)
    em.add_field(name = "data base system save !" , value = "errors = o")
    await ctx.send(embed = em)

@client.command()
async def show(ctx):
    member = ctx.message.author
    for test_db in db[member.id]:
        await ctx.send(f"```{test_db}```")


@client.command()
async def delete_data(ctx): 
  del db['text_db']

@client.command()
async def list_keys(ctx):
    keys = db.keys()
    embed = discord.Embed(color = 0x88fcd0)
    
    embed.add_field(value  = keys , name = "succes the message was sent" )
    await ctx.send(embed = embed)



keep_alive()
TOKEN = os.environ.get('DISCORD_BOT_SECRET')
client.run(TOKEN)
