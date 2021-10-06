import pytest


@pytest.mark.run(order=1)
def test_anything_get(test_config_anything_get):
    print(test_config_anything_get.json())
    assert test_config_anything_get.status_code == 200


# @pytest.mark.run(order=2)
# def test_anything_patch(test_config_anything_patch):
#     print(test_config_anything_patch.json())
#     assert test_config_anything_patch.status_code == 200



