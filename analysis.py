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
    # Cell 1: Create slider UI element (no dependencies)
    slider = mo.ui.slider(start=1, stop=10, value=5)
    slider

    return (slider,)


@app.cell
def _(np, pd, slider):
    # Cell 2: Uses slider.value to build dataframe (depends on Cell 1)
    x = np.arange(1, 21)
    y = x * slider.value

    df = pd.DataFrame({"x": x, "y": y})
    df

    return (df,)


@app.cell
def _(mo, slider):
    # Cell 3: Dynamic text updates when slider changes (depends on slider)
    mo.md(f"Selected multiplier: {slider.value}")

    return


@app.cell
def _(df):
    # Cell 4: Plot updates reactively based on df (depends on Cell 2)
    import matplotlib.pyplot as plt

    plt.plot(df["x"], df["y"])
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Reactive plot: y = x * slider.value")
    plt.show()

    return


@app.cell
def _(mo):
    # Cell 5: Full data flow summary:
    # slider.value → updates df → updates markdown + plot
    mo.md("""
    Data flow documented with comments in each cell.
    """)

    return


@app.cell
def _():
    # ----------------------------------------------------------
    # DATA FLOW DOCUMENTATION
    #
    # Cell 1:
    #     Creates the slider UI element (slider)
    #
    # Cell 2:
    #     Reads slider.value
    #     Uses it to compute y = x * slider.value
    #     Builds the dataframe df
    #
    # Cell 3:
    #     Displays dynamic markdown that updates when slider.value changes
    #
    # Cell 4:
    #     Plots df, so the plot updates automatically when slider changes
    #
    # Summary:
    # slider.value  →  updates df  →  updates markdown & plot
    # ----------------------------------------------------------

    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
