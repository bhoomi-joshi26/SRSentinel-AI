import plotly.graph_objects as go


def create_impact_chart(ambiguity, quality):

    categories = [
        "Ambiguity",
        "Quality"
    ]

    values = [
        ambiguity,
        quality
    ]

    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            x=categories,
            y=values,
            text=values,
            textposition="outside"
        )
    )

    fig.update_layout(
        title="Quality vs Ambiguity",
        yaxis=dict(range=[0, 100]),
        height=400
    )

    return fig