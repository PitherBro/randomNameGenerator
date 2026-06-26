# **!!Still Incomplete!!**

# How to use

Simply run the bash script file `run-linux` to run program from local `.venv` dirctory

**Currently** you can pass:
>
>`3 1969 100`
>
>for 100 random first and last names from 1969
>
>`3 1969 0 100`
>
>for 100 girl first and last names from 1969
>
>`3 1969 1 100`
>
>for 100 boy first and last names from 1969

As a full command:
> `bash run-linux 3 1969 1 100`
>
> will make 100 boy first and last names from 1969

Outputs are dumped as `json` and `html` under `/temp/*type*` with an embedded css styling from `style.css`

## All information is randomly generated based off information from this [Repo](https://github.com/aruljohn/popular-baby-names.git)
> Thank you Aruljohn for providing a comprohensive data set.

## Plan
- make a local embeded pyton distibution to run on any platform
- ref local python to run name gen
- modules from several sources
- each module has self checking data set.

## As it stands
- works on linux, assumes python3 is installed.
- uses  [github repository](https://github.com/aruljohn/popular-baby-names.git) of names from 1880-2022 as data source.
- [DB_ZIP_FILE](https://github.com/aruljohn/popular-baby-names/archive/refs/heads/master.zip)

## TODO
- add logic to do an option base off menu selction
- finish console command logic to complete opperations if passed as param
- consolidate common vars and libs into common.py


----
----


- completed user input for case 1.
- add in console input for case 1
- add in automated input for case 3
- add in automated input for case 4
- universally validate the console commands assuming the first arg is a menu selection.


## Possible Adjustments
- batch thread program to rescan a few copies of file to reduce latency.
- consider using a copy of file object rather than re-reading the same file x times.
- http API server to request a person or random name as GET response.
- add in automatic download, extraction, consolidation of master file on mondule load as main. via system calls from main file.
