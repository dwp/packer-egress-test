#!/usr/bin/env python3

import os
import sys
import logging
import requests
import json

# Initialise logging
logger = logging.getLogger(__name__)
log_level = os.environ["LOG_LEVEL"] if "LOG_LEVEL" in os.environ else "ERROR"
logger.setLevel(logging.getLevelName(log_level.upper()))
logging.basicConfig(
    stream=sys.stdout,
    format="%(asctime)s %(levelname)s %(module)s "
           "%(process)s[%(thread)s] %(message)s",
)
logger.info("Logging at {} level".format(log_level.upper()))


def handler(event, context):
    errors = []
    for key, value in event["required_endpoints"].items():
        response = requests.get(value)
        if response.status_code != 200:
            errors.append(f"Error connecting to {key}: {value} - status code: {response.status_code}")
        else:
            logger.debug(f"Successfully connected to {key}: {value} - status code {response.status_code}")
        if len(errors) > 0:
            logger.error(errors)
            raise Exception(f"{len(errors)} required endpoints unreachable")


if __name__ == "__main__":
    try:
        json_content = json.loads(open("event.json", "r").read())
        handler(json_content, None)
    except Exception as e:
        logger.error(e)
        raise e
