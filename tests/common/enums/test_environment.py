import pytest

from common.enums import Environment


@pytest.mark.parametrize(
    'value',
    [
        'some_random_string',
        '',
    ],
)
def test_environment_from_str_unknown(value):
    env = Environment.from_str(value)
    assert env == Environment.UNKNOWN
