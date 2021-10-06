import pytest


@pytest.mark.run(order=1)
def test_response_inspection_modification_check(test_config_response_inspection_modification_check):
    print("\n")

    assert test_config_response_inspection_modification_check.status_code == 304


# @pytest.mark.run(order=2)
# def test_response_inspection_header_check_for_sec(test_config_response_inspection_header_check_for_sec):
#     assert test_config_response_inspection_header_check_for_sec.status_code == 200

