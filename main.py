import configparser

class ConfigParser:
    def __init__(self, filename):
        self.config = configparser.ConfigParser()
        self.filename = filename

    def load_config(self):
        self.config.read(self.filename)

    def get_section(self, section_name):
        return self.config[section_name]

    def get_option(self, section_name, option_name):
        return self.config.get(section_name, option_name)

    def set_option(self, section_name, option_name, value):
        self.config.set(section_name, option_name, value)
        with open(self.filename, 'w') as config_file:
            self.config.write(config_file)

    def delete_option(self, section_name, option_name):
        if option_name in self.get_section(section_name):
            self.config.remove_option(section_name, option_name)
            with open(self.filename, 'w') as config_file:
                self.config.write(config_file)

    def add_section(self, section_name):
        if not self.config.has_section(section_name):
            self.config.add_section(section_name)
            with open(self.filename, 'w') as config_file:
                self.config.write(config_file)

    def delete_section(self, section_name):
        if self.config.has_section(section_name):
            self.config.remove_section(section_name)
            with open(self.filename, 'w') as config_file:
                self.config.write(config_file)

# Misol fayl
config = ConfigParser('config.ini')
config.load_config()

# Yozish
config.add_section('database')
config.set_option('database', 'host', 'localhost')
config.set_option('database', 'port', '5432')
config.set_option('database', 'username', 'admin')
config.set_option('database', 'password', 'password')

# O'qish
print(config.get_option('database', 'host'))  # localhost
print(config.get_option('database', 'port'))  # 5432
print(config.get_option('database', 'username'))  # admin
print(config.get_option('database', 'password'))  # password

# O'zgartirish
config.set_option('database', 'host', '192.168.1.1')
config.set_option('database', 'port', '5433')

# O'qish
print(config.get_option('database', 'host'))  # 192.168.1.1
print(config.get_option('database', 'port'))  # 5433

# Ochirish
config.delete_option('database', 'username')
config.delete_option('database', 'password')

# O'qish
print(config.get_option('database', 'host'))  # 192.168.1.1
print(config.get_option('database', 'port'))  # 5433
print(config.get_option('database', 'username'))  # None
print(config.get_option('database', 'password'))  # None
