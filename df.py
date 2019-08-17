def create_seperate_columns(df, max_of_tags, column, nan_value='notags'):
    new = df[column].str.split("|", expand=True)

    for i in range(0, max_of_tags):
        name = 'tag_' + str(i)
        df[name] = new[i]

    df.drop(columns=[column], inplace=True)
    df.fillna(nan_value, inplace=True)
    return df


def create_listed_columns(df, column):
    df[column] = df[column].str.split(".")
    return df
