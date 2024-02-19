import configparser

config_file_path = 'config/app.properties'
PROPERTIES = {}


def initialize_parser(path):
    """
    It initializes the parser with the file present at path
    :param path: location of the app.properties file
    :return: the RawConfigParser
    """

    config = configparser.RawConfigParser()
    print(f'Reading Configuration file present in {path}')
    config.read(path)
    return config


def parse_config_file(config):
    """
    This function is used to parse the config file and
    :param config: the initialised RawConfigParser
    :return: properties as a dictionary
    """
    sections = config.sections()
    print(f'SECTIONS :: {sections}')

    cities = config.get('app', 'cities').split(' ')
    database_mysql_host = config.get('app', 'database.mysql.host')
    database_mysql_username = config.get('app', 'database.mysql.username')
    database_mysql_password = config.get('app', 'database.mysql.password')
    api_openweathermap_key = config.get('app', 'api.openweathermap.key')

    print(f'\n-------------------------------------'
          f'\n--------Configuration Loaded---------'
          f'\n-------------------------------------'
          f'\ncities: {cities}'
          f'\ndatabase_mysql_host: {database_mysql_host}'
          f'\ndatabase_mysql_username: {database_mysql_username}'
          f'\ndatabase_mysql_password: {database_mysql_password}'
          f'\napi_openweathermap_key: {api_openweathermap_key}')

    # create a dictionary for the properties
    global PROPERTIES
    PROPERTIES = {
        'cities': cities,
        'database_mysql_host': database_mysql_host,
        'database_mysql_username': database_mysql_username,
        'database_mysql_password': database_mysql_password,
        'api_openweathermap_key': api_openweathermap_key
    }

    return PROPERTIES


config_parser = initialize_parser(config_file_path)
parse_config_file(config_parser)
