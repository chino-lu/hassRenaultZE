"""Utils for the new Renault API."""
import aiohttp
import logging
from typing import Dict

_LOGGER = logging.getLogger("pyze.api.utils")


async def get_api_keys_from_myrenault(
    session: aiohttp.ClientSession, locale: str = "en_GB"
) -> Dict:
    url = f"https://renault-wrd-prod-1-euw1-myrapp-one.s3-eu-west-1.amazonaws.com/configuration/android/config_{locale}.json"
    async with session.get(url) as response:
        response.raise_for_status()
        response_body = await response.json()

        _LOGGER.debug("Received api keys from myrenault response: % s", response_body)

        servers = response_body["servers"]
        return {
            "gigya-api-key": servers["gigyaProd"]["apikey"],
            "gigya-api-url": servers["gigyaProd"]["target"],
            "kamereon-api-key": servers["wiredProd"]["apikey"],
            "kamereon-api-url": servers["wiredProd"]["target"],
        }