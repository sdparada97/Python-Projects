from .ticket import Ticket

from typing import Type, List
from uuid import uuid4
from collections import deque


class Client:
    def __init__(self, user_name: str, phone: str) -> None:
        self.id = uuid4()
        self.user_name = user_name
        self.phone = phone
        self.tickets_purchase: deque = deque()
