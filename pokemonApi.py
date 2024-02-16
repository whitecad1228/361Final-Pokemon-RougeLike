import requests
import json

if __name__ == '__main__':


    api_url = "https://pokeapi.co/api/v2/pokemon?limit=251"
    response = requests.get(api_url)
    data = response.json()
    print(data["results"])
    pokemonList = []
    for urls in data["results"]:
        api_url = urls["url"]
        response = requests.get(api_url)
        data = response.json()
        moves = []
        for val in data["moves"]:
            #print(val["version_group_details"][0]["move_learn_method"]["name"])
            #print(val["version_group_details"][0]["level_learned_at"])
            if val["version_group_details"][0]["move_learn_method"]["name"] == "level-up":
                dict = {}
                dict["name"] = val["move"]["name"]
                dict["level"] = val["version_group_details"][0]["level_learned_at"]
                moves.append(dict)
        print(moves)
        print(data["id"])

        pokemon = {}
        pokemon["name"] = data["name"]
        pokemon["id"] = data["id"]
        pokemon["moves"] = moves
        pokemonList.append(pokemon)
    with open('movesByLevel.json', 'w', encoding='utf-8') as f:
        json.dump(pokemonList, f, ensure_ascii=False, indent=4)








    # print(data["moves"])
    # print(type(data["moves"]))
    # print(data["moves"][0])
    # print(type(data["moves"][0]))
    # print(data["moves"][0]["move"])
    # print(data["moves"][0]["move"]["name"])
    # print(type(response))
    # print(type(data))
    # print(data)

    # file = open("moveByLevel.json", "w")
    # file.write(json)
    # file.close()