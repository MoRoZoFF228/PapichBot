import discord
from discord.ext import commands
from datetime import datetime
import datetime
from discord.ext import menus
import json
from random import choice

bot = commands.Bot(
                command_prefix = "-",
                case_insensitive = True,
                intents = discord.Intents.all()
                )


@bot.event
async def on_ready():
    game = discord.Game("-info | Patch v0.6.0")
    await bot.change_presence(status=discord.Status.idle, activity=game)
    print("\nLogged in as:",bot.user.name)
    print("ID:",bot.user.id)
    print("\nAvaliable guilds:")
    for guild in bot.guilds:
        print(guild.name,guild.id)

    print("\nПриятного Использования!)")



@bot.event
async def on_message_delete(payload):
   channel = bot.get_channel(id=825421428501250088)
   embed = discord.Embed(title="Сообщение было удалено", colour=discord.Colour(16711680), description="")
    
   embed.add_field(name="Удалённое сообщение", value='```Удалённое сообщение```')
   await channel.send(content = '_ _', embed=embed)
   





class MyMenu(menus.Menu):
    async def send_initial_message(self, ctx, channel):
       embed = discord.Embed(title='Papich Bot || Trello Board', colour=discord.Colour(000000), description="**Вас приветствует бот собственной разработки Papich Bot. Дальше будет описана информация о боте, так что просьба: Прочитайте Внимательно нижеуказанную информацию, чтобы не возникало лишних вопросов. Приятного Использования)**. По всем вопросам к боту обратитесь к создателю: <@527771957198979073>", url="https://trello.com/b/YyB5iroK/papich-bot")

       embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/745691018103619724/796995766656565259/PapichBot_Avatar_v2.0.png")
       embed.set_author(name="Papich Bot", url="https://github.com/MoRoZoFF228/PapichBot/blob/main/description.md")

       embed.add_field(name="О Боте", value="**Префикс бота: `-`**. Papich Bot является тестовым ботом, поэтомму он может отличатся от функционала полноценных ботов, таких как:  _ _ `-Dungeon Durker` _ _`-JuniperBot` _ _ `-MEE6` и других ботов. _ _ В дальнейшем бот будет переделан и доступен в общий доступ, с возможностью добавления бота на свой сервер")
       embed.add_field(name="Функционал", value="Papich Bot имеет возможность мутить/кикать/банить участников сервера, которые нарушили правила. Имеет систему аудита для Администрации сервера. Также он имеет систему 'Cтатистики Участников', в которой каждый участник сервера может посмотреть 'Карточку Пользователя', в которой будет указано количество сообщений, количество репутации и прочую информацию. В дальнейшем появится так называемые Веселости, в виде команд ")
       return await channel.send(embed=embed)


    @menus.button("\N{SOON WITH RIGHTWARDS ARROW ABOVE}")
    async def on_soon(self, payload):
        embed = discord.Embed(title='_ _', colour=discord.Colour(000000), url="https://discordapp.com")
        embed.set_author(name="", url="https://discordapp.com")
        embed.set_footer(text="Произодство: MoRoZoFF228#2697", icon_url="https://cdn.discordapp.com/attachments/745691018103619724/764170264640225330/unknown.png")

        embed.add_field(name="Команды", value="Вот список доступных команд: `durka` - шуточная командa для вызова дурка. `poisk` - команда для направления человека в канал <#745691592492580965>, если он искал напарника в неправильном канал. `media` - команда для направления человека в канал <#742797730983837727>, если он прислал фото/видеоматериал не по теме разговора.")
        await self.message.edit(embed=embed)

    @menus.button("\N{BACK WITH LEFTWARDS ARROW ABOVE}")
    async def on_back(self, payload):
        embed = discord.Embed(title='_ _', colour=discord.Colour(000000), url="https://discordapp.com")
        embed.set_author(name="", url="https://discordapp.com")
        embed.set_footer(text="Произодство: MoRoZoFF228#2697", icon_url="https://cdn.discordapp.com/attachments/745691018103619724/764170264640225330/unknown.png")

        embed.add_field(name="Команды для Администрации", value="`ban` -бан пользователя. `kick` - изгнание пользователя с сервера. `colony` - мьют пользователя(**Команда временно недоступна**). `unban/unmute` команды также временно недоступны, как и команда `reader`")
        await self.message.edit(embed=embed)

    @menus.button("\N{END WITH LEFTWARDS ARROW ABOVE}")
    async def on_end(self, payload):
       embed = discord.Embed(title='Papich Bot || Trello Board', colour=discord.Colour(000000), description="**Вас приветствует бот собственной разработки Papich Bot. Дальше будет описана информация о боте, так что просьба: Прочитайте Внимательно нижеуказанную информацию, чтобы не возникало лишних вопросов. Приятного Использования)**", url="https://trello.com/b/YyB5iroK/papich-bot")

       embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/745691018103619724/796995766656565259/PapichBot_Avatar_v2.0.png")
       embed.set_author(name="Papich Bot", url="https://github.com/MoRoZoFF228/PapichBot/blob/main/description.md")

       embed.add_field(name="О Боте", value="**Префикс бота: `-`**. Papich Bot является тестовым ботом, поэтомму он может отличатся от функционала полноценных ботов, таких как:  _ _ `-Dungeon Durker` _ _`-JuniperBot` _ _ `-MEE6` и других ботов. _ _ В дальнейшем бот будет переделан и доступен в общий доступ, с возможностью добавления бота на свой сервер")
       embed.add_field(name="Функционал", value="Papich Bot имеет возможность мутить/кикать/банить участников сервера, которые нарушили правила. Имеет систему аудита для Администрации сервера. Также он имеет систему 'Cтатистики Участников', в которой каждый участник сервера может посмотреть 'Карточку Пользователя', в которой будет указано количество сообщений, количество репутации и прочую информацию. В дальнейшем появится так называемые Веселости, в виде команд ")
       await self.message.edit(embed=embed)


@bot.command(name = 'info', aliases = ['инфо'])
async def menu_example(ctx):
    m = MyMenu()
    await m.start(ctx)
    await ctx.message.delete()


@bot.command(name = "echo", aliases = ['аче'])
@commands.has_any_role(702066740242284619, 706606973289758822)
async def echo(ctx, *, content:str):
    await ctx.send(content)
    await ctx.message.delete()
async def cool(ctx):
    await ctx.send('You are cool indeed')

@bot.command(name = 'swear', aliases = ['свир', 'мат'])
@commands.has_any_role(702066740242284616, 702066740242284615 , 716267660639469602, 702066740242284617, 702066740242284619, 706606973289758822)
async def swear_command(ctx, member: discord.Member):
    
    await ctx.send(f" {member.mention} Следите за языком, пожалуйста. С вашего счёта было списано 25 единиц репутации")
    await ctx.message.delete()
async def cool(ctx):
    await ctx.send('You are cool indeed')

@bot.command(name = 'message', aliases = ['сообщения'])
async def mystats(ctx):
    embed = discord.Embed(title=f"Колличество сообщений {ctx.author.display_name}", colour=discord.Colour(16711680), description="Количество сообщений:", timestamp=ctx.message.created_at)
    
    embed.add_field(name="**Error!!!**", value='The Statistics system is not available')
    await ctx.send(content="_ _", embed=embed)
    await ctx.message.delete()

@bot.command(name = 'mystats', aliases = ['я', 'статистика'])
async def mystats(ctx):
   embed = discord.Embed(title=f"Карточка {ctx.author.display_name}", colour=discord.Colour(16711680), description="", timestamp=ctx.message.created_at)
   
   embed.add_field(name="**Error!!!**", value='The Statistics system is not available')
   await ctx.message.delete()
   await ctx.send(content="_ _", embed=embed)

@bot.command(name = 'mylvl', aliases = ['уровень'])
async def mystats(ctx):
   embed = discord.Embed(title=f"Уровень {ctx.author.display_name}", colour=discord.Colour(16711680), description="Уровень: 1", timestamp=ctx.message.created_at)
   
   embed.add_field(name="**Error!!!**", value='The Statistics system is not available')
   await ctx.send(content="_ _", embed=embed)
   await ctx.message.delete()

@bot.command(name = 'myrep', aliases = ['реп', 'репутация'])
async def mystats(ctx):
   embed = discord.Embed(title=f"Репутация {ctx.author.display_name}", colour=discord.Colour(16711680), description="Репутация: 100", timestamp=ctx.message.created_at)
   
   embed.add_field(name="**Error!!!**", value='The Statistics system is not available')
   await ctx.send(content="_ _", embed=embed)
   await ctx.message.delete()


@bot.command(name = 'durka', aliases = ['дурка'])
@commands.has_any_role(702066740242284616, 702066740242284615 , 716267660639469602, 702066740242284617, 702066740242284619,706606973289758822)
async def durka_command(ctx, members: commands.Greedy[discord.Member]):
    mentions = " ".join(user.mention for user in members)
    await ctx.send(f"Из-за серьёзных бед с башкой, мы должны изолировать {mentions} от здоровых людей. Счет за лечение вышлем по Почте России")
    await ctx.message.delete()
    await ctx.send(file=discord.File('Durka.jpg'))
async def cool(ctx):
    await ctx.send('You are cool indeed')
    

@bot.command(name = 'slap', aliases = ['hat', 'шапка'])
@commands.has_any_role(702066740242284616, 702066740242284615 , 716267660639469602, 702066740242284617, 702066740242284619, 706606973289758822)
async def hat_command(ctx, member: discord.Member):
    await ctx.send(f"Дружище {member.mention}, шапка в порядке?")
    await ctx.message.delete()
async def cool(ctx):
    await ctx.send('You are cool indeed')



@bot.command(name = 'poisk', aliases = ['поиск'])
@commands.has_any_role(702066740242284616, 702066740242284615 , 716267660639469602, 702066740242284617, 702066740242284619, 706606973289758822)
async def poisk_command(ctx, member: discord.Member):
    await ctx.send(f'**ДАННЫЙ КАНАЛ НЕ ДЛЯ ПОИСКА ИГРОКОВ**, {member.mention} пожалуйста, используйте канал <#745691592492580965>')
    await ctx.message.delete()
    await ctx.send(file=discord.File('Poisk.png'))
async def cool(ctx):
    await ctx.send('You are cool indeed')

@bot.command(name = 'media', aliases = ['медиа'])
@commands.has_any_role(702066740242284616, 702066740242284615 , 716267660639469602, 702066740242284617, 702066740242284619, 706606973289758822)
async def media_command(ctx, member: discord.Member):
    await ctx.send(f"Фото и прочим медиафайлом не место в этом чате.{member.mention} Пожалуйста, используйте канал <#742797730983837727>")
    await ctx.message.delete() 
    await ctx.send(file=discord.File('Media.png'))
async def cool(ctx):
    await ctx.send('You are cool indeed')



@bot.command(name = 'kick', aliases = ['кик'])
@commands.has_any_role(702066740242284616, 702066740242284615 , 716267660639469602, 702066740242284617, 702066740242284619,706606973289758822)
@commands.has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member, *, reason=None):
  await member.kick(reason=reason)
  await ctx.message.delete()
async def cool(ctx):
    await ctx.send('You are cool indeed')



@bot.command(name = 'ban', aliases = ['бан'])
@commands.has_any_role(702066740242284616, 702066740242284615 , 716267660639469602, 702066740242284617, 702066740242284619, 706606973289758822)
async def ban(ctx, member : discord.Member, *, reason=None):
  await member.ban(reason=reason)
  await ctx.message.delete()
async def cool(ctx):
    await ctx.send('You are cool indeed')



bot.run("NzY3MDgwNjAxNjE0MDI0NzI0.X4stew.aj6SpNppy0_80V052M55YCiYPgo")