from .parser import SQLParser
from .skyhook import SkyhookRunner

class Query():
    """A class that represents a mutable SQL query object."""

    def __init__(self):        
        self.statement = ''

        self.options = {'cls'              : True,
                        'quiet'            : False,
                        'header'           : True,
                        'pool'             : 'tpchdata',
                        'num-objs'         : '2',
                        'oid-prefix'       : 'public',
                        'path_to_run_query': '~/skyhookdm-ceph/build/ && bin/run-query'}

        self.query = {'selection'  : '',
                      'projection' : '',
                      'table-name' : ''}
        
        self.results = None

    def sql(self, statement):
        """Parses SQL statement and sets Query object parameters. 

        Arguments:
        statement -- A string parsed as an unvalidated SQL statement
        """
        self.statement = statement
        parsed = SQLParser.parse_query(statement)
        self.set_table_name(parsed['table-name'])
        self.set_projection(parsed['projection'])
        self.set_selection(parsed['selection'])

    def run(self):
        """A function that executes the Skyhook CLI command by calling the run-query binary."""
        self.results = SkyhookRunner.run_query(self.query, self.options)

    def lifetime(self, statement):
        """A function that performs a full query execution. 

        Arguments:
        statement -- A string parsed as an unvalidated SQL statement
        """
        query = SQLParser.parse_query(statement)

        self.set_projection(query['projection'])
        
        self.set_selection(query['selection'])

        self.set_table_name(query['table-name'])

        self.create_sk_cmd()

        self.run()

    def set_selection(self, *args):
        """Sets the selection parameter for a query.

        Arguments:
        args -- 
        """
        for arg in args:
            if not isinstance(arg, str):
                raise NotImplementedError
            self.query['selection'] = arg.split(', ')

    def set_projection(self, *args):
        """Sets the projection parameter for a query.

        Arguments:
        args -- A comma separated string of names of attributes
        """
        for arg in args:
            if not isinstance(arg, str):
                raise NotImplementedError
            self.query['projection'] = arg

    def set_table_name(self, *args):
        """Sets the table name parameter for a query.

        Arguments:
        args -- A comma separated string of names of tables
        """
        for arg in args:
            if not isinstance(arg, str):
                raise NotImplementedError
            self.query['table-name'] = arg

    def set_option(self, option, value):
        """ Sets the option to be the given value.

        Arguments:
        option -- 
        value  -- 
        """
        if option not in self.options.keys():
            print("Error: Not an option")
            return
        self.options[str(option)] = value 

    def show_query(self):
        """ A function that shows the current Query object."""
        print(self.query)

    def show_options(self):
        """ A function that shows the current options being used."""
        print(self.options)

    def show_results(self):
        """ A function that shows the results of the previously ran query."""
        print(self.results)

    def show_sk_cmd(self):
        """ A function that shows the Skyhook CLI command representation of the query object."""
        sk_cmd = SkyhookRunner.create_sk_cmd(self.query, self.options)
        print(sk_cmd)

    def generate_pyarrow_dataframe(self):
        """An example of what may be done in the near future."""
        raise NotImplementedError
