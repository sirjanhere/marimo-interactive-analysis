import marimo

__generated_with = "0.18.0"
app = marimo.App(width="medium")


# ----------------------------------------------------------
# Cell 1: Import libraries (no dependencies)
# ----------------------------------------------------------
@app.cell
def _():
    # 24f2004829@ds.study.iitm.ac.in
    import marimo as mo
    import pandas as pd
    import numpy as np
    return mo, np, pd


# ----------------------------------------------------------
# Cell 2: Create slider (no dependencies)
# ----------------------------------------------------------
@app.cell
def _(mo):
    slider = mo.ui.slider(start=1, stop=10, value=5)
    slider
    return slider


# ----------------------------------------------------------
# Cell 3: Use slider.value to create dataframe (depends on Cell 2)
# slider → df
# ----------------------------------------------------------
@app.cell
def _(np, pd, slider):
    x = np.arange(1, 21)
    y = x * slider.value
    df = pd.DataFrame({"x": x, "y": y})
    df
    return df


# ----------------------------------------------------------
# Cell 4: Dynamic markdown reacts to slider (depends on slider)
# slider → markdown
# ----------------------------------------------------------
@app.cell
def _(mo, slider):
    mo.md(f"Selected multiplier: {slider.value}")
    return


# ----------------------------------------------------------
# Cell 5: Plot updates when df updates (depends on df)
# df → plot
# ----------------------------------------------------------
@app.cell
def _(df):
    import matplotlib.pyplot as plt
    plt.plot(df["x"], df["y"])
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Reactive plot: y = x * slider.value")
    plt.show()
    return


# ----------------------------------------------------------
# Cell 6: Full data flow summary (metadata only)
# slider → df → markdown + plot
# ----------------------------------------------------------
@app.cell
def _(mo):
    mo.md("""
**Data Flow Documentation**

Cell 2: slider created  
Cell 3: slider.value → dataframe df  
Cell 4: slider.value → dynamic markdown  
Cell 5: df → reactive plot  

**Full chain:**  
slider → df → markdown + plot
""")
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
