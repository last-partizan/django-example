import pytest
from django.utils import translation


@pytest.mark.parametrize(
    "language,expected",
    [("en", "Yes"), ("de", "Ja")],
)
def test_activate_language(language, expected):
    translation.activate(language)

    result = translation.gettext("Yes")

    assert result == expected


def test_default_translation():
    result = translation.gettext("Yes")

    assert result == "Yes"
