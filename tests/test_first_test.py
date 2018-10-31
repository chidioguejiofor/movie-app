import pytest


@pytest.fixture
def hello_string():
    return 'HELLO WORLD'

def test_ensure_that_fixture_works_correctly(hello_string):
    assert hello_string == 'HELLO WORLD'

