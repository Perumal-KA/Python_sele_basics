import logging

def test_print_logs():
    Logger=logging.getLogger(__name__)
    Logger.info("this is information")
    Logger.warning("this is warning")
    Logger.error("this is error")
    Logger.critical("this is critical")