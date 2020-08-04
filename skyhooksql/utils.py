import argparse
import re
import sys

# ------------------------------
# Utility methods
def print_help_msg():
    print( 
'''
Skyhook SQL Client Application\n

To show this message enter:     'help'
To quit this application enter: 'quit' 

Options:\n \t -n [--num-objs]\n \t -p [--pool]\n \t -q [--quiet]\n \t -c [--use-cls] 

Supported syntax:
\t Projections (EXAMPLE: SELECT orderkey FROM lineitem)
\t Selections  (EXAMPLE: SELECT orderkey FROM lineitem WHERE orderkey<3;)
\t Show Schema (EXAMPLE: DESCRIBE TABLE lineitem)
'''
)


def print_intro_msg():
    print('{:^100}'.format("Welcome to the Skyhook SQL Client Application")) 
    print('{:^100}'.format("---------------------------------------------"))
    print('{:^100}'.format("(Enter 'help' for a brief summary of supported commands)\n"))
    print("Enter a SQL query (multiple semi-colon separated queries can be accepted).")

def prompt(curr_mode):
    i = input("Enter a supported SQL query: \n")
    return i

# ------------------------------
# Utility classes
class ArgparseBuilder(object):
    def __init__(self, **kwargs):
        super(ArgparseBuilder, self).__init__(**kwargs)
        
        self.arg_parser = argparse.ArgumentParser(usage='usage: python3 -m skyhooksql.client | ./start_client.sh')
        self.arg_parser.add_argument('-c', 
                                '--use-cls', 
                                dest='use-cls', 
                                action='store_false', 
                                default=True, 
                                help='push execution onto storage servers using object classses')
        self.arg_parser.add_argument('-q', 
                                '--quiet', 
                                dest='quiet',
                                action='store_true', 
                                default=False, 
                                help='see summary of query results only')
        self.arg_parser.add_argument('-n', 
                                '--num-objs', 
                                dest='num-objs',
                                nargs=1,
                                default=2, 
                                type=int,
                                help='number of storage objects')
        self.arg_parser.add_argument('-p',
                                '--pool',
                                dest='pool',
                                nargs=1,
                                default='tpchdata',
                                type=str,
                                help='name of object pool')
        self.arg_parser.add_argument('-s',
                                '--schema',
                                dest='header',
                                nargs=1,
                                default=True,
                                help='show schema of query result')
        self.arg_parser.add_argument('-b',
                                '--binary',
                                dest='path_to_run_query',
                                nargs=1,
                                default='~/skyhookdm-ceph/build/ && bin/runquery',
                                help='Path to run-query binary. Include && bin/run-query.')
        self.arg_parser.add_argument('-o',
                                '--oid-prefix',
                                dest='oid-prefix',
                                nargs=1,
                                type=str,
                                default='public',
                                help='')
        self.args = vars(self.arg_parser.parse_args())

class PredefinedCommands():
    def __init__(self):
        self.Predefined = None

    def describe_table(self, table_name):
        return {'describe': "bin/run-query --num-objs 2 --pool tpchdata --oid-prefix \"public\" --table-name \"{0}\" --header --limit 0;".format(table_name)}