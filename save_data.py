import os
import datetime
import shutil

class SaveData:
    _instance = None

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = SaveData()
        return cls._instance

    def __init__(self):
        self.filename = ""
        self.buffer = bytearray()
        self.adventure = 0

    def open(self, filename):
        if not os.path.exists(filename):
            return False
        with open(filename, "rb") as f:
            self.buffer = bytearray(f.read())
        self.filename = filename
        self.backup()
        return True

    def save(self):
        if not self.filename or not self.buffer:
            return False
        with open(self.filename, "wb") as f:
            f.write(self.buffer)
        return True

    def save_as(self, filename):
        if not self.filename or not self.buffer:
            return False
        self.filename = filename
        return self.save()

    def backup(self):
        now_str = datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")
        backup_dir = os.path.join(os.path.dirname(self.filename), "backup")
        if not os.path.exists(backup_dir):
            os.makedirs(backup_dir)
        backup_path = os.path.join(backup_dir, f"{now_str} {os.path.basename(self.filename)}")
        shutil.copy2(self.filename, backup_path)

    def calc_address(self, address):
        return address + self.adventure

    def read_number(self, address, size):
        if not self.buffer:
            return 0
        address = self.calc_address(address)
        if address + size > len(self.buffer):
            return 0
        result = 0
        for i in range(size):
            result += self.buffer[address + i] << (i * 8)
        return result

    def write_number(self, address, size, value):
        if not self.buffer:
            return
        address = self.calc_address(address)
        if address + size > len(self.buffer):
            return
        for i in range(size):
            self.buffer[address + i] = value & 0xFF
            value >>= 8

    def read_text(self, address, size):
        if not self.buffer:
            return ""
        address = self.calc_address(address)
        if address + size > len(self.buffer):
            return ""
        tmp = bytearray()
        for i in range(size):
            b = self.buffer[address + i]
            if b == 0:
                break
            tmp.append(b)
        return tmp.decode('utf-8', errors='ignore').strip('\0')

    def write_text(self, address, size, value):
        if not self.buffer:
            return
        address = self.calc_address(address)
        if address + size > len(self.buffer):
            return
        encoded = value.encode('utf-8')
        for i in range(size):
            if i < len(encoded):
                self.buffer[address + i] = encoded[i]
            else:
                self.buffer[address + i] = 0
