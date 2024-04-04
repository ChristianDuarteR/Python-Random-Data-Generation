from datetime import datetime, timedelta
from src.loadWords import load_words_from_file
import numpy as np


def generate_random_classification(start, end, count):
    """
    Generate a list of random numbers within a specified range.

    Parameters:
    - start (int): The start of the range (inclusive).
    - end (int): The end of the range (inclusive).
    - count (int): The number of random numbers to generate.

    Returns:
    - list: A list of random numbers.
    """
    return [random.randint(start, end) for _ in range(count)]

def generate_random_valid_emails(count, names):
    """
    Generate a list of random valid email addresses.

    Parameters:
    - count (int): The number of random email addresses to generate.

    Returns:
    - list: A list of random valid email addresses.
    """
    domains = ["gmail.com", "yahoo.com", "hotmail.com", "gov.com", "outlook.com"]
    return [f"{random.choice(load_words_from_file(names))}@{random.choice(domains)}" for _ in range(count)]


import random

def generate_random_nameGames(count, themes_file, endings_file):
    """
    Generate a list of random video game names.

    Parameters:
    - count (int): The number of random video game names to generate.

    Returns:
    - list: A list of random video game names.
    """
    themes = load_words_from_file(themes_file)
    endings = load_words_from_file(endings_file)
    game_names = set()
    while len(game_names) < count:
        game_name = f"{random.choice(themes)} {random.choice(endings)}"
        game_names.add(game_name)
    return list(game_names)

def generate_random_date(size):
    """
    Generate a list of random release dates for video games.

    Parameters:
    - size (int): The number of random dates to generate.

    Returns:
    - list: A list of random release dates.
    """
    start_date = datetime(1980, 1, 1)
    end_date = datetime.now()

    random_dates = []
    for _ in range(size):
        random_date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
        random_dates.append(random_date.strftime("%Y-%m-%d"))

    return random_dates

def generate_random_console(size):
    """
    Generate a list of randomly weighted video game console names.

    Parameters:
    - size (int): The number of console names to generate.

    Returns:
    - list: A list of randomly weighted console names.
    """
    consoles_weighted = [
        ("A", ["PlayStation", "Nintendo Switch", "Nintendo 64", "Sega Genesis", "GameCube"]),
        ("B", ["Xbox", "PlayStation 2 (PS2)", "Sega Dreamcast", "Xbox 360"]),
        ("C", ["Sony PlayStation 5 (PS5)", "Xbox Series X", "Super Nintendo Entertainment System (SNES)"]),
        ("D", ["Nintendo Wii", "Sega Saturn", "Atari 2600", "Nintendo Entertainment System (NES)"]),
        ("E", ["Atari Jaguar"])
    ]

    consoles = [console for group in consoles_weighted for console in random.choices(group[1], k=size)]

    return consoles


def generate_random_publishers(size):
    """
    Generate a list of random video game publishers.

    Parameters:
    - size (int): The number of random publishers to generate.

    Returns:
    - list: A list of random video game publishers.
    """
    publishers = [
        "Electronic Arts",
        "Activision",
        "Ubisoft",
        "Square Enix",
        "Take-Two Interactive",
        "Nintendo",
        "Capcom",
        "Bandai Namco Entertainment",
        "Sony Interactive Entertainment",
        "Microsoft Studios",
        "Sega",
        "Bethesda Softworks",
        "CD Projekt",
        "Valve",
        "Epic Games",
        "Konami",
        "Rockstar Games",
        "Tencent Games",
        "Warner Bros. Interactive Entertainment",
        "THQ Nordic"
    ]
    if size > len(publishers):
        publishers *= (size // len(publishers)) + 1

    return random.sample(publishers, size)


def generate_random_developers(size):
    """
    Generate a list of random video game developers.

    Parameters:
    - size (int): The number of random developers to generate.

    Returns:
    - list: A list of random video game developers.
    """
    developers = [
        "Naughty Dog",
        "Infinity Ward",
        "CD Projekt Red",
        "Rockstar North",
        "Nintendo EAD",
        "Epic Games",
        "Bethesda Game Studios",
        "Ubisoft Montreal",
        "Capcom",
        "Blizzard Entertainment",
        "Square Enix",
        "Valve",
        "343 Industries",
        "Bioware",
        "Insomniac Games",
        "Respawn Entertainment",
        "Guerrilla Games",
        "Bungie",
        "Kojima Productions",
        "Gearbox Software"
    ]
    if size > len(developers):
        developers *= (size // len(developers)) + 1

    return random.sample(developers, size)


def generate_random_genres(size):
    """
    Generate a list of randomly weighted video game genres.

    Parameters:
    - size (int): The number of genres to generate.

    Returns:
    - list: A list of randomly weighted video game genres.
    """
    genres_weighted = [
        ("Action-Adventure", ["Action", "Adventure"]),
        ("Role-Playing", ["Role-Playing", "MMORPG"]),
        ("Strategy-Simulation", ["Strategy", "Simulation", "RTS"]),
        ("Sports-Racing", ["Sports", "Racing"]),
        ("Puzzle-Platformer", ["Puzzle", "Platformer"]),
        ("Shooter", ["Shooter"]),
        ("Open World", ["Open World"]),
        ("Survival-Horror", ["Survival", "Horror"]),
        ("Fighting", ["Fighting"]),
        ("MOBA", ["MOBA"]),
        ("Music/Rhythm", ["Music/Rhythm"]),
        ("Educational", ["Educational"]),
        ("Stealth", ["Stealth"])
    ]

    genres = [genre for group in genres_weighted for genre in random.choices(group[1], k=size)]

    return genres


def generate_random_multiplayer(size):
    """
    Generate a list of random multiplayer options for video games.

    Parameters:
    - size (int): The number of random multiplayer options to generate.

    Returns:
    - list: A list of random multiplayer options.
    """
    multiplayer_options = [
        "Local Co-op",
        "Online Co-op",
        "Local Multiplayer",
        "Online Multiplayer",
        "Split Screen",
        "LAN Co-op",
        "LAN Multiplayer",
        "Couch Co-op",
        "Couch Multiplayer",
        "Cross-platform Multiplayer",
        "Competitive Online",
        "Competitive Local",
        "Competitive LAN"
    ]
    if size > len(multiplayer_options):
        multiplayer_options *= (size // len(multiplayer_options)) + 1

    return random.sample(multiplayer_options, size)


def generate_random_online_features(size):
    """
    Generate a list of random online features for video games.

    Parameters:
    - size (int): The number of random online features to generate.

    Returns:
    - list: A list of random online features.
    """
    online_features = [
        "Online Leaderboards",
        "Cross-platform Play",
        "Downloadable Content (DLC)",
        "In-game Purchases",
        "Cloud Saves",
        "Online Chat",
        "Voice Chat",
        "Matchmaking",
        "User-generated Content",
        "Social Media Integration",
        "Streaming Integration",
        "Online Tournaments",
        "Online Events",
        "Season Pass",
        "Live Events",
        "Online Challenges",
        "Server Browser"
    ]
    if size > len(online_features):
        online_features *= (size // len(online_features)) + 1

    return random.sample(online_features, size)


def generate_random_platforms(size):
    """
    Generate a list of randomly weighted platforms for video games.

    Parameters:
    - size (int): The number of platforms to generate.

    Returns:
    - list: A list of randomly weighted platforms for video games.
    """
    platforms_weighted = [
        ("Nintendo", ["Nintendo Switch", "Nintendo 3DS", "Wii U", "Nintendo DS", "Wii", "GameCube", "Game Boy Advance", "Nintendo 64"]),
        ("PlayStation-Xbox", ["PlayStation 5", "Xbox Series X", "PlayStation 4", "Xbox One", "PlayStation 3", "Xbox 360", "PlayStation 2", "Xbox"]),
        ("PC-iOS-Android", ["PC", "iOS", "Android", "PlayStation Vita"])
    ]

    platforms = [platform for group in platforms_weighted for platform in random.choices(group[1], k=size)]

    return platforms


def generate_random_modes(size):
    """
    Generate a list of random modes for video games.

    Parameters:
    - size (int): The number of random modes to generate.

    Returns:
    - list: A list of random modes for video games.
    """
    modes = [
        "Single Player",
        "Multiplayer",
        "Cooperative",
        "Competitive",
        "Online",
        "Offline",
        "Story Mode",
        "Campaign",
        "Survival",
        "Free Play",
        "Challenge Mode",
        "Time Trial",
        "Tutorial",
        "Practice Mode",
        "Custom Mode"
    ]
    if size > len(modes):
        modes *= (size // len(modes)) + 1

    return random.sample(modes, size)
def generate_random_dlc_availability(size):
    """
    Generate a list of random downloadable content (DLC) availability for video games.

    Parameters:
    - size (int): The number of random DLC availability options to generate.

    Returns
     - list: A list of random downloadable content (DLC) availability for video games.
    """

    dlc_availability = [
        "Available",
        "Not Available",
        "Planned",
        "Season Pass",
        "Expansion Pack",
        "Free DLC",
        "Paid DLC"
    ]
    return [random.choice(dlc_availability) for _ in range(size)]


def generate_random_prices(size):
    """
    Generate a list of random prices for video games.

    Parameters:
    - size (int): The number of random prices to generate.

    Returns:
    - list: A list of random prices for video games.
    """
    mean_price = 8
    std_dev = 4

    prices = np.random.normal(loc=mean_price, scale=std_dev, size=size)

    prices = np.clip(prices, 5, 10)

    prices = np.round(prices, decimals=2)

    prices = prices.tolist()

    return prices

def generate_random_metacritic_scores(size):
    """
    Generate a list of random Metacritic scores for video games.

    Parameters:
    - size (int): The number of random Metacritic scores to generate.

    Returns:
    - list: A list of random Metacritic scores for video games.
    """
    return [random.randint(0, 100) for _ in range(size)]


def generate_random_esrb_content_ratings(size):
    """
    Generate a list of random ESRB content ratings for video games.

    Parameters:
    - size (int): The number of random ESRB content ratings to generate.

    Returns:
    - list: A list of random ESRB content ratings for video games.
    """
    esrb_content_ratings = [
        "Early Childhood",
        "Everyone",
        "Everyone 10+",
        "Teen",
        "Mature",
        "Adults Only"
    ]
    return [random.choice(esrb_content_ratings) for _ in range(size)]


def generate_random_system_requirements(size):
    """
    Generate a list of random system requirements for video games.

    Parameters:
    - size (int): The number of random system requirements to generate.

    Returns:
    - list: A list of random system requirements for video games.
    """
    system_requirements = [
        "Minimum: Windows 10, Intel Core i5, 8 GB RAM, NVIDIA GeForce GTX 1060, 50 GB storage",
        "Recommended: Windows 11, Intel Core i7, 16 GB RAM, NVIDIA GeForce RTX 3060, 100 GB storage",
        "Minimum: macOS Catalina, Intel Core i3, 8 GB RAM, AMD Radeon RX 570, 50 GB storage",
        "Recommended: macOS Monterey, Apple M1 chip, 16 GB RAM, AMD Radeon Pro 5600M, 100 GB storage",
        "Minimum: Ubuntu 20.04 LTS, AMD Ryzen 5, 8 GB RAM, AMD Radeon RX 580, 50 GB storage",
        "Recommended: Ubuntu 22.04 LTS, AMD Ryzen 7, 16 GB RAM, NVIDIA GeForce RTX 3070, 100 GB storage"
    ]
    if size > len(system_requirements):
        system_requirements *= (size // len(system_requirements)) + 1

    return random.sample(system_requirements, size)


def generate_random_physical_releases(size):
    """
    Generate a list of random physical release information for video games.

    Parameters:
    - size (int): The number of random physical releases to generate.

    Returns:
    - list: A list of random physical release information for video games.
    """
    physical_releases = [
        "Standard Edition",
        "Collector's Edition",
        "Limited Edition",
        "Steelbook Edition",
        "Special Edition",
        "Game of the Year Edition",
        "Ultimate Edition",
        "Day One Edition",
        "Definitive Edition",
        "Anniversary Edition",
        "Complete Edition",
        "Enhanced Edition",
        "Platinum Hits",
        "Gold Edition",
        "Premium Edition",
        "Signature Edition"
    ]
    if size > len(physical_releases):
        physical_releases *= (size // len(physical_releases)) + 1

    return random.sample(physical_releases, size)


def generate_random_awards(size):
    """
    Generate a list of random awards for video games.

    Parameters:
    - size (int): The number of random awards to generate.

    Returns:
    - list: A list of random awards for video games.
    """
    awards = [
        "Game of the Year",
        "Best Action Game",
        "Best Adventure Game",
        "Best RPG",
        "Best Strategy Game",
        "Best Sports Game",
        "Best Racing Game",
        "Best Fighting Game",
        "Best Multiplayer Game",
        "Best Indie Game",
        "Best Narrative",
        "Best Visuals",
        "Best Soundtrack",
        "Best Performance",
        "Best Direction",
        "Best Game Design",
        "Best Innovation",
        "Fan Favorite",
        "Most Anticipated"
    ]
    if size > len(awards):
        awards *= (size // len(awards)) + 1

    return random.sample(awards, size)