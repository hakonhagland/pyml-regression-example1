import locale
import logging

import click
import colorama
from sphinx_click.rst_to_ansi_formatter import make_rst_to_ansi_formatter
from life_expectancy.config import Config

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


@click.group(cls=make_rst_to_ansi_formatter(doc_url, group=True, colors=cli_colors))
@click.option("--verbose", "-v", is_flag=True, help="Show verbose output")
@click.pass_context
def main(ctx: click.Context, verbose: bool) -> None:
    """``life-expectancy`` let's you explore life expectancy data from ...

    * ``download-data``: downloads the data from ..
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
    click.echo(f"Downloading data to {datadir}")
