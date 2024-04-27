def proverb(*input_data, qualifier=None):
    result_list = []
    for i in range(0, len(input_data)):
        if i == len(input_data) - 1:
            if qualifier is not None:
                result_list += [f"And all for the want of a {qualifier} {input_data[0]}."]
            else:
                result_list += [f"And all for the want of a {input_data[0]}."]
        else:
            result_list += [f"For want of a {input_data[i]} the {input_data[i + 1]} was lost."]
    return result_list
