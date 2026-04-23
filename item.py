from save_data import SaveData
from util import Util

class Item:
    def __init__(self, address):
        self.address = address

    @property
    def id(self):
        return SaveData.instance().read_number(self.address, 2)

    @property
    def count(self):
        return SaveData.instance().read_number(self.address + 2, 2)

    @count.setter
    def count(self, value):
        Util.write_number(self.address + 2, 2, 0, 999, value)
