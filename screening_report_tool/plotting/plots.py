import plotly.graph_objects as go


def create_screenings_boxplot(screenings_array, our_number):
    fig = go.Figure()
    fig.add_trace(go.Box(x=screenings_array, boxmean=True, name=""))
    fig.update_layout(
        title={
            "text": "Network's Screening Distribution",
            "x": 0.5,
            "xanchor": "center",
        },
        xaxis_title="Number of Screenings",
        yaxis_title="",
        width=600,
        height=400,
        annotations=[
            {
                "x": our_number,
                "y": 0,
                "xref": "x",
                "yref": "y",
                "text": "Us",
                "showarrow": True,
                "arrowhead": 6,
            }
        ],
    )
    return fig

