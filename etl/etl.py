def transform(legacy_data):
    ##list_new = []
    dict_new = {}
    for key, values in legacy_data.items():
        for elements in values:
            dict_new[elements.lower()] = key
    return dict_new
