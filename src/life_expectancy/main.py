import locale
import logging

from pathlib import Path

import click
import colorama
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sphinx_click.rst_to_ansi_formatter import make_rst_to_ansi_formatter

from life_expectancy import helpers
from life_expectancy.config import Config
from life_expectancy.constants import FileNames


# Most users should depend on colorama >= 0.4.6, and use just_fix_windows_console().
colorama.just_fix_windows_console()
# Set the locale to the user's default setting
locale.setlocale(locale.LC_ALL, "")
# Set the documentation URL for make_rst_to_ansi_formatter()
doc_url = "https://hakonhagland.github.io/pyml-regressions-example1/main/index.html"
# CLI colors for make_rst_to_ansi_formatter()
cli_colors = {
    "heading": {"fg": colorama.Fore.GREEN, "style": colorama.Style.BRIGHT},
    "url": {"fg": colorama.Fore.CYAN, "style": colorama.Style.BRIGHT},
    "code": {"fg": colorama.Fore.BLUE, "style": colorama.Style.BRIGHT},
}
click_command_cls = make_rst_to_ansi_formatter(doc_url, colors=cli_colors)

np.random.seed(42)  # make the output stable across runs
plt.rc("font", size=12)
plt.rc("axes", labelsize=14, titlesize=14)
plt.rc("legend", fontsize=12)
plt.rc("xtick", labelsize=10)
plt.rc("ytick", labelsize=10)
matplotlib.use("TkAgg")  # Ensure that the Tkinter backend is used for docker containers


@click.group(cls=make_rst_to_ansi_formatter(doc_url, group=True, colors=cli_colors))
@click.option("--verbose", "-v", is_flag=True, help="Show verbose output")
@click.pass_context
def main(ctx: click.Context, verbose: bool) -> None:
    """``life-expectancy`` let's you explore life expectancy data presented in Chapter
    1 of the book `Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow (3rd ed.) <https://github.com/ageron/handson-ml3>`_.


    * ``download-data``: downloads the ``.csv`` data file from
      `the book web page <https://github.com/ageron/handson-ml3>`_.

    * ``plot-data``: plots the data using `matplotlib <https://matplotlib.org/stable/index.html>`_.

    """
    ctx.ensure_object(dict)
    ctx.obj["VERBOSE"] = verbose
    if verbose:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)
        # logging.basicConfig(level=logging.WARNING)


@main.command(cls=click_command_cls)
def download_data() -> None:
    """``life-expectancy download-data`` downloads the data from ..."""
    config = Config()
    datadir = config.get_data_dir()
    helpers.download_data(datadir)


@main.command(cls=click_command_cls)
def plot_data() -> None:
    """``life-expectancy plot-data`` plots the data ..."""
    logging.info(f"Matplotlib backend: {matplotlib.get_backend()}")
    config = Config()
    datadir = config.get_data_dir()
    data_file = Path(datadir) / FileNames.lifesat_csv
    # Check that the data file exists, if not download it
    if not data_file.exists():
        logging.info(f"Data file {data_file} not found. Downloading data ...")
        helpers.download_data(datadir)
    lifesat = pd.read_csv(data_file)
    # X = lifesat[["GDP per capita (USD)"]].values
    # y = lifesat[["Life satisfaction"]].values
    lifesat.plot(
        kind="scatter", grid=True, x="GDP per capita (USD)", y="Life satisfaction"
    )
    plt.axis([23_500, 62_500, 4, 9])  # [xmin, xmax, ymin, ymax]
    plt.show()  # type: ignore
