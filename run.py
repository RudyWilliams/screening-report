from screening_report_tool.preprocessing.read import read_data_from_excel
from screening_report_tool.preprocessing.transform import (
    get_our_screenings,
    get_screenings,
)
from screening_report_tool.plotting.plots import create_screenings_boxplot

filepath = "data/SampleScreeningData.xlsx"
column_name = "Screenings"
our_name = "K"
output_name = "output/SampleScreeningBoxplot.html"

data = read_data_from_excel(filepath=filepath)
screenings = get_screenings(df=data, column_name=column_name)
our_number = get_our_screenings(df=data, column_name=column_name, our_name=our_name)

fig = create_screenings_boxplot(screenings_array=screenings, our_number=our_number)
fig.show()
fig.write_html(output_name)
