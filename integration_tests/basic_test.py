from assertpy import assert_that
from paddock import models
from integration_tests import (
    FAKE_CUSTOMER_ID,
    IRacingIntegrationTest,
)


class TestCarsDriven(IRacingIntegrationTest):

    def test_cars_driven_success(self):
        response = self.paddock.cars_driven(customer_id=404787)

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

    def test_cars_driven_failure(self):
        response = self.paddock.cars_driven(customer_id=FAKE_CUSTOMER_ID)

        # Check model:
        assert_that(response.body()).is_equal_to([])

        # Check raw:
        assert_that(response.status_code).is_equal_to(200)
        assert_that(response.raw.json()).is_equal_to([])


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


class TestAllTracks(IRacingIntegrationTest):

    def test_all_tracks_success(self):
        response = self.paddock.all_tracks()

        # Check model:
        assert_that(response.body()).contains(
            models.TrackConfigurationRecord(
                id=44,
                name="[Legacy] Silverstone Circuit - 2008",
                configuration_name="National",
                max_cars_on_track=81,
                pit_stalls=42,
                grid_stalls=62,
                coordinates="52.0733006,-1.0168574",
                is_dirt=False,
                is_oval=False,
                is_fully_lit=False,
                is_lap_scoring=False,
                latitude=52.0733006,
                longitude=-1.0168574,
                category=models.Category.road,
                configuration_order=5,
                short_parade_lap=True,
                time_zone="Europe/London",
            )
        )

        # # Check raw:
        assert_that(response.status_code).is_equal_to(200)
        assert_that(
            [x for x in response.raw.json() if x["trackid"] == 304][0],
        ).is_equal_to(
            {
                'config_name': 'Rallycross',
                'isdirt': 0,
                'ngridstalls': 16,
                'trackid': 304,
                'timeZoneId': 'America%2FIndiana%2FIndianapolis',
                'latitude': 39.812512,
                'coordinates': '39.8125120%2C-86.3405270',
                'hasShortParadeLap': False,
                'maxcarsontrack': 16,
                'isoval': 0,
                'farmid': 11,
                'fullylit': True,
                'priority': 0,
                'lapscoring': 0,
                'catid': 4,
                'displayname': 'NL-Ams',
                'npitstalls': 7,
                'track_name': 'Lucas+Oil+Raceway',
                'longitude': -86.340527
            }
        )

    def test_all_tracks_failure(self):
        response = self.paddock.all_tracks(farm_id=999_999_999)

        # Check model:
        assert_that(response.body()).is_equal_to([])

        # Check raw:
        assert_that(response.status_code).is_equal_to(200)
        assert_that(response.raw.json()).is_equal_to([])
