import re


def validate_name(name):
    """
    Regex to check if name of players are write correctly
    """
    pattern = r"^[A-Za-zÀ-ÖØ-öø-ÿ\s'-]+$"
    return re.match(pattern, name)


def is_name_valid(element):
    """
    Function to say to the user if the name is not enter correctly
    """
    while True:
        name = input(element)
        if not validate_name(name):
            print("Le nom saisie n'est pas valide. Veuillez réessayer")
        else:
            return name


def validate_date(date):
    """
    Regex to check if name of players are write correctly
    """
    pattern = r"^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])(?:/[0-9]{4})?$"
    return re.match(pattern, date)


def is_date_valid(element):
    """
    Function to say to the user if the date is not enter correctly
    """
    while True:
        date = input(element)
        if not date or not validate_date(date):
            print("Merci d'entrer la date sur le format jj/mm ou jj/mm/aaaa")
        else:
            return date
