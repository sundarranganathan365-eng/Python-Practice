import re
from collections import Counter

text = """
Python is great, and Python is fun. 
AI with Python is the future. Python everywhere!
"""

words = re.findall(r"\b\w+\b", text.lower())
freq = Counter(words)

print("Top 3 most common words:")
for word, count in freq.most_common(3):
    print(word, "→", count)
