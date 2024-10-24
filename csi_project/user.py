import enum
import uuid

class user_type(enum.Enum):
    DEFAULT = 0
    EDUCATOR = 1
    STUDENT = 2
    ADMIN = 3

class user():
    def __init__(self) -> None:
        self.id: uuid.UUID


        self.type : user_type = user_type.DEFAULT
        self.first_name: str = ""
        self.last_name: str = ""

    def set_type(self, type : user_type):
        self.type = type

    