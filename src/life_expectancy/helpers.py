import logging
import requests

from pathlib import Path
from life_expectancy.constants import FileNames


def download_data(datadir: Path) -> None:
    """Download the data file from the book's web page."""
    download_items = []
    filename1 = FileNames.lifesat_csv
    data_url1 = f"https://github.com/ageron/data/raw/main/lifesat/{filename1}"
    download_items.append((filename1, data_url1))
    data_url2 = "https://sdmx.oecd.org/archive/rest/data/OECD,DF_BLI,/all?dimensionAtObservation=AllDimensions&format=csvfilewithlabels"
    filename2 = FileNames.lifesat_full_csv
    download_items.append((filename2, data_url2))
    # filename3 = FileNames.gdb_per_capita_csv
    # NOTE: I was not able to find a direct download URL at:
    #     https://ourworldindata.org/grapher/gdp-per-capita-worldbank
    #  instead I downloaded the data manually and uploaded it to my own GitHub repo
    # data_url3 = "https://raw.githubusercontent.com/hakonhagland/pyml-regression-example1/refs/heads/main/data/{filename2}"
    download_data_from_url(datadir, download_items=download_items)


def download_data_from_url(
    datadir: Path, download_items: list[tuple[str, str]]
) -> None:
    for filename, data_url in download_items:
        download_file(datadir, filename, data_url)


def download_file(datadir: Path, filename: str, data_url: str) -> None:
    response = requests.get(data_url)
    response.raise_for_status()  # Ensure we notice bad responses
    datadir.mkdir(parents=True, exist_ok=True)
    savename = Path(datadir) / filename
    with open(savename, "w", encoding="utf-8") as f:
        f.write(response.content.decode("utf-8"))
    logging.info(f"Data downloaded and saved to {savename}")
