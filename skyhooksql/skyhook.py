import os

class SkyhookRunner:
    def __init__(self):
        '''
        A class that 
        '''
        self.default_path = "~/skyhookdm-ceph/build/ && bin/run-query"

    def create_sk_cmd(self, query, options):
        '''
        A function that generates the Skyhook CLI command from a Query Object. 
        '''
        command_args = [
            '--num-objs'   , options['num-objs'],
            '--pool'       , options['pool'],
            '--oid-prefix' , "\"{}\"".format(options['oid-prefix']),
            '--table-name' , "\"{}\"".format(query['table-name'])
        ]

        if options['header']:
            command_args.append("--header")

        if options['cls']:
            command_args.append("--use-cls")

        if options['quiet']:
            command_args.append("--quiet")

        if query['projection']:
            projection = query['projection'].replace(' ','')
            command_args.append("--project \"{}\" ".format(projection))

        if query['selection']:
            # TODO: Make order here not matter. Maybe dicts? 
            if len(query['selection']) == 3:
                command_args.append("--select \"{0},{1},{2}\" ".format(query['selection'][1],
                                                                        query['selection'][0],
                                                                        query['selection'][2]))

        skyhook_cmd = self.default_path
        for arg in command_args:
            skyhook_cmd = ' '.join([skyhook_cmd, str(arg)])

        return skyhook_cmd


    def execute_sk_cmd(self, command):
        '''
        A function that executes a Skyhook CLI command. 
        '''
        result = os.popen("cd " + command).read()
        return result

    def run_query(self, query): 
        '''
        A function that generates and executes a Skyhook CLI command starting from 
        a Query object. 
        '''
        cmd = create_sk_cmd(query)

        result = self.execute_command(cmd)
        
        return result

    def package_arrow_objects(self):
        '''
        A function to coordinate the joining of arrow objects return from a Skyhook CLI 
        command execution. 
        '''
        raise NotImplementedError
