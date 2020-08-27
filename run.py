from screening_report_tool.preprocessing.read import read_data_from_excel
from screening_report_tool.preprocessing.transform import Data
from screening_report_tool.plotting.plots import (
    create_screenings_boxplot,
    create_problems_grouped_bar_plot,
)

filepath = "data/SampleScreeningData.xlsx"
column_name = "Screenings"
our_name = "K"
output_name = "output/SampleScreeningBoxplot.html"

df = read_data_from_excel(filepath=filepath)
data = Data(df=df, screening_column=column_name, our_name=our_name)
data.set_screenings_array()
data.set_us_data()
data.set_rest_data(total_row_name="Total")

fig = create_screenings_boxplot(
    screenings_array=data.screenings_array, our_number=data.n_screenings_us
)
fig2 = create_problems_grouped_bar_plot(
    us_prop_array=data.us_prop_array,
    rest_prop_array=data.rest_prop_array,
    problems=data.problems,
)
fig.show()
fig2.show()
# fig.write_html(output_name)
