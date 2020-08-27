from screening_report_tool.preprocessing.read import read_data_from_excel
from screening_report_tool.preprocessing.transform import (
    get_our_screenings,
    get_screenings,
    Data,
)
from screening_report_tool.plotting.plots import create_screenings_boxplot

filepath = "data/SampleScreeningData.xlsx"
column_name = "Screenings"
our_name = "K"
output_name = "output/SampleScreeningBoxplot.html"

df = read_data_from_excel(filepath=filepath)
data = Data(df=df, screening_column=column_name, our_name=our_name)
data.set_screenings_array()
data.set_us_data()

fig = create_screenings_boxplot(
    screenings_array=data.screenings_array, our_number=data.n_screenings_us
)
fig.show()
# fig.write_html(output_name)
