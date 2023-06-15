import utils

from colorama import Fore, Style

options = {
    "1": (
        "Crear concierto",
        utils.create_new_concert,
    ),
    "2": (
        "Crear cliente",
        utils.create_new_client,
    ),
    "3": (
        "Comprar ticket",
        utils.buy_ticket,
    ),
    "4": (
        "Emular concierto (Entrada - Salida)",
        utils.simulate_concert,
    ),
    "5": ("Salida", exit),
}


def show_menu(options):
    """
    The show_menu function takes a dictionary of options as an argument.
    The keys are the numbers that will be displayed to the user, and the values
    are tuples containing two elements: (0) The text to display for each option,
    and (2) A function that is called when this option is selected by the user.

    Args:
        options: Show the options of the menu

    Returns:
        The key of the selected option
    """
    print(f"{Fore.BLUE}Selecciona una opcion: {Style.RESET_ALL}")
    for key in sorted(options):
        print(f"{Fore.BLUE}{key}){Style.RESET_ALL} {options[key][0]}")


def execute_option(options, option):
    """
    The execute_option function takes two arguments:
        options - a dictionary of option names and their associated functions.
        option - the name of an option in the options dictionary.

    Args:
        options: Pass the dictionary of options to the function
        option: Determine which option to execute

    Returns:
        None
    """
    options[option][1]()


def read_option(options):
    """
    The read_option function takes a list of options and prompts the user to select one.
    It will keep prompting until the user selects an option from the list.


    Args:
        options: Validate the user input

    Returns:
        A string
    """
    while (
        option := input(
            f"{Fore.BLUE}Seleccione alguna de las opciones: {Style.RESET_ALL}"
        )
    ) not in options:
        print(f"{Fore.RED}Opcion Incorrecta, vuelve a intentarlo{Style.RESET_ALL}")
    return option


def generate_menu(options, exit):
    """
    The generate_menu function takes two arguments:
        options - a list of tuples containing the menu options and their functions.
        exit - an integer representing the index of the option to be used as an exit condition.


    Args:
        options: Pass the list of options to the function
        exit: Determine when the user wants to exit the program

    Returns:
        The value of the option variable
    """
    option = None
    while option != exit:
        show_menu(options)
        option = read_option(options)
        execute_option(options, option)
        print()


def exit():
    print(f"{Fore.YELLOW}Saliendo...")


if __name__ == "__main__":
    generate_menu(options, "5")
