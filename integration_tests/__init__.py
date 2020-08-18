import logging
import os
import sys
import unittest

from paddock._client import Paddock


__all__ = [
    "IRacingIntegrationTest",
    "IRACING_USERNAME",
    "IRACING_PASSWORD",
]

logging.basicConfig(
    stream=sys.stdout,
    level=logging.INFO,
    datefmt="%Y-%m-%dT%H:%M:%S%Z",
    format="%(asctime)s [%(levelname)s] -- %(message)s"
)


def get_required_env(key: str) -> str:
    """
    Get an environment variable's value, raising an exception if it isn't set.
    """
    value = os.getenv(key)
    if value is None:
        raise EnvironmentError(
            f"Must set {key} environment variable to to run integration tests."
        )
    return value


IRACING_USERNAME = get_required_env("IRACING_USERNAME")
IRACING_PASSWORD = get_required_env("IRACING_PASSWORD")

# We create a singleton client that we use for all tests to avoid constantly
# re-authenticating. iRacing may see constant re-authentication as suspicious
# activity, we see the disadvantages of 1) using a singleton and 2) sharing
# state between tests are outweighed by being good citizens to the iRacing
# platform.
client = Paddock(
    username=IRACING_USERNAME,
    password=IRACING_PASSWORD,
)


class IRacingIntegrationTest(unittest.TestCase):
    """
    Test service that runs against iRacing's server.
    """

    def setUp(self) -> None:
        self.client = client
