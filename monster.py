from save_data import SaveData
from util import Util

class Monster:
    def __init__(self, address):
        self.address = address

    @property
    def name(self):
        return SaveData.instance().read_text(self.address, 30)
    
    @name.setter
    def name(self, value):
        SaveData.instance().write_text(self.address, 30, value)

    @property
    def id(self):
        return SaveData.instance().read_number(self.address + 60, 2)

    @id.setter
    def id(self, value):
        SaveData.instance().write_number(self.address + 60, 2, value)

    @property
    def lv(self):
        return SaveData.instance().read_number(self.address + 104, 1)

    @lv.setter
    def lv(self, value):
        Util.write_number(self.address + 104, 1, 1, 99, value)

    @property
    def hp_plus(self):
        return SaveData.instance().read_number(self.address + 228, 1)

    @hp_plus.setter
    def hp_plus(self, value):
        SaveData.instance().write_number(self.address + 228, 1, value)

    @property
    def attack_plus(self):
        return SaveData.instance().read_number(self.address + 229, 1)

    @attack_plus.setter
    def attack_plus(self, value):
        SaveData.instance().write_number(self.address + 229, 1, value)

    @property
    def defense_plus(self):
        return SaveData.instance().read_number(self.address + 230, 1)

    @defense_plus.setter
    def defense_plus(self, value):
        SaveData.instance().write_number(self.address + 230, 1, value)
