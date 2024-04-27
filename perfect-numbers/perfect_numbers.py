def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    sum=0
    if number<1:
        raise ValueError("Classification is only possible for positive integers.")
    for i in range(1,number):
        if number%i==0:
            sum = sum +i

    if sum ==number:
        result="perfect"
        return result
    elif sum>number:
        result="abundant"
        return result
    else :
        result="deficient"
        return result