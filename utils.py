import datetime
import locale


def make_date(date_str):
    """
    Converts a date string in the format "YYYY-MM-DD" to "MMM DD, YYYY" format.

    Args:
        date_str (str): The date string in "YYYY-MM-DD" format.

    Returns:
        str: The converted date string in "MMM DD, YYYY" format.
    """
    date = datetime.datetime.strptime(date_str, "%Y-%M-%d")
    return date.strftime("%b %d, %Y")

def format_currency(value):
    """
    Converts a float value to a string representation of currency.

    Args:
        value (float): The value to be converted to currency.

    Returns:
        str: The string representation of the currency.
    """
    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
    return locale.currency(value, grouping=True)

def format_columname(colname):
    """
    Converts a column name to a more readable format.

    Args:
        colname (str): The column name to be converted.

    Returns:
        str: The converted column name.
    """
    return colname.replace("_", " ").title()