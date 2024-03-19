import datagenerator
from VideoGame import VideoGame

if __name__ == "__main__":
    size = 10

    classifications = datagenerator.generate_random_classification(1, 10, size)
    emails = datagenerator.generate_random_valid_emails(size, '../files/dictionary.txt')
    names = datagenerator.generate_random_nameGames(size, '../files/themes.txt', '../files/endings.txt')
    apto = datagenerator.generate_random_to(size)
    date = datagenerator.generate_random_date(size)
    consoles = datagenerator.generate_random_console(size)
    publishers = datagenerator.generate_random_publishers(size)
    developers = datagenerator.generate_random_developers(size)
    genres = datagenerator.generate_random_genres(size)
    multiplayer_options = datagenerator.generate_random_multiplayer(size)
    online_features = datagenerator.generate_random_online_features(size)
    platforms = datagenerator.generate_random_platforms(size)
    modes = datagenerator.generate_random_modes(size)
    dlc_availability = datagenerator.generate_random_dlc_availability(size)
    prices = datagenerator.generate_random_prices(size)
    metacritic_scores = datagenerator.generate_random_metacritic_scores(size)
    esrb_content_ratings = datagenerator.generate_random_esrb_content_ratings(size)
    system_requirements = datagenerator.generate_random_system_requirements(size)
    physical_releases = datagenerator.generate_random_physical_releases(size)
    awards = datagenerator.generate_random_awards(size)

    games = []
    for i in range(size):
        game = VideoGame(names[i], classifications[i], emails[i], apto[i], date[i], consoles[i],
                         publishers[i], developers[i], genres[i], multiplayer_options[i],
                         online_features[i], platforms[i], modes[i],
                         dlc_availability[i], prices[i], metacritic_scores[i],
                         esrb_content_ratings[i], system_requirements[i],
                         physical_releases[i], awards[i])
        games.append(game)

    for game in games:
        print(game)

    # Escribir la información de los juegos en un archivo de texto
    with open('video_games_info.txt', 'w') as file:
        for game in games:
            file.write(str(game) + '\n')
