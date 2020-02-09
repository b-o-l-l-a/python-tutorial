def create_boolean_cols(df, col_name, new_col_name_prepend, sep = "|"):

    orig_col_vals_array = df[col_name].values
    orig_col_vals_array = [x for x in orig_col_vals_array if x == x]
    df[col_name] = df[col_name].astype(str)
    
    cats_concat = sep.join(orig_col_vals_array)
    unique_cats = list(set(cats_concat.split(sep)))
    
    print("\n-------------- start column name: {}".format(col_name))
    print("unique values:\n{}".format(unique_cats))
    
    col_prepend = "{}_".format(new_col_name_prepend)
    
    print("building out new boolean columns...")
    for cat in unique_cats:
    
        df["{col_prepend}{cat}_flg".format(**locals())] = \
            df.apply(lambda row: 
            True if cat in row[col_name] else False
        , axis=1)
        
    print("-------------- end column name: {}".format(col_name))
    return df