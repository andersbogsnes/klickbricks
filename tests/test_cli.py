from click.testing import CliRunner
from klickbrick.cli import cli
import pytest


@pytest.fixture(scope="session")
def runner():
    return CliRunner()


def test_cli_returns_hello_world_with_no_args(runner: CliRunner):
    result = runner.invoke(cli, ["hello"])
    assert result.output == 'Hello World\n'


def test_cli_return_hello_name_when_passed_name(runner: CliRunner):
    result = runner.invoke(cli, ["hello", "--name", "tester"])
    assert result.output == 'Hello tester\n'
