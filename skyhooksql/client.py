from .query import Query
from .utils import ArgparseBuilder, prompt, print_help_msg

class Client():
    '''
    A simple client to access the SQL Query object 
    '''
    def __init__(self, opts):
        self.q = Query()
        
        for opt in opts:
            self.q.set_option("","") # TODO: Setup options here 

    def run(self):
        user_input = prompt()
        
        while True: 
            if user_input == 'quit':
                self._quit()
            elif user_input == 'help':
                self._help()
            else:
                self._query(user_input)

    def _query(self, user_input):
        self.q.sql(user_input)
        self.q.run()
        self.show_results()

    def _quit(self):
        quit()

    def _help(self):
        print_help_msg()

def main():
    argparse_obj = ArgparseBuilder() 

    c = Client(argparse_obj)
    
    c.run()

if __name__ == "__main__":
    main()
