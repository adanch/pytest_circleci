import logging


def test_first():
    logging.info('TEST 1')
    logging.info('Some text')
    assert '21' in 'smth'


def test_second():
    logging.info('TEST 2')
    assert 1 == 1


def test_third():
    logging.info('http://google.nl')
    logging.info('TEST 3')
    assert 1 > 1