import collections
import math

def calculate_entropy(text):
    if not text:
        return 0

    frequency = collections.Counter(text)
    n = len(text)
    entropy = - sum((count / n) * math.log2(count / n) for count in frequency.values())

    return entropy
