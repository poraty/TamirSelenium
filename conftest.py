import pytest
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from definitions import CONFIG_FILES, CHROME_DRIVER_PATH
import json
import logging
import datetime
from enum import Enum
import infra.helper.log.log_helper as log_helper

configuration: dict

log_levels = {"CRITICAL": logging.CRITICAL,
              "FATAL": logging.FATAL,
              "ERROR": logging.ERROR,
              "WARNING": logging.WARNING,
              "WARN": logging.WARN,
              "INFO": logging.INFO,
              "DEBUG": logging.DEBUG,
              "NOTSET": logging.NOTSET,
              }

# log_levels.setdefault(key, default=None)

class CONFIG_LOG_LEVEL(Enum):
    CRITICAL = 50,
    FATAL = CRITICAL,
    ERROR = 40,
    WARNING = 30,
    WARN = WARNING,
    INFO = 20,
    DEBUG = 10,
    NOTSET = 0

    @staticmethod
    def get_level_from_string(level_name: str) -> Enum:
        for level in CONFIG_LOG_LEVEL:
            if level_name == level:
                return level


@pytest.fixture(scope="session")
def init_configs() -> dict:
    # configuration: dict = {}
    # global configuration
    with open(file=CONFIG_FILES, mode="r") as file:
        configuration = json.load(fp=file)
    return configuration


# def get_configuration_value(key: str) -> str:
#     global configuration
#     if configuration is None:
#         configuration = init_configs()
#
#     return configuration[key]


@pytest.fixture(scope="function")
def handle_web_driver(request):
    driver = get_web_driver()
    yield driver
    close_web_driver(driver)


def get_web_driver() -> webdriver:
    opts = ChromeOptions()
    # This will not close the browser at the end of the test
    opts.add_experimental_option("detach", True)

    return webdriver.Chrome(executable_path=CHROME_DRIVER_PATH, chrome_options=opts)

    # opts = ChromeOptions()
    # opts.add_experimental_option("detach", True)
    # driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH, chrome_options=opts)
    # driver.get("https://www.youtube.com/")


def close_web_driver(driver: webdriver):
    pass
    # driver.quit()


@pytest.fixture(scope="function")
def init_log(request, init_configs) -> logging.Logger:
    # init_log_levels_dict()
    print(f"At setup the test name is {request.node.name}")
    log_helper.create_log_file(request, init_configs)
    # logging.getLogger(f'File_Log_{request.node.name}').info(f"At setup the test name is: {request.node.name}")
    logging.getLogger('File_Log').info(f"At setup the test name is: {request.node.name}")
    return logging.getLogger('File_Log')

# def init_log_levels_dict() -> dict:
#     global log_levels
#     if log_levels is not None or log_levels is not {}:
#         return log_levels
#
#     # CRITICAL = 50,
#     #     FATAL = CRITICAL,
#     #     ERROR = 40,
#     #     WARNING = 30,
#     #     WARN = WARNING,
#     #     INFO = 20,
#     #     DEBUG = 10,
#     #     NOTSET = 0
#     log_levels = {"CRITICAL": logging.CRITICAL,
#                   "FATAL": logging.FATAL,
#                   "ERROR": logging.ERROR,
#                   "WARNING": logging.WARNING,
#                   "WARN": logging.WARN,
#                   "INFO": logging.INFO,
#                   "DEBUG": logging.DEBUG,
#                   "NOTSET": logging.NOTSET,
#                   }


def create_log_file(request, init_configs):
    current_time_formatted = datetime.datetime.now().strftime(init_configs["start_time_format"])
    # current_time_formatted = datetime.datetime.now().strftime("%y_%m_%d-%H_%M_%S")
    file_name = f"{request.node.name}__{current_time_formatted}"
    formatter = logging.Formatter(init_configs["logging_format"]
                                  , datefmt=init_configs["date_format"])
    # formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(funcName)s Line No_%(lineno)d %(message)s'
    #                               , datefmt="%Y_%m_%d %H_%M_%S")
    file_handler_1 = logging.FileHandler(f'{file_name}.log')
    file_handler_1.setFormatter(formatter)
    # file_logger = logging.getLogger(f'File_Log_{request.node.name}')
    file_logger = logging.getLogger(init_configs["default_log_name"])
    # file_logger = logging.getLogger('File_Log')
    file_logger.addHandler(file_handler_1)
    # CONFIG_LOG_LEVEL.get_level_from_string(get_configuration_value("log_level"))

    log_levels.get("", )
    file_logger.setLevel(log_levels[init_configs["log_level"].upper()])
    # file_logger.setLevel(CONFIG_LOG_LEVEL.get_level_from_string(get_configuration_value("log_level")).value)
    # file_logger.setLevel(logging.DEBUG)


def delete_log_file_handler():
    logging.getLogger('File_Log').handlers = []
