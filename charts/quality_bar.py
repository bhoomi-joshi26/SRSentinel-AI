import plotly.graph_objects as go


def create_quality_bar(score):

    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            x=["Quality Score"],
            y=[score],
            text=[f"{score}%"],
            textposition="outside"
        )
    )

    fig.update_layout(
        title="Overall SRS Quality",
        yaxis=dict(range=[0, 100]),
        height=400
    )

    return fig