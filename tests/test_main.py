import logging
from pathlib import Path

import pytest
from _pytest.logging import LogCaptureFixture
from click.testing import CliRunner
from pytest_mock.plugin import MockerFixture

import life_expectancy.main as main


@pytest.mark.parametrize("verbose", [True, False])
class TestMainCmd:
    def test_help(
        self,
        verbose: bool,
        caplog: LogCaptureFixture,
        mocker: MockerFixture,
        data_dir_path: Path,
    ) -> None:
        caplog.set_level(logging.INFO)
        data_dir = data_dir_path
        mocker.patch(
            "platformdirs.user_config_dir",
            return_value=data_dir,
        )
        runner = CliRunner()
        args = ["download-data", "--help"]
        if verbose:
            args.insert(0, "-v")
        result = runner.invoke(main.main, args)
        assert result.stdout.startswith("Usage: main download-data [OPTIONS]")


class TestDownloadDataCmd:
    def test_invoke(
        self,
        caplog: LogCaptureFixture,
        mocker: MockerFixture,
        config_dir_path: Path,
        data_dir_path: Path,
    ) -> None:
        caplog.set_level(logging.INFO)
        data_dir = data_dir_path
        config_dir = config_dir_path
        mocker.patch(
            "platformdirs.user_config_dir",
            return_value=config_dir,
        )
        data_dir = data_dir_path
        mocker.patch(
            "platformdirs.user_data_dir",
            return_value=data_dir,
        )
        runner = CliRunner()
        args = ["download-data"]
        result = runner.invoke(main.main, args)
        assert result.exit_code == 0
