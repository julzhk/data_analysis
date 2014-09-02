A simple approach
=====

By using Bit.ly access data for US .gov site: http://www.usa.gov/About/developer-resources/1usagov.shtml
we can easily step through downloaded data files with a list comprehension:

```
import json
path = 'usagov_bitly_data_sample.json'
records = [json.loads(line) for line in open(path)]
```

Alternatively, we can use the Pandas Library: pip install pandas
```
from pandas import DataFrame
frame = DataFrame(records)
```
A dataframe is a 'data table'

hence : frame['tz'][:10] gives the first ten timezones.
Pandas dataframes have many useful methods:
```
>>>tz_counts = frame['tz'].value_counts()
America/New_York       1251
                        521
America/Chicago         400
America/Los_Angeles     382
America/Denver          191
...
```
Clean the gaps in the data:

```
> lean_tz = frame['tz'].fillna('Missing')
> clean_tz[clean_tz == ''] = 'Unknown'
> tz_counts = clean_tz.value_counts()
America/New_York       1251
Unknown                 521
America/Chicago         400
America/Los_Angeles     382
America/Denver          191
```

And to make a chart:
``` tz_counts[:10].plot(kind='barh', rot=0)
