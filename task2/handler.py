from exchange_rates import OpenExchangeRatesApiFetcher, OpenExchangeRatesApiPusher


def handle(event, context) -> dict:
    # pulling the data from openexchangerates.org
    data = OpenExchangeRatesApiFetcher().get_current_exchange()
    # saving the data in S3
    OpenExchangeRatesApiPusher(data=data).push_current_exchange_to_s3()
    return {
        "message": "The current exchange rates has been successfully upload to S3",
    }
