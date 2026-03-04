from serg.core import greet

def test_greet_returns_expected_message():
    result = greet("Jordan")
    assert result == "Welcome to SERG, Jordan."