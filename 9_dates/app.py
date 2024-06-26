import datetime

current_date_time = datetime.datetime.now()
print(current_date_time)

print("Year:", current_date_time.year)
print("Month:", current_date_time.month)
print("Day:", current_date_time.day)

print(datetime.date.today())

# year month day
custom_date = datetime.datetime(2001, 4, 7)
print(custom_date.date())

print("==========================================")

"""
The strftime() Method
The datetime object has a method for formatting date objects into readable strings.

The method is called strftime(), and takes one parameter, format, to specify the format of the returned string:
%a	Weekday, short version	Wed	
%A	Weekday, full version	Wednesday	
%w	Weekday as a number 0-6, 0 is Sunday	3	
%d	Day of month 01-31	31	
%b	Month name, short version	Dec	
%B	Month name, full version	December	
%m	Month as a number 01-12	12	
%y	Year, short version, without century	18	
%Y	Year, full version	2018	
%H	Hour 00-23	17	
%I	Hour 00-12	05	
%p	AM/PM	PM	
%M	Minute 00-59	41	
%S	Second 00-59	08	
%f	Microsecond 000000-999999	548513	
%z	UTC offset	+0100	
%Z	Timezone	CST	
%j	Day number of year 001-366	365	
%U	Week number of year, Sunday as the first day of week, 00-53	52	
%W	Week number of year, Monday as the first day of week, 00-53	52	
%c	Local version of date and time	Mon Dec 31 17:41:00 2018	
%C	Century	20	
%x	Local version of date	12/31/18	
%X	Local version of time	17:41:00	
%%	A % character	%	
%G	ISO 8601 year	2018	
%u	ISO 8601 weekday (1-7)	1	
%V	ISO 8601 weeknumber (01-53)	01

"""

formatted_date = (custom_date.strftime("%A ") +
                  custom_date.strftime("%B ") + custom_date.strftime("%Y ") +
                  custom_date.strftime("%H ") + custom_date.strftime("%M "))

print(formatted_date)
