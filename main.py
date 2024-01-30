import random
import string


def generate_random_numbers(start, end, count):
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


def generate_random_strings(size, alphabet, count):
    """
    Generate a list of random strings of a specified size and alphabet.

    Parameters:
    - size (int): The size of each random string.
    - alphabet (str): The set of characters to choose from.
    - count (int): The number of random strings to generate.

    Returns:
    - list: A list
    """
    return [''.join(random.choice(alphabet) for _ in range(size)) for _ in range(count)]


def generate_random_strings_from_dictionary(dictionary, count):
    """
    Generate a list of random strings by choosing from a dictionary file.

    Parameters:
    - dictionary (str): The path to the dictionary file.
    - count (int): The number of random strings to generate.

    Returns:
    - list: A list of random strings.
    """
    with open(dictionary, 'r') as file:
        words = file.read().splitlines()
    return random.sample(words, count)


def generate_random_sets_of_ids(start, end, set_size, num_sets):
    """
    Generate random sets of IDs within a specified interval.

    Parameters:
    - start (int): The start of the ID range (inclusive).
    - end (int): The end of the ID range (inclusive).
    - set_size (int): The size of each random set of IDs.
    - num_sets (int): The number of random sets to generate.

    Returns:
    - list: A list of sets, each containing random IDs.
    """
    return [{random.randint(start, end) for _ in range(set_size)} for _ in range(num_sets)]


def generate_random_valid_emails(count):
    """
    Generate a list of random valid email addresses.

    Parameters:
    - count (int): The number of random email addresses to generate.

    Returns:
    - list: A list of random valid email addresses.
    """
    domains = ["gmail.com", "yahoo.com", "hotmail.com", "example.com"]
    return [f"{generate_random_string(8, string.ascii_lowercase)}@{random.choice(domains)}" for _ in range(count)]


def generate_random_colombian_addresses(count):
    """
    Generate a list of random Colombian addresses.

    Parameters:
    - count (int): The number of random addresses to generate.

    Returns:
    - list: A list of random Colombian addresses.
    """
    cities = ["Bogotá", "Medellín", "Cali", "Cartagena"]
    streets = ["Calle Principal", "Avenida Central", "Carrera Secundaria", "Diagonal Norte"]
    return [f"{random.randint(100, 999)}, {random.choice(streets)}, {random.choice(cities)}" for _ in range(count)]


# Additional helper function
def generate_random_string(size, alphabet):
    """
    Generate a random string of a specified size and alphabet.

    Parameters:
    - size (int): The size of the random string.
    - alphabet (str): The set of characters to choose from.

    Returns:
    - str: A random string.
    """
    return ''.join(random.choice(alphabet) for _ in range(size))


if __name__ == "__main__":
    # Examples of usage
    numbers = generate_random_numbers(1, 100, 5)
    print("Random Numbers:", numbers)

    alphabet = string.ascii_lowercase
    strings = generate_random_strings(8, alphabet, 5)
    print("Random Strings:", strings)

    dictionary_file = 'dictionary.txt'  # Replace with the name of your dictionary file
    dictionary_strings = generate_random_strings_from_dictionary(dictionary_file, 3)
    print("Random Strings from Dictionary:", dictionary_strings)

    sets_of_ids = generate_random_sets_of_ids(1000, 9999, 3, 2)
    print("Random Sets of IDs:", sets_of_ids)

    emails = generate_random_valid_emails(3)
    print("Random Valid Email Addresses:", emails)

    colombian_addresses = generate_random_colombian_addresses(2)
    print("Random Colombian Addresses:", colombian_addresses)
