import logging
import requests

from pathlib import Path
from life_expectancy.constants import FileNames


def download_data(datadir: Path) -> None:
    """Download the data file from the book's web page."""
    data_url = (
        f"https://github.com/ageron/data/raw/main/lifesat/{FileNames.lifesat_csv}"
    )
    response = requests.get(data_url)
    response.raise_for_status()  # Ensure we notice bad responses
    datadir.mkdir(parents=True, exist_ok=True)
    savename = Path(datadir) / FileNames.lifesat_csv
    with open(savename, "w", encoding="utf-8") as f:
        f.write(response.content.decode("utf-8"))
    logging.info(f"Data downloaded and saved to {savename}")
