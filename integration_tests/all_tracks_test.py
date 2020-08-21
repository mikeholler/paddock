from assertpy import assert_that
from paddock import models
from integration_tests import (
    IRacingIntegrationTest,
)


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
                raw_category=models.Category.road.value,
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
