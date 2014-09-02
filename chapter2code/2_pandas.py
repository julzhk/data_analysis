import pprint
import json
from pandas import DataFrame
path = 'usagov_bitly_data_sample.json'
records = [json.loads(line) for line in open(path)]
frame = DataFrame(records)
# pprint.pprint(records)
print frame['tz'][:10]
    # 0       Europe/London
    # 1
    # 2       Asia/Calcutta
    # 3
    # 4      Asia/Hong_Kong
    # 5       Europe/Moscow
    # 6    America/New_York
    # 7           Asia/Baku
    # 8       Europe/London
    # 9
    # Name: tz, dtype: object

tz_counts = frame['tz'].value_counts()
print tz_counts[:10]
lean_tz = frame['tz'].fillna('Missing')
print lean_tz[:10]
clean_tz[clean_tz == ''] = 'Unknown'
lean_tz = clean_tz.value_counts()
print lean_tz[:10]