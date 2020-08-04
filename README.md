# SkyhookDM SQL Interface

A python frontend for interfacing with SkyhookDM that generates query commands via SQL statements. It is asssumed that 
you have already completed the build steps to make SkyhookDM-Ceph and are ready to run test queries. 

## How to run 

* Run `run_tests.sh` to run tests.

* Run `start_client.sh` to run the client 

* For custom options do not run `start_client.sh`, and instead run `python3 -m skyhooksql.client -h` to show options. 
