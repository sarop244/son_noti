import discord

TOKEN = 'MTIwOTEwNDU5MzU5OTA3MDI0OQ.GRZnUf.YCLdwVZz7Po_e1oz_E8Ac0MQJr2zaV82hMcC6Y'
CHANNEL_ID = 1209141953002733618                        # 광태 공습경보
USER_ID = 295482295467376650                            # 광태 아이디
SERVER_ID = 387940168159723540                          # 서버 아이디

intents = discord.Intents.all()
intents.presences = True                                # Presence Intent 활성화

class MyClient(discord.Client):
    async def on_ready(self):
        print('로그인')

    async def on_presence_update(self, before, after):  # 상태창 변경될때마다 실행
        guild = self.get_guild(SERVER_ID)               # 길드
        User = guild.get_member(USER_ID)                # 길드 겟멤버를 해야 status 를 사용할수있음
        print(User,before)
        if before == User:                              # 바뀜을 감지한 유저와 '광태'가 같은 사람인지 확인

            if User.status == discord.Status.online:    # 메시지를 보낼 채널을 찾음
                channel = self.get_channel(CHANNEL_ID)
                if channel:                             # 메시지를 보냄
                    await channel.send('광태 감지')


client = MyClient(intents=intents)
client.run(TOKEN)