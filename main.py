import requests
from bs4 import BeautifulSoup
from discord.ext import commands
from googlesearch import search


headers = {
        "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36"}


def bot_anime(anime, site):
    for resultado in search(f'"{anime}" {site}', stop=1):
        animelink = resultado
        return animelink


def anime_scrap_score_mal(link):
    global headers
    site = requests.get(link, headers=headers)
    soup = BeautifulSoup(site.content, 'html.parser')

    animescore = soup.find('div', class_='fl-l score').get_text()
    animename = soup.find('h1', class_='title-name h1_bold_none').get_text()
    return f"a nota de {animename} é: {animescore}"


def anime_scrap_score_al(link):
    global headers
    site = requests.get(link, headers=headers)
    soup = BeautifulSoup(site.content, 'html.parser')

    animescore = soup.find('div', class_='el-tooltip data-set').get_text()
    animename = soup.find('h1', class_='title-name h1_bold_none').get_text()
    return f"a nota de {animename} é: {animescore}"


def anime_scrap_eps_mal(link):
    global headers
    site = requests.get(link, headers=headers)
    soup = BeautifulSoup(site.content, 'html.parser')

    animeeps = soup.find('span', id='curEps').get_text()
    animename = soup.find('h1', class_='title-name h1_bold_none').get_text()
    return f"O anime {animename} tem {animeeps} episódio(s)!"


def anime_scrap_studio_mal(link):
    global headers
    site = requests.get(link, headers=headers)
    soup = BeautifulSoup(site.content, 'html.parser')

    animestudio = soup.find('span', class_='information studio author').get_text()
    animename = soup.find('h1', class_='title-name h1_bold_none').get_text()
    return f"O anime {animename} foi feito pelo estúdio {animestudio}!"


def anime_scrap_season_mal(link):
    global headers
    site = requests.get(link, headers=headers)
    soup = BeautifulSoup(site.content, 'html.parser')

    animeseason = soup.find('span', class_='information season').get_text()
    animename = soup.find('h1', class_='title-name h1_bold_none').get_text()
    return f"O anime {animename} veio na temporada {animeseason}!"


def anime_scrap_synopsis_mal(link):
    global headers
    site = requests.get(link, headers=headers)
    soup = BeautifulSoup(site.content, 'html.parser')

    animesin = soup.find('p', itemprop='description').get_text()
    animename = soup.find('h1', class_='title-name h1_bold_none').get_text()
    return f"Sinopse de {animename}:\n{animesin}"


bot = commands.Bot("!")


@bot.event
async def on_ready():
    print("I'm Ready!")


@bot.command(name="score")
async def anime_score(ctx, expression, *expression2):
    link = bot_anime(str(expression2), expression)

    score = anime_scrap_score_mal(link)

    await ctx.send(score)


@bot.command(name="eps")
async def anime_eps(ctx, expression, *expression2):
    link = bot_anime(str(expression2), expression)

    eps = anime_scrap_eps_mal(link)

    await ctx.send(eps)


@bot.command(name="studio")
async def anime_studio(ctx, expression, *expression2):
    link = bot_anime(str(expression2), expression)

    studio = anime_scrap_studio_mal(link)

    await ctx.send(studio)


@bot.command(name="season")
async def anime_studio(ctx, expression, *expression2):
    link = bot_anime(str(expression2), expression)

    studio = anime_scrap_season_mal(link)

    await ctx.send(studio)


@bot.command(name="sinopse")
async def anime_synopsis(ctx, expression, *expression2):
    link = bot_anime(str(expression2), expression)

    studio = anime_scrap_synopsis_mal(link)

    await ctx.send(studio)


@bot.command(name="link")
async def anime_link(ctx, expression, *expression2):
    link = bot_anime(str(expression2), expression)

    await ctx.send(link)


@bot.command(name="bothelp")
async def bot_help(ctx):
    instructions = """
    _Como usar o AniScore Bot:_
    ! + comando + site de pesquisa (myanimelist ou anilist) + nome do anime (o bot aceita erros ortográficos  e siglas)
    
    _Lista de comandos do AniScore:_
    
    !score
    _Pega a nota do anime em questão no site que você escolheu_
    
    !eps
    _Pega a quantidade de episódios do anime (animes sem número máximo de episódios aparecerão com '?')_
    
    !studio
    _Pega o principal estúdio que produziu a animação do anime_
    
    !season
    _Pega a temporada e o ano de lançamento do anime_
    
    !sinopse
    _Pega a sinopse do anime disponível no site que você escolheu (apenas em inglês por hora)_
    
    ## aviso ##
    O AniScore bot só funciona com o MyAnimeList por hora
    """

    await ctx.send(instructions)


bot.run(token)
