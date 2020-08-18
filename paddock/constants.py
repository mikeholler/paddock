# _*_ coding: utf_8 _*_

ALL = -1
NUM_ENTRIES = 25
"""Entries per page. This is the amount set in iRacing site. We shouldn't increase it."""

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

#OTHER
EVENT_TEST = 1
EVENT_PRACTICE = 2
EVENT_QUALY = 3
EVENT_TTRIAL = 4
EVENT_RACE = 5
EVENT_OFFICIAL = 6
EVENT_UNOFFICIAL = 7

#INCIDENT FLAGS
#these are used in the laps data
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

#URLS
URL_IRACING_LOGIN = "https://members.iracing.com/membersite/login.jsp"
URL_IRACING_LOGIN2 = "https://members.iracing.com/membersite/Login"
URL_IRACING_HOME = "https://members.iracing.com/membersite/member/Home.do"
URL_CURRENT_SERIES = "https://members.iracing.com/membersite/member/Series.do"
URL_STATS_CHART = "https://members.iracing.com/memberstats/member/GetChartData?custId=%s&catId=%s&chartType=1"
URL_DRIVER_COUNTS = "https://members.iracing.com/membersite/member/GetDriverCounts"
URL_CAREER_STATS = "https://members.iracing.com/memberstats/member/GetCareerStats?custid=%s"
URL_YEARLY_STATS = "https://members.iracing.com/memberstats/member/GetYearlyStats?custid=%s"
URL_CARS_DRIVEN = "https://members.iracing.com/memberstats/member/GetCarsDriven?custid=%s"
URL_PERSONAL_BEST = "https://members.iracing.com/memberstats/member/GetPersonalBests?carid=%s&custid=%s"
URL_DRIVER_STATUS = "https://members.iracing.com/membersite/member/GetDriverStatus?%s"
URL_DRIVER_STATS = "https://members.iracing.com/memberstats/member/GetDriverStats"
URL_LASTRACE_STATS = "https://members.iracing.com/memberstats/member/GetLastRacesStats?custid=%s"
URL_RESULTS_ARCHIVE = "https://members.iracing.com/memberstats/member/GetResults"
URL_SEASON_STANDINGS = "https://members.iracing.com/memberstats/member/GetSeasonStandings"
URL_SEASON_STANDINGS2 = "https://members.iracing.com/membersite/member/statsseries.jsp"
URL_HOSTED_RESULTS = "https://members.iracing.com/memberstats/member/GetPrivateSessionResults"
URL_SELECT_SERIES = "https://members.iracing.com/membersite/member/SelectSeries.do?&season=%s&view=undefined&nocache=%s"
URL_SESSION_TIMES = "https://members.iracing.com/membersite/member/GetSessionTimes"#T-m-d
URL_SERIES_RACERESULTS = "https://members.iracing.com/memberstats/member/GetSeriesRaceResults"

URL_GET_EVENTRESULTS_CSV = "https://members.iracing.com/membersite/member/GetEventResultsAsCSV?subsessionid=%s&simsesnum=%s&includeSummary=1"
URL_GET_EVENTRESULTS = "https://members.iracing.com/membersite/member/EventResult.do?&subsessionid=%s"

URL_GET_LAPS_SINGLE = "https://members.iracing.com/membersite/member/GetLaps?&subsessionid=%s&groupid=%s&simsessnum=%s"
URL_GET_LAPS_ALL = "https://members.iracing.com/membersite/member/GetLapChart?&subsessionid=%s&carclassid=-1"

URL_GET_PASTSERIES = "https://members.iracing.com/membersite/member/PreviousSeasons.do"

URL_GET_WORLDRECORD = "https://members.iracing.com/memberstats/member/GetWorldRecords?seasonyear=%s&seasonquarter=%s&carid=%s&trackid=%s&custid=%s&format=json&upperbound=1"


#LOCATIONS
LOC_ALL = "null"
