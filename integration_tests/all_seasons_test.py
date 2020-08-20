from assertpy import assert_that
from paddock import models
from integration_tests import (
    IRacingIntegrationTest,
)


class TestAllSeasons(IRacingIntegrationTest):

    def test_all_seasons_complete_success(self):
        response = self.paddock.all_seasons(only_active=False)

        # Check model:
        response.body()
        # assert_that(response.body()).contains(
        #     models.CarRecord(id=31, name="Modified - NASCAR Whelen Tour"),
        #     models.CarRecord(id=36, name="Street Stock"),
        #     models.CarRecord(
        #         id=58,
        #         name="[Legacy] NASCAR Xfinity Chevrolet Camaro - 2014"
        #     ),
        # )

        # # Check raw:
        assert_that(response.status_code).is_equal_to(200)

        # This is a week 13 series. You can tell from the fact it has 7 weeks,
        # which amounts to one per day and the name "13th Week..."
        assert_that(response.raw.json()).contains(
            {
                'serieslicgroupid': 1,
                'year': 2020,
                'start': 1591056000000,
                'active': False,
                'islite': False,
                'seriesid': 382,
                'seasonid': 2903,
                'seriesshortname': '13th+Week+2x4+Off+Road+Trucks',
                'end': 1591660800000,
                'category': 4,
                'raceweek': 7,
                'quarter': 2,
                'licenseEligible': True,
                'catid': 4,
                'carclasses': [
                    {
                        'relspeed': 51,
                        'lowername': 'pro+2+truck',
                        'custid': 0,
                        'name': 'Pro+2+Truck',
                        'max_dry_tire_sets': 0,
                        'carsinclass': [
                            {
                                'name': 'Lucas+Oil+Off+Road+Pro+2+Truck',
                                'id': 104
                            }
                        ],
                        'id': 1277,
                        'shortname': 'Pro+2+Truck'
                    },
                    {
                        'relspeed': 53,
                        'lowername': 'pro+4+truck',
                        'custid': 0,
                        'name': 'Pro+4+Truck',
                        'max_dry_tire_sets': 0,
                        'carsinclass': [
                            {
                                'name': 'Lucas+Oil+Off+Road+Pro+4+Truck',
                                'id': 107
                            }
                        ],
                        'id': 1278,
                        'shortname': 'Pro+4+Truck'
                    }
                ],
                'tracks': [
                    {
                        'lowername': 'wild+horse+pass+motorsports+park',
                        'name': 'Wild+Horse+Pass+Motorsports+Park',
                        'id': 334,
                        # TODO: What is pkgid?
                        'pkgid': 279,
                        'priority': 0,
                        'raceweek': 0,
                        'config': '',
                        'timeOfDay': 9
                    },
                    {
                        'lowername': 'wild+west+motorsports+park',
                        'name': 'Wild+West+Motorsports+Park',
                        'id': 332,
                        'pkgid': 276,
                        'priority': 0,
                        'raceweek': 1,
                        'config': '',
                        'timeOfDay': 9
                    },
                    {
                        'lowername': 'wild+horse+pass+motorsports+park',
                        'name': 'Wild+Horse+Pass+Motorsports+Park',
                        'id': 334,
                        'pkgid': 279,
                        'priority': 0,
                        'raceweek': 2,
                        'config': '',
                        'timeOfDay': 0
                    },
                    {
                        'lowername': 'wild+west+motorsports+park',
                        'name': 'Wild+West+Motorsports+Park',
                        'id': 332,
                        'pkgid': 276,
                        'priority': 0,
                        'raceweek': 3,
                        'config': '',
                        'timeOfDay': 0
                    },
                    {
                        'lowername': 'wild+horse+pass+motorsports+park',
                        'name': 'Wild+Horse+Pass+Motorsports+Park',
                        'id': 334,
                        'pkgid': 279,
                        'priority': 0,
                        'raceweek': 4,
                        'config': '',
                        'timeOfDay': 1
                    },
                    {
                        'lowername': 'wild+west+motorsports+park',
                        'name': 'Wild+West+Motorsports+Park',
                        'id': 332,
                        'pkgid': 276,
                        'priority': 0,
                        'raceweek': 5,
                        'config': '',
                        'timeOfDay': 1
                    },
                    {
                        'lowername': 'wild+horse+pass+motorsports+park',
                        'name': 'Wild+Horse+Pass+Motorsports+Park',
                        'id': 334,
                        'pkgid': 279,
                        'priority': 0,
                        'raceweek': 6,
                        'config': '',
                        'timeOfDay': 0
                    }
                ],
                'cars': [
                    {
                        'lowername': 'lucas+oil+off+road+pro+2+truck',
                        'name': 'Lucas+Oil+Off+Road+Pro+2+Truck',
                        'id': 104,
                        # TODO: What is this?
                        'pkgid': 284,
                        # TODO: What is this?
                        'sku': 10450
                    },
                    {
                        'lowername': 'lucas+oil+off+road+pro+4+truck',
                        'name': 'Lucas+Oil+Off+Road+Pro+4+Truck',
                        'id': 107,
                        'pkgid': 284,
                        'sku': 10450
                    }
                ],
            }
        )

        # This is the iRacing Endurance Series, which takes place across the
        # usual season boundaries.
        assert_that(response.raw.json()).contains(
            {
                'serieslicgroupid': 3,
                'year': 2020,
                'start': 1586822400000,
                'active': True,
                'islite': False,
                'seriesid': 408,
                'seasonid': 2814,
                'seriesshortname': 'iRacing+Endurance+Series',
                'end': 1602979200000,
                'category': 2,
                'raceweek': 4,
                'quarter': 2,
                'carclasses': [
                    {
                        'relspeed': 49,
                        'lowername': 'porsche+718+cayman+gt4+clubsport+mr',
                        'custid': 0,
                        'name': 'Porsche+718+Cayman+GT4+Clubsport+MR',
                        'max_dry_tire_sets': 0,
                        'carsinclass': [
                            {
                                'name': 'Porsche+718+Cayman+GT4+Clubsport+MR',
                                'id': 119
                            }
                        ],
                        'id': 1860, 'shortname': 'Porsche+718'
                    },
                    {
                        'relspeed': 70,
                        'lowername': 'gte+class+2',
                        'custid': 0,
                        'name': 'GTE+Class+2',
                        'max_dry_tire_sets': 0,
                        'carsinclass': [
                            {'name': 'Porsche+911+RSR', 'id': 102},
                            {'name': 'BMW+M8+GTE', 'id': 109}
                        ],
                        'id': 2040,
                        'shortname': 'GTE+Class+2'
                    },
                    {
                        'relspeed': 52,
                        'lowername': 'gt3+class+2',
                        'custid': 0,
                        'name': 'GT3+Class+2',
                        'max_dry_tire_sets': 0,
                        'carsinclass': [
                            {'name': 'Mercedes+AMG+GT3', 'id': 72},
                            {'name': 'Ferrari+488+GT3', 'id': 94}
                        ],
                        'id': 2041,
                        'shortname': 'GT3+Class+2'
                    },
                    {
                        'relspeed': 45,
                        'lowername': 'audi+rs+3+lms',
                        'custid': 0,
                        'name': 'Audi+RS+3+LMS',
                        'max_dry_tire_sets': 0,
                        'carsinclass': [
                            {'name': 'Audi+RS+3+LMS', 'id': 112}
                        ],
                        'id': 1450,
                        'shortname': 'Audi+RS+3+LMS'
                    }
                ],
                'tracks': [
                    {
                        'lowername': 'suzuka+international+racing+course',
                        'name': 'Suzuka+International+Racing+Course',
                        'id': 168,
                        'pkgid': 114,
                        'priority': 0,
                        'raceweek': 0,
                        'config': 'Grand+Prix',
                        'timeOfDay': 5
                    },
                    {
                        'lowername': 'silverstone+circuit',
                        'name': 'Silverstone+Circuit',
                        'id': 341,
                        'pkgid': 282,
                        'priority': 1,
                        'raceweek': 1,
                        'config': 'Grand+Prix',
                        'timeOfDay': 5
                    },
                    {
                        'lowername': 'circuit+de+barcelona+catalunya',
                        'name': 'Circuit+de+Barcelona+Catalunya',
                        'id': 345,
                        'pkgid': 292,
                        'priority': 0,
                        'raceweek': 2,
                        'config': 'Grand+Prix',
                        'timeOfDay': 5
                    },
                    {
                        'lowername': 'circuit+of+the+americas',
                        'name': 'Circuit+of+the+Americas',
                        'id': 229,
                        'pkgid': 154,
                        'priority': 0,
                        'raceweek': 3,
                        'config': 'Grand+Prix',
                        'timeOfDay': 5
                    }
                ],
                'licenseEligible': True,
                'catid': 2,
                'cars': [
                    {
                        'lowername': 'porsche+718+cayman+gt4+clubsport+mr',
                        'name': 'Porsche+718+Cayman+GT4+Clubsport+MR',
                        'id': 119,
                        'pkgid': 309,
                        'sku': 10473
                    },
                    {
                        'lowername': 'porsche+911+rsr',
                        'name': 'Porsche+911+RSR',
                        'id': 102,
                        'pkgid': 263,
                        'sku': 10445
                    },
                    {
                        'lowername': 'bmw+m8+gte',
                        'name': 'BMW+M8+GTE',
                        'id': 109,
                        'pkgid': 281,
                        'sku': 10457
                    },
                    {
                        'lowername': 'mercedes+amg+gt3',
                        'name': 'Mercedes+AMG+GT3',
                        'id': 72,
                        'pkgid': 199,
                        'sku': 10404
                    },
                    {
                        'lowername': 'ferrari+488+gt3',
                        'name': 'Ferrari+488+GT3',
                        'id': 94,
                        'pkgid': 244,
                        'sku': 10432
                    },
                    {
                        'lowername': 'audi+rs+3+lms',
                        'name': 'Audi+RS+3+LMS',
                        'id': 112,
                        'pkgid': 291,
                        'sku': 10461
                    }
                ],
            }
        )
