# `thermometer`

Converts temperatures from degrees Celsius to degrees Fahrenheit:

```console
$ to-fahrenheit 20 36.6 -40
20.0 °C = 68.0 °F
36.6 °C = 97.9 °F
-40.0 °C = -40.0 °F
```

This is the end state of shuuchuu's package creation lab, published on
[Test PyPI](https://test.pypi.org/project/thermometer-shuuchuu/) as
`thermometer-shuuchuu`, whose module keeps the lab's name, `thermometer`. The lab
installs it from there when trainees have no Test PyPI account of their own, and
its automated runs publish development versions (`0.2.0.dev<timestamp>`) to check
the whole chain.

## Installing it from Test PyPI

Test PyPI doesn't mirror PyPI (its `rich` is a 0.0.0 placeholder), and uv takes
each package from the first index that has it. List PyPI first:

```console
uv pip install --index https://pypi.org/simple/ --index https://test.pypi.org/simple/ thermometer-shuuchuu
```

In a project, declare Test PyPI as an explicit index and pin the package to it:

```toml
[tool.uv.sources]
thermometer-shuuchuu = { index = "testpypi" }

[[tool.uv.index]]
name = "testpypi"
url = "https://test.pypi.org/simple/"
explicit = true
```

## Development

```console
uv run pytest
uv run ruff check && uv run ruff format --check
uv run pyrefly check
uv build
uv publish --index testpypi
```
