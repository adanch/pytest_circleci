
def pytest_addoption(parser):
    parser.addoption('--log',
                     action='store',
                     default=True,
                     help='info')


def pytest_configure(config):

    if config.getoption('log'):
        import logging
        logging.basicConfig(level=logging.INFO)