import unittest

from pathlib import Path

from paddock import Paddock

from assertpy import assert_that
from integration_tests import (
    IRACING_USERNAME,
    IRACING_PASSWORD,
)


class SessionPersistenceTest(unittest.TestCase):

    def setUp(self) -> None:
        self.cookie_file = Path("cookies.pickle")

    def tearDown(self) -> None:
        self.cookie_file.unlink(missing_ok=True)

    def test_recover_session_from_file(self):
        with Paddock(
            username=IRACING_USERNAME,
            password=IRACING_PASSWORD,
            cookie_file=self.cookie_file,
        ) as paddock1:
            assert_that(paddock1.cars_driven(custid=404787)).contains(
                1, 13, 23, 24, 25, 36, 41, 44, 67, 72, 79, 88, 99, 100, 101, 103,
                106, 109, 112, 113, 117, 119, 120, 121,
            )

        with Paddock(
            username=IRACING_USERNAME,
            password=IRACING_PASSWORD,
            cookie_file=self.cookie_file,
        ) as paddock2:
            assert_that(paddock2.cars_driven(custid=404787)).contains(
                1, 13, 23, 24, 25, 36, 41, 44, 67, 72, 79, 88, 99, 100, 101, 103,
                106, 109, 112, 113, 117, 119, 120, 121,
            )
