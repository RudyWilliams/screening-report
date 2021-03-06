import argparse
import pathlib

import screening_report_tool.config as config
from screening_report_tool.preprocessing.read import (
    create_filepath,
    read_data_from_excel,
)
from screening_report_tool.preprocessing.transform import Data
from screening_report_tool.plotting.plots import (
    create_screenings_boxplot,
    create_problems_grouped_bar_plot,
)


def run_cli():
    parser = argparse.ArgumentParser(description="Create plots to analyze screenings.")

    parser.add_argument(
        "--month",
        type=str,
        default=None,
        help="The month to look for the data in (required when --testing is not flagged)",
    )
    parser.add_argument(
        "--year",
        type=str,
        default=None,
        help="The year to look for the data in (required when --testing is not flagged)",
    )
    parser.add_argument(
        "--testing", action="store_true", help="When flagged, use the sample data"
    )
    parser.add_argument(
        "--save-at", type=str, default=None, help="Dir path as location to save figures"
    )
    args = parser.parse_args()

    month = args.month
    year = args.year
    testing = args.testing
    save_at = args.save_at

    if testing:
        filepath = config.testing_filepath

    else:
        if (month is None) or (year is None):
            raise ValueError(
                "Must set both --month and --year when --testing is not flagged"
            )

        filepath = create_filepath(
            root=config.root, month=month, year=year, filename=config.filename
        )

    screening_column_name = config.screening_column_name
    our_row_name = config.our_row_name
    total_row_name = config.total_row_name

    df = read_data_from_excel(filepath=filepath)

    data = Data(
        df=df, screening_column_name=screening_column_name, our_name=our_row_name
    )
    data.set_screenings_array()
    data.set_us_data()
    data.set_rest_data(total_row_name=total_row_name)

    fig1 = create_screenings_boxplot(
        screenings_array=data.screenings_array, our_number=data.n_screenings_us
    )
    fig2 = create_problems_grouped_bar_plot(
        us_prop_array=data.us_prop_array,
        rest_prop_array=data.rest_prop_array,
        problems=data.problems,
    )
    fig1.show()
    fig2.show()

    if save_at:
        path = pathlib.Path(save_at).as_posix()  # to get rid of potentially trailing /
        boxplot_fpath = f"{path}/boxplot.html"
        bar_fpath = f"{path}/grouped_barplot.html"
        fig1.write_html(boxplot_fpath)
        print(f"---boxplot saved at {boxplot_fpath}")
        fig2.write_html(bar_fpath)
        print(f"---grouped barplot saved at {bar_fpath}")

