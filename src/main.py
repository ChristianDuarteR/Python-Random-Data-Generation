import datagenerator
import csv
from VideoGame import VideoGame

if __name__ == "__main__":
    size = 2000000

    classifications = datagenerator.generate_random_classification(1, 10, size)
    emails = datagenerator.generate_random_valid_emails(size, '../files/dictionary.txt')
    names = datagenerator.generate_random_nameGames(size, '../files/themes.txt', '../files/middle.txt', '../files/endings.txt')
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
        game = VideoGame(names[i], classifications[i], emails[i], date[i], consoles[i],
                         publishers[i], developers[i], genres[i], multiplayer_options[i],
                         online_features[i], platforms[i], modes[i],
                         dlc_availability[i], prices[i], metacritic_scores[i],
                         esrb_content_ratings[i], system_requirements[i],
                         physical_releases[i], awards[i])
        games.append(game)

    with open('video_games_info.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['ID', 'Name', 'Classification per User', 'Provider Email', 'Date of Release', 'Consoles', 'Owners',
                      'Developers', 'Genres', 'Multiplayer Options', 'Online Features', 'Platforms',
                      'Modes', 'DLC Availability', 'Prices in dollars', 'Metacritic Scores', 'ESRB Content Ratings',
                      'System Requirements', 'Physical Releases', 'Awards']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for idx, game in enumerate(games, start=1):
            writer.writerow({'ID': idx,
                             'Name': game.title,
                             'Classification per User': game.classification,
                             'Provider Email': game.email_provider,
                             'Date of Release': game.release_date,
                             'Consoles': game.console,
                             'Owners': game.publisher,
                             'Developers': game.developer,
                             'Genres': game.genre,
                             'Multiplayer Options': game.multiplayer,
                             'Online Features': game.online_features,
                             'Platforms': game.platform,
                             'Modes': game.modes,
                             'DLC Availability': game.dlc_available,
                             'Prices in dollars': game.price,
                             'Metacritic Scores': game.metacritic_score,
                             'ESRB Content Ratings': game.esrb_content_rating,
                             'System Requirements': game.system_requirements,
                             'Physical Releases': game.physical_release,
                             'Awards': game.awards})

    print("CSV file 'video_games_info.csv' has been generated successfully.")