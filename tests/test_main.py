import logging
from pathlib import Path

import pytest
from _pytest.logging import LogCaptureFixture
from click.testing import CliRunner
from pytest_mock.plugin import MockerFixture

import life_expectancy.main as main
from .common import PrepareDataDir


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


@pytest.mark.parametrize("datafile_exists", [True, False])
class TestPlotDataCmd:
    def test_invoke(
        self,
        datafile_exists: bool,
        caplog: LogCaptureFixture,
        mocker: MockerFixture,
        config_dir_path: Path,
        prepare_data_dir: PrepareDataDir,
        datafile_contents: bytes,
    ) -> None:
        caplog.set_level(logging.INFO)
        data_dir = prepare_data_dir(datafile_exists=datafile_exists)
        config_dir = config_dir_path
        mocker.patch(
            "platformdirs.user_config_dir",
            return_value=config_dir,
        )
        mocker.patch(
            "platformdirs.user_data_dir",
            return_value=data_dir,
        )
        if not datafile_exists:
            # Create a mock response object
            mock_response = mocker.Mock()
            mock_response.content = datafile_contents
            mock_response.raise_for_status = mocker.Mock()
            # Patch requests.get to return the mock response
            mocker.patch("requests.get", return_value=mock_response)
        mocker.patch("matplotlib.pyplot.show", return_value=None)
        import matplotlib

        matplotlib.use("Agg")
        runner = CliRunner()
        args = ["plot-data"]
        result = runner.invoke(main.main, args)
        assert result.exit_code == 0
