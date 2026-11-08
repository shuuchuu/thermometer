import sys

# The lab's choice: rich's print understands markup such as [bold].
from rich import print  # ruff: ignore[builtin-import-shadowing]

from thermometer.conversion import celsius_to_fahrenheit


def main() -> int:
    arguments = sys.argv[1:]
    if not arguments:
        print("Usage: to-fahrenheit TEMPERATURE...", file=sys.stderr)
        return 1
    for argument in arguments:
        celsius = float(argument)
        print(
            f"{celsius:.1f} °C = [bold]{celsius_to_fahrenheit(celsius):.1f} °F[/bold]"
        )
    return 0
