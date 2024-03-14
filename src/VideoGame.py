class VideoGame:
    def __init__(self, title, classification, email_provider, suitable_for, release_date, console):

        self.title = title
        self.classification = classification
        self.email_provider = email_provider
        self.suitable_for = suitable_for
        self.release_date = release_date
        self.console = console

    def __str__(self):
        """
        String representation of the VideoGame object.

        Returns:
        - str: String representation of the VideoGame object.
        """
        return f"Title: {self.title}, Classification: {self.classification}, Email Provider: {self.email_provider}, Suitable For: {self.suitable_for}, Release Date: {self.release_date}, Console: {self.console}"