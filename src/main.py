import datagenerator
from src.VideoGame import VideoGame

if __name__ == "__main__":
    size = 5

    classifications = datagenerator.generate_random_classification(1, 10, size)
    emails = datagenerator.generate_random_valid_emails(size, '../files/dictionary.txt')
    names = datagenerator.generate_random_nameGames(size, '../files/themes.txt', '../files/endings.txt')
    apto = datagenerator.generate_random_to(size)
    date = datagenerator.generate_random_date(size)
    consoles = datagenerator.generate_random_console(size)

    games = []
    for i in range(size):
        game = VideoGame(names[i], classifications[i], emails[i], apto[i], date[i], consoles[i])
        games.append(game)

    for game in games:
        print(game)

