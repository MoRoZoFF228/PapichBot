import discord
from discord.ext import commands
from datetime import datetime
import datetime
import asyncio

bot = commands.Bot(
                command_prefix = "_",
                case_insensitive = True,
                intents = discord.Intents.all()
                )


@bot.event
async def on_ready():
    print("\nLogged in as:",bot.user.name)
    print("ID:",bot.user.id)
    print("\nAvaliable guilds:")
    for guild in bot.guilds:
        print(guild.name,guild.id)

    print("\nReady to use!")


@bot.event
async def on_message(message):
    await bot.process_commands(message)
    if not message.author.bot:
        print(message.content)

    #On Ping Message
    if "<@767080601614024724>" in message.content:
        welcome = "Приветствую тебя на моём сервере. Чувствуй себя как дома и помни что Адекватность - это Неотъемливая часть сервера"
        await message.channel.send(welcome)


@bot.command(name = 'info', aliases = ['инфо'])
async def info(ctx):
    embed = discord.Embed(title='', colour=discord.Colour(0xff8500), description="При обнаружении проблем с ботом, просьба написать об этом в канал <#796001512047640627> или разработчику бота: <@527771957198979073>")

    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/745691018103619724/796995766656565259/PapichBot_Avatar_v2.0.png")
    embed.set_author(name="PapichBot", url="https://github.com/MoRoZoFF228/PapichBot/blob/main/description.md")
    embed.set_footer(text="")

    embed.add_field(name="_ _", value="Вас приветствует бот собственной разработки Papich Bot, разработчиком которого является <@527771957198979073> ")
    embed.add_field(name="О Боте", value="Papich Bot является тестовым ботом, поэтомму он может отличатся от функционала полноценных ботов, таких как: Dungeon Durker, JuniperBot, MEE6 и других ботов. В дальнейшем бот будет переделан и доступен в общий доступ, с возможностью добавления бота на свой сервер")
    embed.add_field(name="Функционал", value="Papich Bot имеет возможность мутить/кикать/банить участников сервера, которые нарушили правила. Имеет систему аудита для Администрации сервера. Также он имеет систему 'Cтатистики Участников', в которой каждый участник сервера может посмотреть 'Карточку Пользователя', в которой будет указано количество сообщений, количество репутации и прочую информацию. В дальнейшем появится так называемые Веселости. ")
    embed.add_field(name="Для справки", value="Если у вас есть какие-то претензии к боту, просьба сообщить об этом в личные сообщения в Дискорде разработчику бота: <@527771957198979073>", inline=True)
    embed.add_field(name="Форма Заполнения", value="Для указания жалобы вам нужно указать: Что вас не устраивает в боте. Для указания Бага вам нужно указать: В чем заключается баг, по возможности прикрепите фото или видеоматериал. Для указания для изменения бота вам нужно указать: Причину, по которой разработчик должен добавить/изменить/удалить ту или иную команду", inline=True)

    await ctx.send(content='_ _', embed=embed)


    embed = discord.Embed(title='_ _', colour=discord.Colour(0xff8500), url="https://discordapp.com", timestamp=ctx.message.created_at)
    embed.set_author(name="", url="https://discordapp.com")
    embed.set_footer(text="Произодство: MoRoZoFF228#2697", icon_url="https://cdn.discordapp.com/attachments/745691018103619724/764170264640225330/unknown.png")

    embed.add_field(name="_ _", value="Префикс Бота `'_'`")
    embed.add_field(name="Команды", value="Вот список доступных команд: `durka` - шуточная командa для вызова дурка. `poisk` - команда для направления человека в канал <#745691592492580965>, если он искал напарника в неправильном канал. `media` - команда для направления человека в канал <#742797730983837727>, если он прислал фото/видеоматериал не по теме разговора. `slaves` - шуточная гачи-команда")
    embed.add_field(name="Команды для Администрации", value="Команды для админов: `Swear` - команда для снижения репутации за мат. `Slap` - команда для снижение репутации, когда для мута еще рано, а по шапке дать уже нужно. Выдается за неадекватное поведение. `obezyannik` - мут на 15 минут. `sizo` - мут на 1 час. `kolonia` - мут на 6 часов.")
    
    await ctx.send(content='_ _', embed=embed)


@bot.command(name = 'swear', aliases = ['свир', 'мат'])
async def swear_command(ctx, member: discord.Member):
    await ctx.send(f"{member.mention} Следи за языком, пожалуйста, системы репутации нет, но в скором появится")
    

@bot.command(name = 'durka', aliases = ['дурка'])
async def durka_command(ctx, members: commands.Greedy[discord.Member]):
    mentions = " ".join(user.mention for user in members)
    await ctx.send(f"Из-за серьёзных бед с башкой, мы должны изолировать {mentions} от здоровых людей. Счет за лечение вышлем по Почте России")
    

@bot.command(name = 'slap', aliases = ['hat', 'шапка'])
async def hat_command(ctx, member: discord.Member):
    await ctx.send(f"Дружище {member.mention}, шапка в порядке?")


@bot.command(name = 'slaves', aliases = ['слава'])
async def slaves_command(ctx):
    await ctx.send(
        '- Алё!'
        '— Да да?'
        '— Ну как там сo :male_sign:slaves:male_sign: ?'
        '— А?— Ну как там с :male_sign:slaves:male_sign:?'
        '— Какими :male_sign:slaves:male_sign: ?'
        '— Чё?'
        '— Куда ты звонишь?'
        '— Тебе звоню.'
        '— Кому?'
        '— Ну тебе.'
        '— Кому тебе?'
        '— А вот тебе вот.'
        '— Ты кто такой?'
        '— :male_sign:Dungeon Master:male_sign:.'
        '— Какой :male_sign:Dungeon Master:male_sign:?'
        '— :male_sign:Fisting is three hundred bucks:male_sign:.'
        '— Такого не знаю, ты ошибся номером, :male_sign:Semen:male_sign:'
        '— Кто?'
        '— Ты.'
        '— Чё с :male_sign:slaves:male_sign: ?'
        '— Какими :male_sign:slaves:male_sign: ?'
        '— Ну которые :male_sign:in my ass:male_sign:'
        '— Куда?'
        '— :male_sign:in my ass:male_sign: вложил'
        '— Ты :male_sign:fucking slaves:male_sign: или кто, сынок?'
        '— Я .. Я :male_sign:Dungeon Master:male_sign:'
        '— Кто такой?'
        '— :male_sign:Master:male_sign:.'
        '— Вот именно, ну и все, :male_sign:Finger in my ass:male_sign:, ёбана в рот.'
        '— Куда... Чьё :male_sign:Ass:male_sign:?'
        '— :male_sign:Finger in my ass:male_sign:,!'
        '— А чё ты кричишь?'
        '— Да ничего!'
        '— Алё!'
        '— Да'
        '— Ну чё там?'
        '— Чего?!')


@bot.command(name = 'poisk', aliases = ['поиск'])
async def poisk_command(ctx, member: discord.Member):
    await ctx.send(f"***ДАННЫЙ КАНАЛ НЕ ДЛЯ ПОИСКА ИГРОКОВ***, {member.mention} пожалуйста, используйте канал <#745691592492580965>")


@bot.command(name = 'media', aliases = ['медиа'])
async def media_command(ctx, member: discord.Member):
    await ctx.send("Фото и прочил медиафайлом не место в этом чате. {member.mention} Пожалуйста, используйте канал <#742797730983837727>")
        

@bot.command(name = 'obezyannik', aliases = ['обезьянник'])
async def obezyannik_command(ctx, member: discord.Member):
    await ctx.send("Система Модерации временно недоступна :sad_cat:")


@bot.command(name = 'kolonia', aliases = ['колония'])
async def kolonia_command(ctx, member: discord.Member):
    await ctx.send("Система Модерации временно недоступна :sad_cat:")

@bot.command(name = 'sizo', aliases = ['сизо'])
async def sizo_command(ctx, member: discord.Member):
    await ctx.send("Система Модерации временно недоступна :sad_cat:")
     




bot.run("NzY3MDgwNjAxNjE0MDI0NzI0.X4stew.aj6SpNppy0_80V052M55YCiYPgo")
