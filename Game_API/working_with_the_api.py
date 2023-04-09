import requests
from Game_API import home_API


def search_game(query, flag=False):
    params = {"search": query}
    response = home_API.home_api(params=params)
    if response.status_code == 200:
        games = response.json()["results"]

        for game in games:
            if flag == False:
                yield '{name}'.format(name=game["name"], id=game["id"])
            else:
                yield game["id"]
    else:
        return "Данной игры не существует."


def all_about_game(name):
    first_id = next(search_game(query=name, flag=True))
    response = home_API.home_api(id=str(first_id))
    if response.status_code == 200:
        games = response.json()
        print(games)
        return '{name} - {rating}\n{background_image}'.format(name=games["name"], rating=games["rating"],
                                           background_image=games["background_image"])
