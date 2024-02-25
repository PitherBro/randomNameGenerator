# How to use

**!!Still Incomplete!!**

Simply run the bash script file to run program from local `.venv` dirctory

Later you can also pass numerical value (1-3) to automaticly generate a name, person, or list of people along with relevant data required.

All information is randomly generated based off information from this [Repo](https://github.com/aruljohn/popular-baby-names.git)

# Plan
- make a local embeded pyton distibution to run on any platform
- ref local python to run name gen
- modules from several sources
- each module has self checking data set.

# As it stands
- works on linux, assumes python3 in installed.
- uses  [github repository](https://github.com/aruljohn/popular-baby-names.git) of names from 1880-2022 as data source.

# TODO
- add logic to do an option base off menu selction
- finish console command logic to complete opperations if passed as param
- consolidate common vars and libs into common.py

# Possible Adjustments
- batch thread program to rescan a few copies of file to reduce latency.
- http API server to request a person or random name as GET response.
- add in automatic download, extraction, consolidation of master file on mondule load as main. via system calls from main file.
- consider using a copy of file object rather than re-reading the same file x times.