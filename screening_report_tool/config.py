import yaml

with open("screening_report_tool/config.yml", "r") as f:
    config = yaml.safe_load(f)

root = config["production"]["root"]
filename = config["production"]["filename"]
testing_filepath = config["testing_filepath"]

screening_column_name = config["screening_column_name"]
our_row_name = config["our_row_name"]
total_row_name = config["total_row_name"]

