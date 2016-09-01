import re

pattern = re.compile(r'\d+')
print re.findall(pattern, 'one11two2three3four4')

### output ###
# ['11', '2', '3', '4']
