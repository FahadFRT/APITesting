import os
import pytest


@pytest.mark.run(order=1)
def test_image_get(test_config_image_get):
    assert test_config_image_get.status_code == 200
    assert os.path.exists("sample_image.webp")
    os.remove("sample_image.webp")
