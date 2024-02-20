import discord
import asyncio  # 슬립 사용을위한

TOKEN = 'MTIwOTEwNDU5MzU5OTA3MDI0OQ.GI1hC9.HYrBTOhpJ5sA5Y4mmErjo7ovAb3BWDwHk3DV8s'
CHANNEL_ID = 1209141953002733618   # 광태 공습경보
USER_ID = 295482295467376650  # 광태 아이디
SERVER_ID = 387940168159723540 # 서버 아이디

intents = discord.Intents.all()
intents.presences = True  # Presence Intent 활성화
class MyClient(discord.Client):
    async def on_ready(self):
        print('로그인')
        while True:
            await self.check_member_status()
            await asyncio.sleep(5)  # 5초마다 상태 확인

    async def check_member_status(self):
        print('첫번째 단계')  # 이 부분이 호출되지 않는 문제를 확인하기 위해 추가
        guild = self.get_guild(SERVER_ID)

        if guild:
            member = guild.get_member(USER_ID)
            if member:
                if member.status != discord.Status.online:
                    channel = self.get_channel(CHANNEL_ID)
                    if channel:
                        await channel.send('광태 감지')

        # guild = self.get_guild(SERVER_ID)
        # User = guild.get_member(USER_ID)

        # if User.status != discord.Status.online:
        #     channel = self.get_channel(CHANNEL_ID)
        #     if channel:
        #         await channel.send('광태 감지')

client = MyClient(intents=intents)
client.run(TOKEN)