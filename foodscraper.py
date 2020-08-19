import json, discord, time, sys
from urllib.request import Request, urlopen
from discord.ext import tasks

discord_token = "" # API Key
client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user.name} | {client.user.id} has logged in')


@client.event
async def on_message(message):

    channel = client.get_channel(733404047045820458)
    counter = 0
    
    url = 'https://www.reddit.com/r/FoodPorn.json'
    request = Request(url, headers = {'User-Agent' : 'Food Porn image scraper bot'})
    info = urlopen(request).read()
    data = json.loads(info)
    
    if '!food' in message.content.lower():
    
        while counter <= 2:

            post_link = data['data']['children'][counter]['data']['permalink']
            post_image = data['data']['children'][counter]['data']['url']
            post_title = data['data']['children'][counter]['data']['title']
            counter += 1

            embed = discord.Embed(
                title = post_title,
                description = f'https://www.reddit.com{post_link}',
                colour = discord.Colour.blue()
                )

            embed.set_image(url = post_image)
            
            await channel.send(embed = embed)
            time.sleep(5)

@tasks.loop(hours=24)
async def count():
    
    channel = client.get_channel(733404047045820458)
    counter = 0
    
    if channel is not None:
        
        url = 'https://www.reddit.com/r/FoodPorn.json'
        request = Request(url, headers = {'User-Agent' : 'Food Porn image scraper bot'})
        info = urlopen(request).read()
        data = json.loads(info)
        
        while counter <= 2:

            post_link = data['data']['children'][counter]['data']['permalink']
            post_image = data['data']['children'][counter]['data']['url']
            post_title = data['data']['children'][counter]['data']['title']
            counter += 1

            embed = discord.Embed(
                title = post_title,
                description = f'https://www.reddit.com{post_link}',
                colour = discord.Colour.blue()
                )

            embed.set_image(url = post_image)
                
            await channel.send(embed = embed)
            time.sleep(2.5) 
        
count.start()
client.run(discord_token)

