import json
import logging
import os
from pathlib import Path

from bot import BotOrchestrator

logging.basicConfig(handlers=[logging.StreamHandler()],
                    level=logging.INFO,
                    format='%(asctime)s %(threadName)-12s %(levelname).4s %(message)s',
                    datefmt='%a %d %H:%M:%S')

current_dir = Path(os.path.dirname(os.path.abspath(__file__)))


def read_all_credentials():
    with open(current_dir.joinpath("credentials.json")) as cred_f:
        return json.load(cred_f)


def main_execution():
    credentials = read_all_credentials()

    with BotOrchestrator(credentials) as orchestrator:
        orchestrator.parse_different_submissions("FreeKarma4U+FreeKarma4You+karmawhore", limit=120)
        orchestrator.log_karma()
