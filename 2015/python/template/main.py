from pathlib import Path

import time
import logging

# Set up logging
logging.basicConfig(
    format="%(asctime)s.%(msecs)03d:%(levelname)s:%(name)s:\t%(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


# Define the directory path
SCRIPT_DIR = Path(__file__).parent
INPUT_FILE = "input/input.txt"

input_file = Path(SCRIPT_DIR, INPUT_FILE)


def main():
    with open(input_file, "rt") as f:
        data = f.read()

    logger.debug(data)


if __name__ == "__main__":
    start_time = time.perf_counter()
    main()
    end_time = time.perf_counter()
    logger.info("Execution time %0.4f seconds", end_time - start_time)
