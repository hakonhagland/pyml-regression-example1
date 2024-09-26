# import logging
import shutil
from pathlib import Path

# import typing
import pytest

from life_expectancy.config import Config
from life_expectancy.constants import FileNames
from .common import PrepareConfigDir, PrepareDataDir

PytestDataDict = dict[str, str]


@pytest.fixture(scope="session")
def test_file_path() -> Path:
    return Path(__file__).parent / "files"


@pytest.fixture(scope="session")
def test_data() -> PytestDataDict:
    return {
        "chats_zip_fn": "chats.zip",
        "config_dir": "config",
        "data_dir": "data",
        "downloads_dir": "Downloads",
        "invalid_conversations_json_fn": "conversations_invalid.json",
    }


# @pytest.fixture()
# def config_oject(
#     data_dir_path: Path,
#     prepare_config_dir: PrepareConfigDir,
#     mocker: MockerFixture,
# ) -> Config:
#     data_dir = data_dir_path
#     config_dir = prepare_config_dir(add_config_ini=True)
#     mocker.patch(
#         "platformdirs.user_config_dir",
#         return_value=config_dir,
#     )
#     data_dir = data_dir_path
#     mocker.patch(
#         "platformdirs.user_data_dir",
#         return_value=data_dir,
#     )
#     return Config()


@pytest.fixture()
def config_dir_path(prepare_config_dir: PrepareConfigDir) -> Path:
    return prepare_config_dir(add_config_ini=False)


@pytest.fixture()
def data_dir_path(prepare_data_dir: PrepareDataDir) -> Path:
    return prepare_data_dir(datafile_exists=True)


@pytest.fixture()
def prepare_config_dir(
    tmp_path: Path, test_file_path: Path, test_data: PytestDataDict
) -> PrepareConfigDir:
    def _prepare_config_dir(add_config_ini: bool) -> Path:
        config_dir = tmp_path / test_data["config_dir"]
        config_dir.mkdir()
        config_dirlock_fn = test_file_path / test_data["config_dir"] / Config.dirlock_fn
        shutil.copy(config_dirlock_fn, config_dir)
        # if add_config_ini:
        #     config_ini_fn = test_file_path / test_data["config_dir"] / Config.config_fn
        #     save_fn = config_dir / config_ini_fn.name
        #     shutil.copy(config_ini_fn, save_fn)
        return config_dir

    return _prepare_config_dir


@pytest.fixture()
def prepare_data_dir(
    tmp_path: Path, test_file_path: Path, test_data: PytestDataDict
) -> PrepareDataDir:
    def _prepare_data_dir(datafile_exists: bool) -> Path:
        data_dir = tmp_path / test_data["data_dir"]
        data_dir.mkdir()
        data_dirlock_fn = test_file_path / test_data["data_dir"] / Config.dirlock_fn
        shutil.copy(data_dirlock_fn, data_dir)
        if datafile_exists:
            datafile_fn = test_file_path / test_data["data_dir"] / FileNames.lifesat_csv
            shutil.copy(datafile_fn, data_dir)
        return data_dir

    return _prepare_data_dir


@pytest.fixture()
def datafile_contents(test_file_path: Path, test_data: PytestDataDict) -> bytes:
    datafile_fn = test_file_path / test_data["data_dir"] / FileNames.lifesat_csv
    with open(datafile_fn, "rb") as fp:
        return fp.read()
