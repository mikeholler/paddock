from assertpy import assert_that
from paddock import models
from integration_tests import (
    IRacingIntegrationTest,
)


class TestAllCars(IRacingIntegrationTest):

    def test_all_cars_success(self):
        response = self.paddock.all_cars()

        # Check model:
        assert_that(response.body()).contains(
            models.CarRecord(id=31, name="Modified - NASCAR Whelen Tour"),
            models.CarRecord(id=36, name="Street Stock"),
            models.CarRecord(
                id=58,
                name="[Legacy] NASCAR Xfinity Chevrolet Camaro - 2014"
            ),
        )

        # # Check raw:
        assert_that(response.status_code).is_equal_to(200)
        assert_that(response.raw.json()).contains(
            {
                "carid": 31,
                "car_name": "Modified+-+NASCAR+Whelen+Tour",
                "displayname": "NL-Ams",
                "farmid": 11,
            },
            {
                "carid": 36,
                "car_name": "Street+Stock",
                "displayname": "NL-Ams",
                "farmid": 11,
            },
            {
                "carid": 58,
                "car_name":
                    "%5BLegacy%5D+NASCAR+Xfinity+Chevrolet+Camaro+-+2014",
                "displayname": "NL-Ams",
                "farmid": 11,
            },
        )

    def test_all_cars_failure(self):
        response = self.paddock.all_cars(farm_id=999_999_999)

        # Check model:
        assert_that(response.body()).is_equal_to([])

        # Check raw:
        assert_that(response.status_code).is_equal_to(200)
        assert_that(response.raw.json()).is_equal_to([])
