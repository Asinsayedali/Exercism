def roman(num):
    if num >= 1000:
        return 'M' + roman(num - 1000)
    if num >= 900:
        return 'CM' + roman(num - 900)
    if num >= 500:
        return 'D' + roman(num - 500)
    if num >= 400:
        return 'CD' + roman(num - 400)
    if num >= 100:
        return 'C' + roman(num - 100)
    if num >= 90:
        return 'XC' + roman(num - 90)
    if num >= 50:
        return 'L' + roman(num - 50)
    if num >= 40:
        return 'XL' + roman(num - 40)
    if num >= 10:
        return 'X' + roman(num - 10)
    if num >= 9:
        return 'IX' + roman(num - 9)
    if num >= 5:
        return 'V' + roman(num - 5)
    if num >= 4:
        return 'IV' + roman(num - 4)
    if num >= 1:
        return 'I' + roman(num - 1)
    return ''