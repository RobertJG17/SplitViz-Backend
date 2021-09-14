import requests
import pandas as pd

from temp import camelSplitter


class Splitgate:

    # SECTION: Properties
    raw_stats = None
    refined_stats = None


    # SECTION: METHODS
    def __init__(self, platform, pid, api_key):
        self.platform = platform
        self.pid = pid
        self.api_key = api_key

    def fetch_stats(self):
        req = requests.get(
            url='https://public-api.tracker.gg/v2/splitgate/standard/profile/{}/{}/segments/overview'.format(
                self.platform,
                self.pid
            ),

            headers={
                "TRN-Api-Key": "{}".format(self.api_key)
            }
        )

        try:
            self.raw_stats = req.json()["data"][0]["stats"]
        except KeyError:
            print("INVALID USERNAME-PLATFORM QUERY")


    def format_stats(self):

        if self.raw_stats is  None:
            return

        temp_ser = pd.Series(
            index=[key for key in sorted(self.raw_stats.keys())],
            data=[self.raw_stats[key]["value"] for key in sorted(self.raw_stats.keys())]
        )

        temp_ser.index = pd.Series(data=temp_ser.index).apply(camelSplitter).values
        temp_ser = temp_ser.rename({"Kd": "K/D", "Kad": "K/A/D"})


        self.refined_stats = temp_ser.to_dict()



