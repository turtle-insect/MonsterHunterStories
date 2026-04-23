from save_data import SaveData

class Util:
    @staticmethod
    def write_number(address, size, min_val, max_val, value):
        value = max(min_val, min(max_val, value))
        SaveData.instance().write_number(address, size, value)
