def create_seperate_columns(df, max_of_tags, column, nan_value='notags'):
    new = df[column].str.split(".", expand = True)

    for i in range(0, max_of_tags):
        name = column+str(i)
        df[name] = new[i]

    # Dropping old tags columns
    df.drop(columns =[column], inplace = True)
    df.fillna(nan_value, inplace = True)
    return df


def create_listed_columns(df, column):
    # new data frame with split value columns
    df[column]= df[column].str.split(".", expand = True)

    return df
