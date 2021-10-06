import pytest
from config import USER


@pytest.mark.run(order=1)
def test_basic_auth(test_config_basic_auth):
    assert test_config_basic_auth.json()['user'] == f"{USER}"


@pytest.mark.run(order=2)
def test_bearer_auth(test_config_bearer_auth):
    assert test_config_bearer_auth.json()['authenticated'] is True


@pytest.mark.run(order=3)
def test_digest_auth_qop(test_config_digest_auth_qop):
    assert test_config_digest_auth_qop.json()['user'] == f"{USER}"


@pytest.mark.run(order=4)
def test_digest_auth_qop_algo(test_config_digest_auth_qop_algo):
    assert test_config_digest_auth_qop_algo.json()['user'] == f"{USER}"


@pytest.mark.run(order=5)
def test_digest_auth_qop_algo_stale(test_config_digest_auth_qop_algo_stale):
    assert test_config_digest_auth_qop_algo_stale.json()['user'] == f"{USER}"


@pytest.mark.run(order=6)
def test_hidden_basic_auth(test_config_hidden_basic_auth):
    assert test_config_hidden_basic_auth.json()['user'] == f"{USER}"
