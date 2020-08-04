import os
import subprocess

class SkyhookRunner:
    '''
    A class that builds Skyhook CLI commands and executes them. 
    '''

    @classmethod
    def create_sk_cmd(cls, query, options):
        '''
        A function that generates the Skyhook CLI command from a Query Object. 
        '''
        command_args = [
            options['path_to_run_query'],
            
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

        skyhook_cmd = options['path_to_run_query']
        for arg in command_args:
            skyhook_cmd = ' '.join([skyhook_cmd, str(arg)])

        # return skyhook_cmd
        yield command_args

    @classmethod
    def execute_sk_cmd(cls, command_args):
        '''
        A function that executes a Skyhook CLI command. 
        '''
        # result = os.popen("cd " + command).read()
        # return result
        cmd_completion = subprocess.run(command_args, check=True, stdout=subprocess.PIPE)
        return cmd_completion.stdout

    @classmethod
    def run_query(cls, query, options): 
        '''
        A function that generates and executes a Skyhook CLI command starting from 
        a Query object. 
        '''
        command_args = create_sk_cmd(query, options)

        return self.execute_command(command_args)

    @classmethod
    def package_arrow_objects(cls):
        '''
        A function to coordinate the joining of arrow objects return from a Skyhook CLI 
        command execution. 
        '''
        raise NotImplementedError
