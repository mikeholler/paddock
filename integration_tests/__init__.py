import logging
import os
import sys
import unittest

from paddock._client import Paddock


__all__ = [
    "IRacingIntegrationTest",
    "IRACING_USERNAME",
    "IRACING_PASSWORD",
    "FAKE_CUSTOMER_ID",
]

here = os.path.abspath(os.path.dirname(__file__))

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
FAKE_CUSTOMER_ID = 999_999_999


class IRacingIntegrationTest(unittest.TestCase):
    """
    Test service that runs against iRacing's server.
    """

    def setUp(self) -> None:
        self.paddock = Paddock(
            username=IRACING_USERNAME,
            password=IRACING_PASSWORD,
            cookie_file=os.path.join(here, "integration_test-cookies.pickle")
        )

    def tearDown(self) -> None:
        self.paddock.close()
