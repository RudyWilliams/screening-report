class Data:
    def __init__(self, df, screening_column, our_name):
        self.df = df
        self.screening_column = screening_column
        self.our_name = our_name
        self.screenings_array = None
        self.n_screenings_us = None
        self.n_screenings_rest = None
        self.us_array = None
        self.rest_array = None
        self.us_prop_array = None
        self.rest_prop_array = None

    @property
    def problems(self):
        return self.df.columns.values[:-1]

    def set_screenings_array(self):
        self.screenings_array = self.df[self.screening_column].values[:-1]
        return self

    def set_us_data(self):
        us_data = self.df.loc[self.our_name, :].values
        us_array, n_screenings_us = us_data[:-1], us_data[-1]
        self.us_array = us_array
        self.n_screenings_us = n_screenings_us
        self.us_prop_array = us_array / n_screenings_us
        return self

    def set_rest_data(self, total_row_name):
        _df = self.df.copy()
        not_us = ~(_df.index == self.our_name) & ~(_df.index == total_row_name)
        rest_df = _df.loc[not_us, :]
        rest_agg_array_with_screenings = rest_df.sum(axis=0).values
        rest_array, n_screenings_rest = (
            rest_agg_array_with_screenings[:-1],
            rest_agg_array_with_screenings[-1],
        )
        self.rest_array = rest_array
        self.n_screenings_rest = n_screenings_rest
        self.rest_prop_array = rest_array / n_screenings_rest
        return self


if __name__ == "__main__":

    import pandas as pd

    df = pd.read_excel("data/SampleScreeningData.xlsx", index_col=0)
    data = Data(df=df, screening_column="Screenings", our_name="K")
    data.set_screenings_array()
    # print(data.screenings_array)
    data.set_us_data()
    print(data.us_array)
    print(data.n_screenings_us)
    print(data.us_prop_array)

    data.set_rest_data(total_row_name="Total")
    print(data.rest_array)
    print(data.n_screenings_rest)
    print(data.rest_prop_array)
