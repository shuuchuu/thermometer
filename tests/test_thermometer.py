import sys

import pytest

from thermometer.cli import main
from thermometer.conversion import celsius_to_fahrenheit


@pytest.mark.parametrize(
    ("celsius", "fahrenheit"), [(0, 32), (100, 212), (-40, -40), (36.6, 97.88)]
)
def test_celsius_to_fahrenheit(celsius: float, fahrenheit: float) -> None:
    assert celsius_to_fahrenheit(celsius) == pytest.approx(fahrenheit)


def test_main_converts_each_argument(
    monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    monkeypatch.setattr(sys, "argv", ["to-fahrenheit", "20", "36.6"])
    assert main() == 0
    assert capsys.readouterr().out.splitlines() == [
        "20.0 °C = 68.0 °F",
        "36.6 °C = 97.9 °F",
    ]


def test_main_without_arguments_fails(
    monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    monkeypatch.setattr(sys, "argv", ["to-fahrenheit"])
    assert main() == 1
    assert "Usage" in capsys.readouterr().err
