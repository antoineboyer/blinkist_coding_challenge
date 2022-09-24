"""Fetch the latest exchange rates available from the Open Exchange Rates API.
Examples
--------
To be written
"""

import os
import json
from datetime import datetime

import requests
import boto3

OPEN_EXCHANGE_API_URL = "https://openexchangerates.org/api/"
BUCKET_NAME = "blinkistchallenge"


class OpenExchangeRatesApiFetcher:
    def __init__(self) -> None:
        self._base_url = OPEN_EXCHANGE_API_URL
        self._auth = "605b5617fae04483a3232a73b56b15f4" or os.environ["appid"]

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
           Not doing it for EUR base as it is not part of the free subscription plan.
        Returns
        -------
        list
            json payload as dict
        """
        url = f"{self._base_url}/latest.json?app_id={self._auth}"
        return self.call_api(method="GET", url=url)


class OpenExchangeRatesApiPusher:
    def __init__(self, data: dict) -> None:
        self.data = data

    def push_current_exchange_to_s3(self) -> None:
        """_summary_"""
        s3 = boto3.resource("s3")
        exchange_datetime = (datetime.fromtimestamp(self.data["timestamp"])).strftime(
            "%Y_%m_%d_%H_%M_%S"
        )
        key = f"exchange_rates_{exchange_datetime}.json"
        body = json.dumps(self.data)
        s3.Bucket(BUCKET_NAME).put_object(Key=key, Body=body)


def handler(event, context) -> None:
    # pulling the data from openexchangerates.org
    data = OpenExchangeRatesApiFetcher().get_current_exchange()
    # saving the data in S3
    OpenExchangeRatesApiPusher(data=data).push_current_exchange_to_s3()