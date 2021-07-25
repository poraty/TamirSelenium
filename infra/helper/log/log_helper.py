import datetime
import logging

log_levels = {"CRITICAL": logging.CRITICAL,
              "FATAL": logging.FATAL,
              "ERROR": logging.ERROR,
              "WARNING": logging.WARNING,
              "WARN": logging.WARN,
              "INFO": logging.INFO,
              "DEBUG": logging.DEBUG,
              "NOTSET": logging.NOTSET,
              }


def create_log_file(request, init_configs):
    current_time_formatted = datetime.datetime.now().strftime(init_configs["start_time_format"])
    file_name = f"{request.node.name}__{current_time_formatted}"
    formatter = logging.Formatter(init_configs["logging_format"]
                                  , datefmt=init_configs["date_format"])

    file_handler_1 = logging.FileHandler(f'{file_name}.log')
    file_handler_1.setFormatter(formatter)
    file_logger = logging.getLogger(init_configs["default_log_name"])
    file_logger.addHandler(file_handler_1)
    file_logger.setLevel(log_levels[init_configs["log_level"].upper()])


def delete_log_file_handler():
    logging.getLogger('File_Log').handlers = []
