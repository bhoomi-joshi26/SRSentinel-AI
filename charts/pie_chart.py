import plotly.express as px


def create_pie_chart(functional, non_functional, others):
    labels = ["Functional", "Non-Functional", "Others"]
    values = [functional, non_functional, others]

    fig = px.pie(
        names=labels,
        values=values,
        hole=0.45
    )

    fig.update_layout(
        title="Requirement Distribution",
        height=400
    )

    return fig