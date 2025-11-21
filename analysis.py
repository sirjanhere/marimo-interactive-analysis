import marimo

__generated_with = "0.18.0"
app = marimo.App(width="medium")


@app.cell
def _():
    return


@app.cell
def _():
    # 24f2004829@ds.study.iitm.ac.in
    # Importing libraries

    import marimo as mo
    import pandas as pd
    import numpy as np

    return mo, np, pd


@app.cell
def _(mo):
    # create slider here ONLY
    slider = mo.ui.slider(start=1, stop=10, value=5)

    slider

    return (slider,)


@app.cell
def _(np, pd, slider):
    # Use slider.value here
    x = np.arange(1, 21)
    y = x * slider.value

    df = pd.DataFrame({"x": x, "y": y})
    df

    return (df,)


@app.cell
def _(mo, slider):
    mo.md(f"Selected multiplier: {slider.value}")

    return


@app.cell
def _(df):
    import matplotlib.pyplot as plt

    plt.plot(df["x"], df["y"])
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Reactive plot: y = x * slider.value")
    plt.show()

    return


@app.cell
def _(mo):
    mo.md("""
    **Data Flow Documentation**

    slider.value
    → affects y values
    → updates df
    → updates markdown + plot
    """)

    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
