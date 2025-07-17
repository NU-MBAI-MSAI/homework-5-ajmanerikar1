"""

In the problem2 module, create a function named date_format that takes one argument,
a string, that is in the format MM/DD/YYYY.
The function should the date formatted as YYYY-MM-DD.
"""

def date_format(s):
    #Convert date from "mm/dd/yyyy" to "yyyy-mm-dd"
    months = s[0:2]
    days = s[3:5]
    years = s[6:]
    reversed_date = years + '-' + months + '-' + days
    return reversed_date
