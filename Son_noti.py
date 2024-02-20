import discord
from discord.ext import commands

TOKEN = 'MTIwOTEwNDU5MzU5OTA3MDI0OQ.G2Aw5t.1jVGE0zkrGnMYmDU-ANcQ6g9KeNLc7g2EP2ZSg'
CHANNEL_ID = '1209141953002733618'   #광태 공습경보
USER_ID = '295482295467376650'  #광태 아이디
intents = discord.Intents.default()
intents.message_content = True

# class Member(USER_ID):
#     if self

class MyClient(discord.Client):
    async def on_ready(self):
        channel = self.get_channel(int(CHANNEL_ID))
        User = self.get_user(int(USER_ID))
        await client.change_presence(activity=discord.Game("광태 감지"),status=discord.Status.online)
        # if User(discord.Member.status) == discord.Status.online:
        #     await channel.send('..')
        # print(User.name)
        print(int(USER_ID))
        print(channel)
        print(users)
        # await discord.client.Client.fetch_user_profile(User)



client = MyClient(intents=intents)
client.run(TOKEN)