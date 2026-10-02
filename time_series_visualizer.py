import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Import data
df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates=["date"])

# Set date as index
df.set_index("date", inplace=True)

# Clean data
df = df[
    (df["value"] >= df["value"].quantile(0.025)) &
    (df["value"] <= df["value"].quantile(0.975))
]


def draw_line_plot():
    # Copy data
    df_line = df.copy()

    # Create figure
    fig, ax = plt.subplots(figsize=(15, 5))

    ax.plot(df_line.index, df_line["value"])

    ax.set_title(
        "Daily freeCodeCamp Forum Page Views 5/2016-12/2019"
    )
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")

    fig.savefig("line_plot.png")

    return fig


def draw_bar_plot():
    # Copy data
    df_bar = df.copy()

    # Create year and month columns
    df_bar["year"] = df_bar.index.year
    df_bar["month"] = df_bar.index.month

    # Average daily page views by month and year
    df_bar = df_bar.groupby(
        ["year", "month"]
    )["value"].mean().unstack()

    # Create bar plot
    fig = df_bar.plot(
        kind="bar",
        figsize=(12, 8)
    ).get_figure()

    plt.xlabel("Years")
    plt.ylabel("Average Page Views")

    # Full month names
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

    plt.legend(
        labels=months,
        title="Months"
    )

    fig.savefig("bar_plot.png")

    return fig


def draw_box_plot():
    # Copy data
    df_box = df.copy()

    # Create year and month columns
    df_box["year"] = df_box.index.year
    df_box["month"] = df_box.index.month

    # Create figure
    fig, axes = plt.subplots(1, 2, figsize=(16, 6))

    # Year-wise box plot
    sns.boxplot(
        data=df_box,
        x="year",
        y="value",
        ax=axes[0]
    )

    axes[0].set_title("Year-wise Box Plot (Trend)")
    axes[0].set_xlabel("Year")
    axes[0].set_ylabel("Page Views")

    # Month-wise box plot
    sns.boxplot(
        data=df_box,
        x="month",
        y="value",
        ax=axes[1]
    )

    axes[1].set_title("Month-wise Box Plot (Seasonality)")
    axes[1].set_xlabel("Month")
    axes[1].set_ylabel("Page Views")

    # Month labels starting from Jan
    axes[1].set_xticklabels([
        "Jan", "Feb", "Mar", "Apr", "May", "Jun",
        "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
    ])

    fig.savefig("box_plot.png")

    return fig

