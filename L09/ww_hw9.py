"""HW9 for CUNY 602:  Advanced Programming Techniques, Spring 2017

__author__= 'Walt Wells'

Use the pandas module to answer the following questions about the EPA-HTTP data set.  
Print the result of each part to the console.  Use pandas as much as you can; 
this includes the data structure and the analysis.

* Which hostname or IP address made the most requests?
* Which hostname or IP address received the most total bytes from the server?  How many 
    bytes did it receive? 
* During what hour was the server the busiest in terms of requests?  (You can do this 
	by grouping each hour period (eg 13:00-14:00) Then count the number of requests in 
	each hour)
* Which .gif image was downloaded the most during the day?
* What HTTP reply codes were sent other than 200?

Use any other tools or techniques you need to create an efficient program.  These 
include scipy, numpy, regex, Tkinter, etc.

"""

import re
import pandas as pd 
from StringIO import StringIO

## Testing to find missing lines
# df = pd.read_csv('epa-http.txt', sep='\s+', header=None, error_bad_lines=False)

# using the error_bad_lines flag, we can see the line numbers where there are common errors.  in all cases, 
# of skipped lines, it looks like an extra ' " ' in the GET call.   let's remove and then setup our DF

with open('epa-http.txt', 'r') as f:
    raw = f.read()
pattern = r'(\" )(?=HTTP)'  
fixed = re.sub(pattern, '', raw) 
df = pd.read_csv(StringIO(fixed), sep='\s+', header=None, na_values="-",
    names = ['host', 'date', 'request', 'reply', 'bytes'])  

# clean for date to get hour
df['date'] = pd.to_datetime(df['date'], format='[%d:%H:%M:%S]')
df['hour'] = pd.DatetimeIndex(df['date']).hour
del df['date']

i = df.groupby('host').size()
i.sort_values(inplace=True, ascending=False)
i.columns = ['num_requests']
# start answering questions
print ''
print '1. Which hostname or IP address made the most requests?'
print ''
print i[:1].to_frame('num_requests')
print '_' * 80

g = df.groupby('host')['bytes'].sum()
g.sort_values(inplace=True, ascending=False)
print ''
print '2. Which hostname or IP address received the most total bytes from the server?'
print ''
print g[:1].to_frame('total_bytes')
print '_' * 80

h = df.groupby('hour').size()
h.sort_values(inplace=True, ascending=False)
print ''
print '3. During what hour was the server the busiest in terms of requests?'
print ''
print h[:1].to_frame('num_requests')
print '_' * 80

x = df.query('reply == 200')
x = x[x['request'].str.contains('GET') & x['request'].str.contains('.gif')]
x = x.groupby('request').size()
x.sort_values(inplace=True, ascending=False)
print ''
print '4. Which .gif image was downloaded the most during the day?'
print ''
print x[:1].to_frame('num_requests')
print '_' * 80

n = df.query('reply != 200')
n = n.groupby('reply').size()
n.sort_values(inplace=True, ascending=False)
print ''
print '5. What HTTP reply codes were sent other than 200?'
print ''
print n.to_frame('num_requests')
print '_' * 80
print ''
