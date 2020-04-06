from collections import Counter
import re
path='sample.txt'
words=re.findall('\w+',open(path).read())
print(Counter(words).most_common(20))
