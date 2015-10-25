import doctest

from ofxstatement.plugins.woolworthsmoney import WoolworthsMoneyParser

def docest_WoolworthsMoneyParser():
    """Test WoolworthsMoneyParser

    Open sample csv
        >>> import os
        >>> csvfile = os.path.join(os.path.dirname(__file__), 'samples',
        ...                       'woolworthsmoney.csv')

    Create parser object and parse:
        >>> fin = open(csvfile)
        >>> parser = WoolworthsMoneyParser(fin)
        >>> statement = parser.parse()

    Check what we've got:
        >>> len(statement.lines)
        4

    Check first line:
        >>> l = statement.lines[0]
        >>> l.amount
        10.99
        >>> l.payee.strip()
        'Edmund Barton'
        >>> l.date
        datetime.datetime(2001, 1, 1, 0, 0)

    Check credit line:
        >>> l = statement.lines[2]
        >>> l.amount
        -3.14
        >>> l.payee.strip()
        'Crocodile Dundee'
        >>> l.date
        datetime.datetime(2015, 9, 11, 0, 0)

    """

def test_suite(*args):
    return doctest.DocTestSuite(optionflags=(doctest.NORMALIZE_WHITESPACE|
                                             doctest.ELLIPSIS|
                                             doctest.REPORT_ONLY_FIRST_FAILURE|
                                             doctest.REPORT_NDIFF
                                             ))

load_tests = test_suite

if __name__ == "__main__":
    import doctest
    doctest.testmod()
