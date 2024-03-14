from datetime import datetime, timedelta

from src.loadWords import load_words_from_file


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

def generate_random_to(size):
    """
    Generate a random age rating for a video game.

    Parameters:
    - size (int): The number of age ratings to generate.

    Returns:
    - list: A list of random age ratings for video games.
    """
    age_ratings = ["Para todo público", "10+", "13+", "16+", "18+"]
    return [random.choice(age_ratings) for _ in range(size)]


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
    Generate a list of random video game console names.

    Parameters:
    - size (int): The number of random console names to generate.

    Returns:
    - list: A list of random console names.
    """
    consoles = [
        "PlayStation",
        "Xbox",
        "Nintendo Switch",
        "Sega Dreamcast",
        "Atari Jaguar",
        "Super Nintendo Entertainment System (SNES)",
        "Sony PlayStation 5 (PS5)",
        "Nintendo 64",
        "Sega Genesis",
        "Xbox Series X",
        "GameCube",
        "PlayStation 2 (PS2)",
        "Xbox 360",
        "Nintendo Wii",
        "Sega Saturn",
        "Atari 2600",
        "Nintendo Entertainment System (NES)"
    ]

    return random.sample(consoles, size)