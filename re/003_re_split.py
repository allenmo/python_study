import re

pattern = re.compile(r'\d+')
print re.split(pattern, 'one11two2three3four4')

### output ###
# ['one', 'two', 'three', 'four', '']
