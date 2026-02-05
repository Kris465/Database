from loguru import logger

from view import view


def controller():
    user_input = ""
    while user_input != 2:
        user_input = view()
        logger.info(f"Пользователь ввел {user_input}")
