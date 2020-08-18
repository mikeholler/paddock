from assertpy import assert_that
from integration_tests import (
    FAKE_CUSTOMER_ID,
    IRacingIntegrationTest,
)


class BasicTest(IRacingIntegrationTest):

    def test_career_stats_success(self):
        response = self.paddock.cars_driven(custid=404787)

        # Check model:
        assert_that(response.body()).contains(
            1, 13, 23, 24, 25, 36, 41, 44, 67, 72, 79, 88, 99, 100, 101, 103,
            106, 109, 112, 113, 117, 119, 120, 121,
        )

        # Check raw:
        assert_that(response.status_code).is_equal_to(200)
        assert_that(response.raw.json()).contains(
            1, 13, 23, 24, 25, 36, 41, 44, 67, 72, 79, 88, 99, 100, 101, 103,
            106, 109, 112, 113, 117, 119, 120, 121,
        )

    def test_career_stats_failure(self):
        response = self.paddock.cars_driven(custid=FAKE_CUSTOMER_ID)

        # Check model:
        assert_that(response.body()).is_equal_to([])

        # Check raw:
        assert_that(response.status_code).is_equal_to(200)
        assert_that(response.raw.json()).is_equal_to([])
