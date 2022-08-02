"""Demo DAO."""
import os
import datetime
from util.logger_utility import LoggerUtility
from util.redis_utility import RedisUtility
from util.common_constants import Constants, EnvironmentVariables


class DemoDao():
    """Demo DAO."""

    def __init__(self, body):
        """Class constructor."""
        self.__body = body

    def info(self):
        """Info User."""
        try:
            user_name = self.__body.get('username')
            message = self.__body.get('message')
            current_now = datetime.datetime.now()
            return (
                f"Hi {user_name}.My name is Ramit.  Here is your message: {message}. The time of your message ==>"
                + current_now.strftime("%Y-%m-%d %H:%M")
            )

        except Exception as exception:
            LoggerUtility.log_error(exception)
            raise Exception(exception)

    def favorite_shows(self):
        """favorite_shows for ramit."""
        try:
            return (
                "Here is the list of My Favorite Shows: "
                + "BBT, "
                + "Young Sheldon,"
                + " Suits"
            )

        except Exception as exception:
            LoggerUtility.log_error(exception)
            raise Exception(exception)
