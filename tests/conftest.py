import pytest
from config import URL, USER, PASSWORD, ALGORITHM, QOP, HEADERS, URLDA, USER_PASS, STALE_AFTER,SESSION
from requests.auth import HTTPBasicAuth, HTTPDigestAuth
from requests.structures import CaseInsensitiveDict
from client import client


# --------------------------------------------------------------------------- #
# ---------------------------- Request Inspection --------------------------- #
# --------------------------------------------------------------------------- #


@pytest.fixture(scope="class")
def test_config_getting_header():
    return client.RequestClient().get_req(f"{URL}/headers")


@pytest.fixture(scope="class")
def test_config_getting_useragent():
    return client.RequestClient().get_req(f"{URL}/ip")


@pytest.fixture(scope="class")
def test_config_getting_ip():
    return client.RequestClient().get_req(f"{URL}/user-agent")


# --------------------------------------------------------------------------- #
# ------------------------------- Authentication ---------------------------- #
# --------------------------------------------------------------------------- #


@pytest.fixture(scope="class")
def test_config_basic_auth():
    return client.RequestClient().get_req(f"{URL}/basic-auth/{USER_PASS}", auth=HTTPBasicAuth(USER, PASSWORD))


@pytest.fixture(scope="class")
def test_config_bearer_auth():
    return client.RequestClient().get_req(f"{URL}/bearer", headers=HEADERS)


@pytest.fixture(scope="class")
def test_config_digest_auth_qop():
    return client.RequestClient().get_req(f"{URLDA}/{QOP}/{USER_PASS}", auth=HTTPDigestAuth(USER, PASSWORD))


@pytest.fixture(scope="class")
def test_config_digest_auth_qop_algo():
    return client.RequestClient().get_req(f"{URLDA}/{QOP}/{USER_PASS}/{ALGORITHM}", auth=HTTPDigestAuth(USER, PASSWORD))


@pytest.fixture(scope="class")
def test_config_digest_auth_qop_algo_stale():
    return client.RequestClient().get_req(f"{URLDA}/{QOP}/{USER_PASS}/{ALGORITHM}/{STALE_AFTER}", auth=HTTPDigestAuth(USER, PASSWORD))


@pytest.fixture(scope="class")
def test_config_hidden_basic_auth():
    return client.RequestClient().get_req(f"{URL}/hidden-basic-auth/{USER_PASS}", auth=HTTPBasicAuth(USER, PASSWORD))


# --------------------------------------------------------------------------- #
# ---------------------------- Response Inspection -------------------------- #
# --------------------------------------------------------------------------- #


@pytest.fixture(scope="class")
def test_config_response_inspection_modification_check():
    return client.RequestClient().get_req(f"{URL}/cache")


@pytest.fixture(scope="class")
def test_config_response_inspection_header_check_for_sec():
    return client.RequestClient().get_req(f"{URL}/cache/5")


# --------------------------------------------------------------------------- #
# ------------------------------- Dynamic Data ------------------------------ #
# --------------------------------------------------------------------------- #

@pytest.fixture(scope="class")
def test_config_dynamic_data_decode_base64string():
    return client.RequestClient().get_req(f"{URL}/base64/SFRUUEJJTiBpcyBhd2Vzb21l")


# --------------------------------------------------------------------------- #
# ---------------------------------- Cookie --------------------------------- #
# --------------------------------------------------------------------------- #

@pytest.fixture(scope="class")
def test_config_cookie_getdata():
    return client.RequestClient().get_req(f"{URL}/cookies")


@pytest.fixture(scope="class")
def test_config_cookie_set():
    header = CaseInsensitiveDict()
    header = {'accept' : 'text/plain'}
    return client.RequestClient().get_req(f"{URL}/cookies/set?freeform=testingForm", headers=header)


@pytest.fixture(scope="class")
def test_config_cookie_set_name_value():
    header = CaseInsensitiveDict()
    header = {'accept': 'text/plain'}
    return client.RequestClient().get_req(f"{URL}/cookies/set/Site/google.com", headers=header)


@pytest.fixture(scope="class")
def test_config_cookie_delete():
    header = CaseInsensitiveDict()
    header = {'accept': 'text/plain'}
    return client.RequestClient().get_req(f"{URL}/cookies/delete?freeform=unknown", headers=header)


# --------------------------------------------------------------------------- #
# ------------------------------------- IMAGE ------------------------------- #
# --------------------------------------------------------------------------- #


@pytest.fixture(scope="class")
def test_config_image_get():
    response = client.RequestClient().get_req(f"{URL}/image/webp")
    file = open("sample_image.webp", "wb")
    file.write(response.content)
    file.close()
    return response

# --------------------------------------------------------------------------- #
# ------------------------------------ AnyThing ----------------------------- #
# --------------------------------------------------------------------------- #

@pytest.fixture(scope="class")
def test_config_anything_get():
    return client.RequestClient().get_req(f"{URL}/anything")

