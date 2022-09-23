"""Fetch the latest exchange rates available from the Open Exchange Rates API.
Examples
--------
To be written
"""

import os

import requests
import boto3

OPEN_EXCHANGE_API_URL = "https://openexchangerates.org/api/"


class OpenExchangeRatesApiFetcher:
    def __init__(self) -> None:
        self._base_url = OPEN_EXCHANGE_API_URL
        self._auth = os.environ["APP_ID"]

    def call_api(self, method: str, url: str) -> dict:
        """make a call to the API
        Parameters
        ----------
        method : str
            http method
        url : str
            url to call
        Returns
        -------
        dict
            json payload as dict
        Raises
        ------
        requests.HTTPError
            below 400 response
        """
        response = requests.request(method=method, url=url)
        response.raise_for_status()
        return response.json()

    def get_current_exchange(self) -> dict:
        """Get the latest exchange rates available from the Open Exchange Rates API.
        Returns
        -------
        list
            json payload as dict
        """
        url = f"{self._base_url}/latest.json?app_id={self._auth}"
        return self.call_api(method="GET", url=url)


class OpenExchangeRatesApiPusher:
    def __init__(self) -> None:
        pass
        # s3 = boto3.resource('s3')
        # s3.Bucket('blinkistchallenge').put_object(Key='my/key/including/anotherfilename.txt', Body='test')
