import pandas as pd
import plotly.graph_objects as go


data = pd.read_excel("data/SampleScreeningData.xlsx", index_col=0)

screenings = data["Screenings"][:-1]
ours = data.loc["K", "Screenings"]
print(ours)

fig = go.Figure()
fig.add_trace(go.Box(x=screenings, boxmean=True, name=""))
fig.update_layout(
    title={"text": "Network's Screening Distribution", "x": 0.5, "xanchor": "center"},
    xaxis_title="Number of Screenings",
    yaxis_title="",
    width=600,
    height=400,
    annotations=[
        {
            "x": ours,
            "y": 0,
            "xref": "x",
            "yref": "y",
            "text": "Us",
            "showarrow": True,
            "arrowhead": 6,
        }
    ],
)
fig.show()
