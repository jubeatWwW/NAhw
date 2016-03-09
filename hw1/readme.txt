WEATHER.PY

NAME
    weather.py - get the information of weather forecast

SYNOPSIS

    python weather.py [-h] [-l location] [-u unit] [-a | -c | -d day] [-s]

DESCRIPTION
    
    This manual page explains how to use this python script to print the weather forecast parsed from Yahoo Api. 

  Command Line Options
    
    -h
        Print help.
    -l location
        Get the weather forecast of the specified location, this argument could be a name of a city,a province, or a country.
        This argument is necessary if there is no config file exists.
    -u unit
        Specified the unit of temperature, 'c' for Centigrade and 'f' for Fahrenheit. Default is f.
    -c
        Show current condition.
    -d day
        Show the forecast, the argument should be number and must less or equal to 5.
    -a
        All information, equal to -c -d 5
    -s
        Show today's sunrise/sunset information

  Config File
    
    You can create a config file for a quick usage.
    Put the config.py in the same folder with weather.py file, and write the config in this file.
    There are two config can be specified, LOCATION and UNIT.

    Example:
        LOCATION=US
        UNIT=c
            ^^Note that there shouldn't be any space at the both side of `=`, 
    
    Then you are able to execute weather.py directly and it is the same as -l US -u c .
    When -l -u argument is specified in command line, the correspond config would lose efficacy during this execution.

NOTE
    This script could be executed by using ./weather,py or python2.7 weather.py command.
    If some problems happened because of the lack of package, try
    pip install urllib urllib2 argparse


YOUTUBE.PY

NAME
    youtube.py - get the search result of youtube

SYNOPSIS

    youtube.py [-h] [-n N] [-p P] keyword

DESCRIPTION
    
    This manual page explains how to use this python script to print the search results parsed from Youtube. 

  Command Line Options
    
    -h
        Print help.
    -n N
        The number of search result that should be printed, default is 5.
    -p P
        Choose the page of search result, default is the first page.

NOTE
    This script could be executed by using ./youtube,py or python2.7 youtube.py command.
    If some problems happened because of the lack of package, try
    pip install bs4 urllib urllib2 argparse lxml
    
    Because some channel have closed the comment function, and even the like/dislike infomation would also be hided.
    Also, some of the result is a link of channel, so sometimes this information would be an error message.

