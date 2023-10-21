import os
from datetime import datetime
import requests

GITHUB_GRAPHQL_ENDPOINT = os.environ['GRAPHQL_ENDPOINT']
TOKEN = os.environ['PROFILE_READ_TOKEN']

START_YEAR = 2017

CONTRIBUTION_GRAPHQL_QUERY = """
query($fromYear: DateTime, $toYear: DateTime) {
	user(login: "TC4Y-777") {
		contributionsCollection(from: $fromYear, to: $toYear) {
			contributionCalendar {
				totalContributions
			}
		}
	}
}
"""

HEADERS = {"Authorization": "Bearer %s" % TOKEN}


def entireTotalContributions() -> int:
    currentYear = datetime.now().year
    totalContribs = 0
    for year in range(START_YEAR, currentYear):
        totalContribs = totalContribs + annualTotalContributions(year)
    return totalContribs


def annualTotalContributions(year: int) -> int:
    fromYear = "%s-01-01T23:05:23Z" % str(year + 1)
    toYear = "%s-01-01T23:05:23Z" % str(year + 2)
    variables = {'fromYear': fromYear, 'toYear': toYear}
    response = requests.post(url=GITHUB_GRAPHQL_ENDPOINT,
                             json={'query': CONTRIBUTION_GRAPHQL_QUERY,
                                   'variables': variables},
                             headers=HEADERS)
    return response.json()["data"]["user"]["contributionsCollection"]["contributionCalendar"]["totalContributions"]


def main():
    totalContributions = entireTotalContributions()
    print(totalContributions)


main()
