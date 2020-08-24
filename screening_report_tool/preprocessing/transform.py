def get_screenings(df, column_name):
    # this assumes that the df has the form of the
    # Total column being on the bottom of the df
    return df[column_name][:-1]


def get_our_screenings(df, column_name, our_name):
    return df.loc[our_name, column_name]
