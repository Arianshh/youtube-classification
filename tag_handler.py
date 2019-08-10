def create_seperate_tags(df, max_of_tags):
    new = df["tags"].str.split(".", expand = True)

    for i in range(0, max_of_tags):
        name = "tags"+str(i)
        df[name] = new[i]

    # Dropping old tags columns
    df.drop(columns =["tags"], inplace = True)
    df.fillna("notags", inplace = True)
    return df


def create_listed_inputs(df):
    # new data frame with split value columns
    df["tag"]= df["tag"].str.split(".", expand = True)

    return df
