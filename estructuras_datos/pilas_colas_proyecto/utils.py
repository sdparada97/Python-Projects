from concertclasses.client import Client
from concertclasses.ticket import Ticket
from concertclasses.concert import Concert

from colorama import Fore, Style
import time

CONCERTS = []
CLIENTS = []


def create_new_concert():
    """
    The create_new_concert function creates a new concert object and appends it to the CONCERTS list.

    Args:

    Returns:
        Nothing
    """
    CONCERTS.append(
        Concert(input(f"{Fore.BLUE}Escriba el nombre del concierto: {Style.RESET_ALL}"))
    )
    print(f"{Fore.GREEN}CONCIERTO CREADO CON EXITO... {Style.RESET_ALL}")


def create_new_client():
    """
    The create_new_client function creates a new client object and appends it to the CLIENTS list.


    Args:

    Returns:
        Nothing
    """
    CLIENTS.append(
        Client(
            input(f"{Fore.BLUE}Escriba el nombre del cliente: {Style.RESET_ALL}"),
            input(f"{Fore.BLUE}Escriba el telefono del cliente: {Style.RESET_ALL}"),
        )
    )
    print(f"{Fore.GREEN}CLIENTE CREADO CON EXITO... {Style.RESET_ALL}")


def buy_ticket():
    """
    The buy_ticket function allows a user to select a client and then
    select a concert. The selected client will be added to the list of clients
    attending the selected concert.

    Args:

    Returns:
        A tuple with the concert and client selected
    """
    for count, client in enumerate(CLIENTS):
        if isinstance(client, Client):
            print(f"{Fore.BLUE}{count}) {client.user_name} {Style.RESET_ALL}")
    client_selected = input(
        f"{Fore.BLUE}Seleccione uno de los conciertos:{Style.RESET_ALL}"
    )

    for count, concert in enumerate(CONCERTS):
        if isinstance(concert, Concert):
            print(f"{Fore.BLUE}{count}) {concert.name} {Style.RESET_ALL}")
    concert_pos = input(
        f"{Fore.BLUE}Seleccione uno de los conciertos:{Style.RESET_ALL}"
    )

    CONCERTS[int(concert_pos) - 1].buy_ticket(CLIENTS[int(client_selected) - 1])


def simulate_concert():
    """
    The simulate_concert function simulates a concert.
        It prints the name of the concert, then enters people into it,
        and finally gives way to them.


    Args:

    Returns:
        A list of concerts
    """
    for concert in CONCERTS:
        print(f"{Fore.RED}{concert.name}{Style.RESET_ALL}")
        if isinstance(concert, Concert):
            concert.enter_paid_concert()

            print(f"{Fore.RED}EN VIVO: {concert.name}{Style.RESET_ALL}")
            time.sleep(3)

            concert.give_way_people()

            print(f"{Fore.RED}CONCIERTO CERRADO !! {concert.name}{Style.RESET_ALL}")
            time.sleep(3)
