from assertpy import assert_that
from integration_tests import IRacingIntegrationTest


class BasicTest(IRacingIntegrationTest):

    def test_career_stats(self):
        results = self.client.cars_driven(custid=404787)
        assert_that(results).contains(
            1, 13, 23, 24, 25, 36, 41, 44, 67, 72, 79, 88, 99, 100, 101, 103,
            106, 109, 112, 113, 117, 119, 120, 121,
        )

        results = self.client.cars_driven(custid=404787)
        assert_that(results).contains(
            1, 13, 23, 24, 25, 36, 41, 44, 67, 72, 79, 88, 99, 100, 101, 103,
            106, 109, 112, 113, 117, 119, 120, 121,
        )

    def test_all_laps(self):
        results = self.client.event_laps_all(subsession=33938036)
