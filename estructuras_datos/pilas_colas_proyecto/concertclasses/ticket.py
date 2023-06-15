from uuid import uuid4, UUID


class Ticket:
    def __init__(self, concert: UUID):
        self.id = uuid4()
        self.concert = concert
        self.status = True
