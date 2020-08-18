# _*_ coding: utf_8 _*_

ALL = -1
NUM_ENTRIES = 25
"""
Entries per page.

This is the amount set in iRacing site. We shouldn't increase it.
"""

IRATING_OVAL_CHART = 1
IRATING_ROAD_CHART = 2

RACE_TYPE_OVAL = 1
RACE_TYPE_ROAD = 2

LIC_ROOKIE = 1
LIC_D = 2
LIC_C = 3
LIC_B = 4
LIC_A = 5
LIC_PRO = 6
LIC_PRO_WC = 7

SORT_IRATING = 'irating'
SORT_TIME = 'start_time'
SORT_POINTS = 'points'
ORDER_DESC = 'desc'
ORDER_ASC = 'asc'

# OTHER
EVENT_TEST = 1
EVENT_PRACTICE = 2
EVENT_QUALY = 3
EVENT_TTRIAL = 4
EVENT_RACE = 5
EVENT_OFFICIAL = 6
EVENT_UNOFFICIAL = 7

# INCIDENT FLAGS
# these are used in the laps data
FLAG_PITTED = 2
FLAG_OFF_TRACK = 4
FLAG_BLACK_FLAG = 8
FLAG_CAR_RESET = 16
FLAG_CONTACT = 32
FLAG_CAR_CONTACT = 64
FLAG_LOST_CONTROL = 128
FLAG_DISCONTINUITY = 256
FLAG_INTERPOLATED_CROSSING = 512
FLAG_CLOCK_SMASH = 1024
FLAG_TOW = 2048

INC_FLAGS = {
    0: "clean",
    2: "pitted",
    4: "off track",
    8: "black flag",
    16: "car reset",
    32: "contact",
    64: "car contact",
    128: "lost control",
    256: "discontinuity",
    512: "interpolated crossing",
    1024: "clock smash",
    2048: "tow"
}

URL_BASE = "https://members.iracing.com"
URL_MEMBERSITE_BASE = f"{URL_BASE}/membersite"
URL_MEMBERSTATS_BASE = f"{URL_BASE}/memberstats"

# URLS
URL_IRACING_LOGIN = f"{URL_MEMBERSITE_BASE}/login.jsp"
URL_IRACING_LOGIN2 = f"{URL_MEMBERSITE_BASE}/Login"
URL_IRACING_HOME = f"{URL_MEMBERSITE_BASE}/member/Home.do"
URL_CURRENT_SERIES = f"{URL_MEMBERSITE_BASE}/member/Series.do"
URL_STATS_CHART = f"{URL_MEMBERSTATS_BASE}/member/GetChartData" \
                  f"?custId=%s&catId=%s&chartType=1"
URL_DRIVER_COUNTS = f"{URL_MEMBERSITE_BASE}/member/GetDriverCounts"
URL_CAREER_STATS = f"{URL_MEMBERSTATS_BASE}/member/GetCareerStats?custid=%s"
URL_YEARLY_STATS = f"{URL_MEMBERSTATS_BASE}/member/GetYearlyStats?custid=%s"
URL_CARS_DRIVEN = f"{URL_MEMBERSTATS_BASE}/member/GetCarsDriven?custid=%s"
URL_PERSONAL_BEST = f"{URL_MEMBERSTATS_BASE}/member/GetPersonalBests" \
                    f"?carid=%s&custid=%s"
URL_DRIVER_STATUS = f"{URL_MEMBERSITE_BASE}/member/GetDriverStatus?%s"
URL_DRIVER_STATS = f"{URL_MEMBERSTATS_BASE}/member/GetDriverStats"
URL_LASTRACE_STATS = f"{URL_MEMBERSTATS_BASE}/member/GetLastRacesStats" \
                     f"?custid=%s"
URL_RESULTS_ARCHIVE = f"{URL_MEMBERSTATS_BASE}/member/GetResults"
URL_SEASON_STANDINGS = f"{URL_MEMBERSTATS_BASE}/member/GetSeasonStandings"
URL_SEASON_STANDINGS2 = f"{URL_MEMBERSITE_BASE}/member/statsseries.jsp"
URL_HOSTED_RESULTS = f"{URL_MEMBERSTATS_BASE}/member/GetPrivateSessionResults"
URL_SELECT_SERIES = f"{URL_MEMBERSITE_BASE}/member/SelectSeries.do" \
                    f"?&season=%s&view=undefined&nocache=%s"
URL_SESSION_TIMES = f"{URL_MEMBERSITE_BASE}/member/GetSessionTimes"  # T-m-d
URL_SERIES_RACERESULTS = f"{URL_MEMBERSTATS_BASE}/member/GetSeriesRaceResults"

URL_GET_EVENTRESULTS_CSV = f"{URL_MEMBERSITE_BASE}/member/" \
                           f"GetEventResultsAsCSV" \
                           f"?subsessionid=%s" \
                           f"&simsesnum=%s" \
                           f"&includeSummary=1"
URL_GET_EVENTRESULTS = f"{URL_MEMBERSITE_BASE}/member/EventResult.do" \
                       f"?&subsessionid=%s"

URL_GET_LAPS_SINGLE = f"{URL_MEMBERSITE_BASE}/member/GetLaps" \
                      f"?&subsessionid=%s&groupid=%s&simsessnum=%s"
URL_GET_LAPS_ALL = f"{URL_MEMBERSITE_BASE}/member/GetLapChart" \
                   f"?&subsessionid=%s&carclassid=-1"

URL_GET_PASTSERIES = f"{URL_MEMBERSITE_BASE}/member/PreviousSeasons.do"

URL_GET_WORLDRECORD = "{URL_MEMBERSTATS_BASE}/member/GetWorldRecords" \
                      "?seasonyear=%s&seasonquarter=%s&carid=%s&trackid=%s" \
                      "&custid=%s&format=json&upperbound=1"


# LOCATIONS
LOC_ALL = "null"
