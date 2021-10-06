import pytest


@pytest.mark.run(order=1)
def test_cookie_getdata(test_config_cookie_getdata):
    print(test_config_cookie_getdata.json())
    assert test_config_cookie_getdata.status_code == 200


@pytest.mark.run(order=2)
def test_cookie_set(test_config_cookie_set):
    print(test_config_cookie_set.json())
    assert test_config_cookie_set.status_code == 200


@pytest.mark.run(order=3)
def test_cookie_set_name_value(test_config_cookie_set_name_value):
    print(test_config_cookie_set_name_value.json())
    assert test_config_cookie_set_name_value.status_code == 200


@pytest.mark.run(order=4)
def test_cookie_delete(test_config_cookie_delete):
    print(test_config_cookie_delete.json())
    assert test_config_cookie_delete.status_code == 200


