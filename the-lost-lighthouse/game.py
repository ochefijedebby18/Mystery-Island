def new_game(name):
    return {
        "name": name,
        "location": "Beach",
        "energy": 5,
        "inventory": [],
        "game_over": False,
        "won": False
    }


LOCATIONS = {
    "Beach": ["Jungle"],
    "Jungle": ["Beach", "Cave"],
    "Cave": ["Jungle", "Old Bridge"],
    "Old Bridge": ["Cave", "Lighthouse"],
    "Lighthouse": ["Old Bridge"]
}


ITEMS = {
    "Beach": "rope",
    "Jungle": "lantern"
}


def show_inventory(player):
    return player["inventory"].copy()


def available_actions(player):
    """Return possible destinations."""
    return LOCATIONS[player["location"]].copy()


def move_player(player, destination):
    if player["game_over"]:
        return False

    current = player["location"]

    if destination not in LOCATIONS[current]:
        return False

    if current == "Cave" and destination == "Old Bridge":
        if "rope" not in player["inventory"]:
            return False

    if current == "Old Bridge" and destination == "Lighthouse":
        if "rope" not in player["inventory"]:
            return False

    player["energy"] -= 1

    if player["energy"] <= 0:
        player["energy"] = 0
        player["game_over"] = True
        player["won"] = False
        return True

    player["location"] = destination

    return True


def collect_item(player):
    if player["game_over"]:
        return False

    location = player["location"]

    if location not in ITEMS:
        return False

    item = ITEMS[location]

    if item in player["inventory"]:
        return False

    player["inventory"].append(item)
    return True


def light_lighthouse(player):
    if player["game_over"]:
        return False

    if player["location"] != "Lighthouse":
        return False

    if "lantern" not in player["inventory"]:
        return False

    if player["energy"] <= 0:
        return False

    player["won"] = True
    player["game_over"] = True

    return True


def is_win(player):
    return player["won"]


def is_loss(player):
    return player["game_over"] and not player["won"]
