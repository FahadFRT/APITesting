from config import DSTRING
import pytest


@pytest.mark.run(order=1)
def test_dynamic_data_decode_base64string(test_config_dynamic_data_decode_base64string):
    assert test_config_dynamic_data_decode_base64string.text == DSTRING
