import inspect
import os
import re
from shutil import rmtree
from typing import Callable

import numpy as np
import pandas as pd

import pandas_bokeh

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
PLOT_DIR = os.path.join(BASE_DIR, "plots")
TEST_SETS_DIRECTORY = os.path.join(os.path.dirname(BASE_DIR), "Testdata")

rmtree(PLOT_DIR, ignore_errors=True)
os.makedirs(PLOT_DIR, exist_ok=True)


def df_stocks() -> pd.DataFrame:

    np.random.seed(42)
    df = pd.DataFrame(
        {"Google": np.random.randn(1000) + 0.2, "Apple": np.random.randn(1000) + 0.17},
        index=pd.date_range("1/1/2000", periods=1000),
    )
    df = df.cumsum()
    df = df + 50

    return df


def df_parabula_cube() -> pd.DataFrame:

    x = np.arange(-3, 3, 0.1)
    y2 = x ** 2
    y3 = x ** 3
    df = pd.DataFrame({"x": x, "Parabula": y2, "Cube": y3})

    return df

def df_iris():

    # Load Iris Dataset:
    df_iris = pd.read_csv(os.path.join(TEST_SETS_DIRECTORY, "iris", "iris.csv"))

    return df_iris




def plot_Startimage():

    plotname = inspect.stack()[0][3][5:]
    pandas_bokeh.output_file(os.path.join(PLOT_DIR, f"{plotname}.html"))

    # Barplot:
    data = {
        "fruits": ["Apples", "Pears", "Nectarines", "Plums", "Grapes", "Strawberries"],
        "2015": [2, 1, 4, 3, 2, 4],
        "2016": [5, 3, 3, 2, 4, 6],
        "2017": [3, 2, 4, 4, 5, 3],
    }
    df = pd.DataFrame(data).set_index("fruits")
    p_bar = df.plot_bokeh(
        kind="bar",
        ylabel="Price per Unit [€]",
        title="Fruit prices per Year",
        show_figure=False,
    )

    # Lineplot:
    np.random.seed(42)
    df = pd.DataFrame(
        {"Google": np.random.randn(1000) + 0.2, "Apple": np.random.randn(1000) + 0.17},
        index=pd.date_range("1/1/2000", periods=1000),
    )
    df = df.cumsum()
    df = df + 50
    p_line = df.plot_bokeh(
        kind="line",
        title="Apple vs Google",
        xlabel="Date",
        ylabel="Stock price [$]",
        yticks=[0, 100, 200, 300, 400],
        ylim=(0, 400),
        colormap=["red", "blue"],
        show_figure=False,
    )

    # Scatterplot:
    df = df_iris()
    p_scatter = df.plot_bokeh(
        kind="scatter",
        x="petal length (cm)",
        y="sepal width (cm)",
        category="species",
        title="Iris DataSet Visualization",
        show_figure=False,
    )

    # Histogram:
    df_hist = pd.DataFrame(
        {
            "a": np.random.randn(1000) + 1,
            "b": np.random.randn(1000),
            "c": np.random.randn(1000) - 1,
        },
        columns=["a", "b", "c"],
    )

    p_hist = df_hist.plot_bokeh(
        kind="hist",
        bins=np.arange(-6, 6.5, 0.5),
        vertical_xlabel=True,
        normed=100,
        hovertool=False,
        title="Normal distributions",
        show_figure=False,
    )

    # Make Dashboard with Grid Layout:
    plot = pandas_bokeh.plot_grid(
        [[p_line, p_bar], [p_scatter, p_hist]], plot_width=450
    )

def plot_ApplevsGoogle_1():

    plotname = inspect.stack()[0][3][5:]
    pandas_bokeh.output_file(os.path.join(PLOT_DIR, f"{plotname}.html"))

    df = df_stocks()
    plot = df.plot_bokeh(kind="line")


def plot_ApplevsGoogle_2():

    plotname = inspect.stack()[0][3][5:]
    pandas_bokeh.output_file(os.path.join(PLOT_DIR, f"{plotname}.html"))

    df = df_stocks()
    plot = df.plot_bokeh(
        figsize=(800, 450),
        y="Apple",
        title="Apple vs Google",
        xlabel="Date",
        ylabel="Stock price [$]",
        yticks=[0, 100, 200, 300, 400],
        ylim=(0, 400),
        toolbar_location=None,
        colormap=["red", "blue"],
        hovertool_string=r"<img src='https://upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Apple_logo_black.svg/170px-Apple_logo_black.svg.png' height='42' alt='@imgs' width='42' style='float: left; margin: 0px 15px 15px 0px;' border='2' ></img> Apple \n\n<h4> Stock Price: </h4> @{Apple}",
        panning=False,
        zooming=False,
    )


def plot_ApplevsGoogle_3():

    plotname = inspect.stack()[0][3][5:]
    pandas_bokeh.output_file(os.path.join(PLOT_DIR, f"{plotname}.html"))

    df = df_stocks()
    plot = df.plot_bokeh(
        figsize=(800, 450),
        title="Apple vs Google",
        xlabel="Date",
        ylabel="Stock price [$]",
        yticks=[0, 100, 200, 300, 400],
        ylim=(100, 200),
        xlim=("2001-01-01", "2001-02-01"),
        colormap=["red", "blue"],
        plot_data_points=True,
        plot_data_points_size=10,
        marker="asterisk",
    )


def plot_Pointplot():

    plotname = inspect.stack()[0][3][5:]
    pandas_bokeh.output_file(os.path.join(PLOT_DIR, f"{plotname}.html"))

    df = df_parabula_cube()
    plot = df.plot_bokeh.point(
        x="x",
        xticks=range(-3, 4),
        size=5,
        colormap=["#009933", "#ff3399"],
        title="Pointplot (Parabula vs. Cube)",
        marker="x",
    )


def plot_Stepplot():

    plotname = inspect.stack()[0][3][5:]
    pandas_bokeh.output_file(os.path.join(PLOT_DIR, f"{plotname}.html"))

    df = df_parabula_cube()
    plot = df.plot_bokeh.step(
        x="x",
        xticks=range(-1, 1),
        colormap=["#009933", "#ff3399"],
        title="Pointplot (Parabula vs. Cube)",
        mode="after",
        figsize=(800, 300),
    )


def plot_Scatterplot():

    plotname = inspect.stack()[0][3][5:]
    pandas_bokeh.output_file(os.path.join(PLOT_DIR, f"{plotname}.html"))

    df = df_iris()
    df = df.sample(frac=1)

    #Create Bokeh-Table with DataFrame:
    from bokeh.models.widgets import DataTable, TableColumn
    from bokeh.models import ColumnDataSource

    data_table = DataTable(
        columns=[TableColumn(field=Ci, title=Ci) for Ci in df.columns],
        source=ColumnDataSource(df.head(10)),
    )

    #Create Scatterplot:
    p_scatter = df.plot_bokeh.scatter(
        x="petal length (cm)",
        y="sepal width (cm)",
        category="species",
        title="Iris DataSet Visualization",
        show_figure=False)

    #Combine Div and Scatterplot via grid layout:
    pandas_bokeh.plot_grid([[data_table, p_scatter]], plot_width=400, plot_height=350)

def plot_Scatterplot2():

    plotname = inspect.stack()[0][3][5:]
    pandas_bokeh.output_file(os.path.join(PLOT_DIR, f"{plotname}.html"))

    df = df_iris()
    df = df.sample(frac=1)

    #Change one value to clearly see the effect of the size keyword
    df.loc[13, "sepal length (cm)"] = 15

    #Make scatterplot:
    p_scatter = df.plot_bokeh.scatter(
        x="petal length (cm)",
        y="sepal width (cm)",
        category="species",
        title="Iris DataSet Visualization with Size Keyword",
        size="sepal length (cm)")

def extract_bokeh_html_from_file(plotname: str) -> str:

    with open(os.path.join(PLOT_DIR, f"{plotname}.html")) as f:
        s = f.read()
        header_content = re.search(r"<head>(.+)</head>", s, re.DOTALL).groups(1)[0]
        body = re.search(r"<body>(.+)</body>", s, re.DOTALL).groups(1)[0]
        bokeh_html = header_content + body

    return bokeh_html


def make_plots() -> dict:

    plots = {}
    for func in _return_plot_functions():
        plotname = func.__name__[5:]
        print(f"Create plot {plotname}")
        func()
        plots[plotname] = extract_bokeh_html_from_file(plotname)

    return plots


def _return_plot_functions() -> Callable:

    functions = []
    for key, value in globals().items():
        if callable(value) and value.__module__ == __name__ and key.startswith("plot_"):
            functions.append(value)

    return functions


if __name__ == "__main__":

    make_plots()
