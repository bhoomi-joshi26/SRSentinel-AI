import plotly.graph_objects as go


def create_gauge_chart(score):

    fig = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=score,
            title={"text": "Quality Score"},
            gauge={
                "axis": {"range": [0, 100]},
                "bar": {"color": "darkblue"},
                "steps": [
                    {"range": [0, 40], "color": "#ff4d4d"},
                    {"range": [40, 70], "color": "#ffcc00"},
                    {"range": [70, 100], "color": "#00cc66"}
                ]
            }
        )
    )

    fig.update_layout(height=350)

    return fig