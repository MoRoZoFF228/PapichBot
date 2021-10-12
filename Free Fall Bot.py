import discord
from discord.ext import commands
from datetime import datetime
import datetime
from discord.ext import menus
import json
from random import choice
from discord import Embed

bot = commands.Bot(
    command_prefix="-",
    case_insensitive=True,
    intents=discord.Intents.all()
)


@bot.event
async def on_ready():
    game = discord.Game("-info | Patch v0.70")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="-info/-инфо | Test Path v.0.1.0"))
    print("\nLogged in as:", bot.user.name)
    print("ID:", bot.user.id)
    print("\nAvaliable guilds:")
    for guild in bot.guilds:
        print(guild.name, guild.id)

    print("\nПриятного Использования!)")


@bot.command(name="echo", aliases=['аче'])
@commands.has_any_role(767082220514705458, 702066740242284619)
async def echo(ctx, *, content: str):
    await ctx.send(content)
    await ctx.message.delete()


async def cool(ctx):
    await ctx.send('You are cool indeed')


@bot.command(name="ping")
async def ping(ctx):
    await ctx.send("Connection time(Delay): {0}ms.".format(bot.latency))
    await ctx.message.delete()


@bot.command(name="info", aliases=["инфо"])
async def info(ctx):
    embed = discord.Embed(
        title="Free Fall Bot",
        colour=discord.Colour(000000),
        description="Вас приветствует игровой бот собственной разработки **Free Fall Bot**.")
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/745691018103619724/886994370186862592/IMG_20210823_183744.jpg")
    embed.add_field(name="О Боте:", value="**Префикс бота: -**", inline=False)
    embed.add_field(
        name="Free Fall Bot - игровой бот для сервера **Free Fall Team v.1.51**",
        value="Hа других серверах он присутсвовать **не будет!!!**",
        inline=False)
    embed.add_field(name="_ _", value="_ _", inline=False)
    embed.add_field(name="Функционал:", value="_ _", inline=False)
    embed.add_field(
        name="Игра **'Хроники Хаоса':**",
        value="RPG игра, адаптированная под дискорд",
        inline=False)
    embed.add_field(name="_ _", value="_ _", inline=False)
    embed.add_field(
        name="C командами можно ознакомиться, прописав команду:",
        value="**commands/команды**",
        inline=False)
    embed.add_field(
        name="_ _",
        value="По всем вопросам к боту обратитесь к создателю: <@527771957198979073>",
        inline=False)
    embed.set_footer(
        text=f"Запросил: {ctx.author.display_name}",
        icon_url=f"{ctx.author.avatar_url}")
    await ctx.send(content="Информация о боте будет обновлена после написания кода", embed=embed)


@bot.command(name='commands', aliases=['команды'])
async def commands(ctx):
    embed = discord.Embed(title='Список доступных команд:', color=0x007dd1)
    embed.add_field(
        name='-профиль',
        value='Профиль пользователя.',
        inline=False)
    embed.add_field(
        name='-ббитва',
        value='Быстрая битва с боссами/идолами, которые доступны в боте.',
        inline=False)
    embed.add_field(
        name='-магазин',
        value='Магазин предметов для прокачки урона.',
        inline=False)
    embed.add_field(
        name='-задания',
        value='Выбор доступных заданий.',
        inline=False)
    embed.add_field(
        name='-принять',
        value='Принять задание/битву.',
        inline=False)
    embed.add_field(
        name='-отказ',
        value='Отказаться от задания/битвы.',
        inline=False)
    embed.add_field(name='-атака', value='Атаковать босса/идола', inline=False)
    embed.set_footer(
        text=f"Запросил: {ctx.author.display_name}",
        icon_url=f"{ctx.author.avatar_url}")
    await ctx.send(embed=embed)


@bot.command(name='profile', aliases=['профиль'])
async def profile(ctx):
    embed = discord.Embed(
        title=f"Карточка {ctx.author.display_name}",
        colour=discord.Colour(16711680))
    embed.set_thumbnail(
        url="https://i.ytimg.com/vi/st5cNzSPaN0/maxresdefault.jpg")
    embed.add_field(name="_ _", value='_ _')
    embed.add_field(
        name="Количество сыгранных битв:",
        value='0(пример)',
        inline=False)
    embed.add_field(name="Количество XP:", value='500xp(пример)', inline=False)
    embed.add_field(
        name="Урон, наносимый за 1 удар:",
        value=' 100xp(пример)',
        inline=False)
    embed.add_field(name="Побед:", value='0(пример)', inline=False)
    embed.add_field(name="Поражений:", value='0(пример)', inline=False)
    embed.add_field(
        name="Количество монет:",
        value='500(пример)',
        inline=False)
    embed.add_field(
        name="Количество золота:",
        value='10(пример)',
        inline=False)
    embed.add_field(name="_ _", value='_ _', inline=False)
    embed.add_field(
        name="**Error!!!**",
        value='The Statistics system is not available',
        inline=False)
    embed.set_footer(
        text=f"Запросил: {ctx.author.display_name}",
        icon_url=f"{ctx.author.avatar_url}")
    await ctx.send(content="Команды тестовые! Во время разработки они будут улучшаться", embed=embed)


@bot.command(name='question', aliases=['задания'])
async def question(ctx):
    embed = discord.Embed(title="Задания: ", colour=discord.Colour(16711680))
    embed.set_thumbnail(
        url="https://e7.pngegg.com/pngimages/916/858/png-clipart-computer-icons-checklist-checklist-miscellaneous-angle.png")
    embed.add_field(name='Битва с боссами', value='-боссы', inline=False)
    embed.add_field(name='Битва с идолами', value='-идолы', inline=False)
    embed.add_field(
        name='Битва за сокровища',
        value='-сокровища',
        inline=False)
    embed.add_field(
        name='_ _',
        value='Выберите подходящее для вас задание, прописав команду, указаную под заданием!',
        inline=False)
    embed.set_footer(
        text=f"Запросил: {ctx.author.display_name}",
        icon_url=f"{ctx.author.avatar_url}")
    await ctx.send(content="Команды тестовые! Во время разработки они будут улучшаться", embed=embed)


bot.run("ODMxNTYxOTU3MzMzMTM5NTA3.YHXCbA.QWSjCJaC4WuImkT_ik-4JZP6MGc")
