import configparser

def get_properties():
    config = configparser.ConfigParser()
    with open("gilgabot.ini") as props:
        config.read_string(props.read())
        return config