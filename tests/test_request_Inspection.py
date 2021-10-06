import pytest


@pytest.mark.run(order=1)
def test_getting_header(test_config_getting_header):
    # assert test_config_getting_header
    print(test_config_getting_header.json())
    assert test_config_getting_header.json()['headers'] is not None


@pytest.mark.run(order=2)
def test_getting_useragent(test_config_getting_useragent):
    assert test_config_getting_useragent.json()['origin'] == "110.37.205.206"


@pytest.mark.run(order=3)
def test_getting_ip(test_config_getting_ip):
    assert test_config_getting_ip.json()['user-agent'] is not None
