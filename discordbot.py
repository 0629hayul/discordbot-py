from cmath import log
from distutils.sysconfig import PREFIX
import discord
from time import sleep
from dotenv import load_dotenv
from discord.ext import commands
import os
load_dotenv()

PREFIX = os.environ['PREFIX']
TOKEN = os.environ['TOKEN']

client = discord.Client()

@client.event
async def on_ready():
    print(f'Logged in as {client.user}.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == f'{PREFIX}tck h':
        embedVar = discord.Embed(title="**help**", color=0x0094ff)
        embedVar.add_field(name="**접두사 : .",value="", inline=False)
        embedVar.add_field(name="",value="- **.tck h** : 명령어확인", inline=False)
        embedVar.add_field(name="",value="- **.tck a** : 관리자 호출", inline=False)
        embedVar.add_field(name="",value="- **.tck g** : 트리넷 게임", inline=False)
        embedVar.add_field(name="",value="- **.tck e** : 젠 환전", inline=False)
        embedVar.add_field(name="",value="- **.tck b** : 젠 구매(충전)", inline=False)
        embedVar.add_field(name="",value="- **.tck c** : 기타 질문", inline=False)
        embedVar.add_field(name="",value="- **.tck p** : 등업기준", inline=False)
        await message.channel.send(embed=embedVar)  

    if message.content.startswith(f'{PREFIX}tck a'):
        await message.channel.send('<@&1081564782102052864>을 호출했습니다. 잠시만 기다려주세요.')

    if message.content.startswith(f'{PREFIX}tck g'):
        await message.channel.send('<@1078124256975659102>\n잠시만 기다려주세요 {member.display_name}님. 대기열 확인 후 게임이 시작됩니다.')
    
    if message.content.startswith(f'{PREFIX}tck e'):
        await message.channel.send('젠 환전 안내```* 최소 가격은 10,000원입니다.\n* 환전 가격은 1,000원 단위로 내림계산합니다.\n* 환전 수수료 5%입니다.\n* 환전은 계좌(80%), 문화상품권(90%) 중 선택 환전입니다.```- 젠 구매 ㅣ <#1082635906894270564>\n- 젠 환전은 <@1078124256975659102> DM으로 문의주세요.')
    
    if message.content.startswith(f'{PREFIX}tck b'):
        await message.channel.send('젠 가격표```- 𝟱,𝟬𝟬𝟬젠 : 계좌 : 4,000원 & 문상 : 5,000원\n- 𝟭𝟬,𝟬𝟬𝟬젠 : 계좌 : 8,000원 & 문상 : 10,000원\n- 𝟮𝟬,𝟬𝟬𝟬젠 : 계좌 : 15,000원 & 문상 : 20,000원\n- 𝟮𝟬,𝟬𝟬𝟬젠 이상 : 계좌 : 원가 70%가격 & 문상 : 원가```20,000젠 이상 문상으로 구매시 5,000단위 반올림으로 계산합니다.\n젠 구매는 <@1078124256975659102> DM으로 문의주세요.')

    if message.content.startswith(f'{PREFIX}tck c'):
        await message.channel.send('기타 질문 - <@1078124256975659102> DM 혹은 <#1082642789868785806>체널에 문의주세요.')
  
    if message.content == f'{PREFIX}tck p':
        embedVar = discord.Embed(title="**등업 기준&역할 정보**", color=0x0094ff)
        embedVar.add_field(name="",value="- **master** : 𝟭𝟬𝟬,𝟬𝟬𝟬젠 이상 보유ㅣ혜택 : 환전 수수료 무료&10,000젠 무료지급", inline=False)
        embedVar.add_field(name="",value="- **VIP** : 𝟱𝟬,𝟬𝟬𝟬젠 이상 보유ㅣ혜택 : 환전 수수료 무료&5,000젠 무료지급", inline=False)
        embedVar.add_field(name="",value="- **expert** : 𝟮𝟬,𝟬𝟬𝟬젠 이상 보유ㅣ혜택 : 5,000젠 무료지급", inline=False)
        embedVar.add_field(name="",value="- **ruki** : 𝟱,𝟬𝟬𝟬젠 이상 보유ㅣ혜택 : 3,000젠 무료지급", inline=False)
        embedVar.add_field(name="",value="- **member** : 서버 가입 7일 이상ㅣ혜택 : 2,000젠 무료지급 (신청 : <#1081825390584139827>열고 서버가입혜택지급요청시 수령 가능합니다.", inline=False)
        await message.channel.send(embed=embedVar) 
        
try:
    client.run(TOKEN)
except discord.errors.LoginFailure as e:
    print("Improper token has been passed.")
