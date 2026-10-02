import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def draw_line_plot():
    # Import data
    df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates=["date"])

    # Set date as index
    df = df.set_index("date")

    # Clean data
    df = df[
        (df["value"] >= df["value"].quantile(0.025))
        & (df["value"] <= df["value"].quantile(0.975))
    ]

    # Create line plot
    fig, ax = plt.subplots(figsize=(15, 5))
    ax.plot(df.index, df["value"])

    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")

    # Save image
    fig.savefig("line_plot.png")

    return fig


def draw_bar_plot():
    # Copy data
    df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates=["date"])

    # Set date as index
    df = df.set_index("date")

    # Clean data
    df = df[
        (df["value"] >= df["value"].quantile(0.025))
        & (df["value"] <= df["value"].quantile(0.975))
    ]

    # Create year and month columns
    df_bar = df.copy()
    df_bar["year"] = df_bar.index.year
    df_bar["month"] = df_bar.index.month

    # Average daily page views by year and month
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
    plt.legend(
        title="Months",
        labels=[
            "January", "February", "March", "April",
            "May", "June", "July", "August",
            "September", "October", "November", "December"
        ]
    )

    fig.savefig("bar_plot.png")

    return fig


def draw_box_plot():
    # Copy data
    df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates=["date"])

    # Set date as index
    df = df.set_index("date")

    # Clean data
    df = df[
        (df["value"] >= df["value"].quantile(0.025))
        & (df["value"] <= df["value"].quantile(0.975))
    ]

    # Prepare data
    df_box = df.copy()
    df_box["year"] = df_box.index.year
    df_box["month"] = df_box.index.month

    # Create month names
    month_names = [
        "Jan", "Feb", "Mar", "Apr", "May", "Jun",
        "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
    ]

    df_box["month"] = pd.Categorical(
        df_box["month"],
        categories=range(1, 13),
        ordered=True
    )

    # Create figure
    fig, axes = plt.subplots(1, 2, figsize=(15, 5))

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

    axes[1].set_xticklabels(month_names)

    fig.savefig("box_plot.png")

    return fig
