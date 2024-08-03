import re

# Matching a date pattern (YYYY-MM-DD)
date_pattern = re.compile(r'\d{4}-\d{2}-\d{2}')
text = 'Today is 2023-12-14 and tomorrow is 2023-12-15.'

matches = date_pattern.findall(text)
print(matches)
