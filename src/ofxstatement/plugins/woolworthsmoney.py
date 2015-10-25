from ofxstatement.plugin import Plugin
from ofxstatement.parser import StatementParser, CsvStatementParser
from ofxstatement.statement import StatementLine

class WoolworthsMoneyPlugin(Plugin):
    """Woolworths Money (Australia) plugin
    """

    def get_parser(self, filename):
        f = open(filename)
        return WoolworthsMoneyParser(f)


class WoolworthsMoneyParser(CsvStatementParser):

    date_format = "%d %b %y"
    mappings = {
            "date": 0,
            "payee": 2,
            "amount": 4,
            }

    def parse_record(self, line):
        if self.cur_record == 1:
            return None

        if line[0] == 'Pending' or line[1] != 'Processed':
            return None

        if len(line[3]) > 0:
            line[4] = "-" + line[3]

        return super(WoolworthsMoneyParser, self).parse_record(line)
