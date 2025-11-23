from presidio_anonymizer.operators import Initial
import pytest


def test_correct_name():
    assert Initial().operator_name() == "initial"


@pytest.mark.parametrize(
    "input_text, initials",
    [
        ("John Smith", "J. S."),
        ("@abc", "@A."),
        ("@843A", "@8."),
    ],
)
def test_given_value_for_initial(input_text, initials):
    result = Initial().operate(input_text)
    assert result == initials


def test_removes_extra_whitespace():
    assert Initial().operate("  John   Smith  ") == "J. S."