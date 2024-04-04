class VideoGame:
    def __init__(self, title, classification, email_provider,
                 release_date, console, publisher,
                 developer, genre, multiplayer, online_features,
                 platform, modes, dlc_available,
                 price, metacritic_score, esrb_content_rating,
                 system_requirements, physical_release, awards):
        """
        Constructor for the VideoGame class.

        Parameters:
        - title (str): The title of the video game.
        - classification (str): The classification given by users.
        - email_provider (str): The email provider.
        - suitable_for (str): The age suitability classification.
        - release_date (str): The release date of the video game.
        - console (str): The console on which the video game is played.
        - publisher (str): The company that published the game.
        - developer (str): The studio that developed the game.
        - genre (str): The genre of the game.
        - multiplayer (bool): Whether the game has multiplayer features.
        - online_features (str): Describes online features of the game.
        - rating (str): The rating of the game (e.g., ESRB, PEGI).
        - platform (str): The specific platform the game is available on.
        - modes (str): The available game modes.
        - dlc_available (bool): Whether DLC is available for the game.
        - price (float): The price of the game.
        - metacritic_score (int): The Metacritic score of the game.
        - esrb_content_rating (str): Specific content contributing to the ESRB rating.
        - system_requirements (str): System requirements for the game.
        - physical_release (bool): Whether the game had a physical release.
        - awards (str): Any awards or recognition the game received.
        """
        self.title = title
        self.classification = classification
        self.email_provider = email_provider
        self.release_date = release_date
        self.console = console
        self.publisher = publisher
        self.developer = developer
        self.genre = genre
        self.multiplayer = multiplayer
        self.online_features = online_features
        self.platform = platform
        self.modes = modes
        self.dlc_available = dlc_available
        self.price = price
        self.metacritic_score = metacritic_score
        self.esrb_content_rating = esrb_content_rating
        self.system_requirements = system_requirements
        self.physical_release = physical_release
        self.awards = awards

    def __str__(self):
        """
        String representation of the VideoGame object.

        Returns:
        - str: String representation of the VideoGame object.
        """
        return f"Title: {self.title}, Classification: {self.classification}, Email Provider: {self.email_provider}, Suitable For: {self.suitable_for}, Release Date: {self.release_date}, Console: {self.console}, Publisher: {self.publisher}, Developer: {self.developer}, Genre: {self.genre}, Multiplayer: {self.multiplayer}, Online Features: {self.online_features}, Platform: {self.platform}, Modes: {self.modes}, DLC Available: {self.dlc_available}, Price: {self.price}, Metacritic Score: {self.metacritic_score}, ESRB Content Rating: {self.esrb_content_rating}, System Requirements: {self.system_requirements}, Physical Release: {self.physical_release}, Awards: {self.awards}"

    def write_to_file(self, filename):
        """
        Write the information of the VideoGame object to a text file.

        Parameters:
        - filename (str): The name of the file to write to.
        """
        with open(filename, 'a') as file:
            file.write(f"Title: {self.title}\n")
            file.write(f"Classification: {self.classification}\n")
            file.write(f"Email Provider: {self.email_provider}\n")
            file.write(f"Suitable For: {self.suitable_for}\n")
            file.write(f"Release Date: {self.release_date}\n")
            file.write(f"Console: {self.console}\n")
            file.write(f"Publisher: {self.publisher}\n")
            file.write(f"Developer: {self.developer}\n")
            file.write(f"Genre: {self.genre}\n")
            file.write(f"Multiplayer: {self.multiplayer}\n")
            file.write(f"Online Features: {self.online_features}\n")
            file.write(f"Platform: {self.platform}\n")
            file.write(f"Modes: {self.modes}\n")
            file.write(f"DLC Available: {self.dlc_available}\n")
            file.write(f"Price: {self.price}\n")
            file.write(f"Metacritic Score: {self.metacritic_score}\n")
            file.write(f"ESRB Content Rating: {self.esrb_content_rating}\n")
            file.write(f"System Requirements: {self.system_requirements}\n")
            file.write(f"Physical Release: {self.physical_release}\n")
            file.write(f"Awards: {self.awards}\n")

