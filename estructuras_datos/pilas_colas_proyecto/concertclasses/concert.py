from .client import Client
from .ticket import Ticket

from colorama import Fore, Style
from uuid import uuid4
from collections import deque


class Concert:
    MAX_PUBLIC = 10

    def __init__(self, name: str):
        self.id = uuid4()
        self.name = name
        self.purchasers_ticket: deque = deque(maxlen=self.MAX_PUBLIC)
        self.spectators: deque = deque(maxlen=self.MAX_PUBLIC)
        self.status = True

    def buy_ticket(self, client: Client):
        """
        The buy_ticket function allows a client to buy a ticket for the concert.
            If there are no more tickets available, it will print an error message.
            Otherwise, it will add the client to the list of purchasers and create
            a new ticket with its id.

        Args:
            self: Access the attributes and methods of the class in python
            client: Client: Check if the client is an instance of client class

        Returns:
            A ticket, so the client should be able to access it
        """
        new_ticket = Ticket(self.id)

        if len(self.purchasers_ticket) == self.MAX_PUBLIC:
            print(
                f"{Fore.RED}AGOTADAS LAS ENTRADAS PARA EL CONCIERTO !!{Style.RESET_ALL}"
            )
            return

        if isinstance(client, Client):
            self.purchasers_ticket.append(client)
            client.tickets_purchase.append(new_ticket)

        print(f"{Fore.GREEN}COMPRA REALIZADA CON EXITO !!{Style.RESET_ALL}")

    def enter_paid_concert(self):
        """
        The enter_paid_concert function is responsible for moving the purchasers_ticket list to the spectators list.
        It does this by iterating through each purchaser in purchasers_ticket and appending them to spectators, then removing them from purchasers_ticket.

        Args:
            self: Access the attributes and methods of a class

        Returns:
            None
        """
        for purchaser in self.purchasers_ticket:
            ticket = next(
                (
                    ticket
                    for ticket in purchaser.tickets_purchase
                    if ticket.concert == self.id
                ),
                None,
            )
            if ticket.status == True:
                print(f"{Fore.CYAN}ENTRANDO: {Style.RESET_ALL}{purchaser.user_name}")
                self.spectators.append(purchaser)

        self.purchasers_ticket.clear()

    def give_way_people(self):
        """
        The give_way_people function is used to give way people from the concert.
            It will print a message with the name of the spectator and change his ticket status to False

        Args:
            self: Refer to the object itself

        Returns:
            None
        """

        for spectator in self.spectators:
            print(f"{Fore.CYAN}SALIENDO: {Style.RESET_ALL}{spectator.user_name}")
            ticket = next(
                (
                    ticket
                    for ticket in spectator.tickets_purchase
                    if ticket.concert == self.id
                ),
                None,
            )
            ticket.status = False

        self.spectators.clear()
