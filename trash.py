import pandas as pd
import plotly.graph_objects as go


data = pd.read_excel("data/SampleScreeningData.xlsx", index_col=0)

# remove total (so we can recalculate without us in it)
no_totals_df = data.iloc[:-1, :]

# create total without us
is_us = no_totals_df.index == "K"
us_array, not_us = no_totals_df.loc[is_us, :].values[0], no_totals_df.loc[~is_us, :]
rest_totals_array = not_us.sum(axis=0).values


# create proportions
us_array, n_screen_us = us_array[:-1], us_array[-1]
rest_totals_array, n_screen_rest = rest_totals_array[:-1], rest_totals_array[-1]

# print(us_array, rest_totals_array)

us_array_prop = us_array / n_screen_us
rest_totals_array_prop = rest_totals_array / n_screen_rest

# print(us_array_prop, rest_totals_array_prop)
x_labels = data.columns[:-1]

fig = go.Figure()
fig.add_trace(go.Bar(x=x_labels, y=us_array_prop, name="Our Proportions"))
fig.add_trace(
    go.Bar(x=x_labels, y=rest_totals_array_prop, name="Rest of Network Proportions")
)
fig.update_layout(
    barmode="group",
    title={"text": "Us vs. Rest of Network Aggregated", "x": 0.5, "xanchor": "center"},
    xaxis_title={"text": "Issue",},
    yaxis_title={"text": "Proportion of Screening"},
)
fig.show()

# fig.update_layout(
#     title={"text": "Network's Screening Distribution", "x": 0.5, "xanchor": "center"},
#     xaxis_title="Number of Screenings",
#     yaxis_title="",
#     width=600,
#     height=400,
#     annotations=[
#         {
#             "x": ours,
#             "y": 0,
#             "xref": "x",
#             "yref": "y",
#             "text": "Us",
#             "showarrow": True,
#             "arrowhead": 6,
#         }
#     ],
# )
# fig.show()
