# API
In API Automation Framework we follow the architechture somthing like the following:
(USER)------>[tests/all_testcases.py --> conftest.py --> (config.py, client/client.py)]

We run the the testcases we have defined in the test folder here testcases have the assrestions but its functionality is defined in the conftest.py here in conftest.py we needed config.py where all the global varialbes are stored and also config file depends on the client.py cz it contains the builtin modified requests
