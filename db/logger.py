import logging


def main() -> None:
    logging.basicConfig(filename="basic.log")

    logging.debug("DEBUG message")
    logging.info("INFO message")
    logging.warning("WARNING message")
    logging.error("ERROR message")
    logging.critical("CRITICAL message")


if __name__ == "__main__":
    main()
