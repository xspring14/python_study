# 统计各时区数量
# method1
def get_counts(seq):
    counts = {}
    for x in seq:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1
    return counts

# 使用defaultdict初始化
from collections import defaultdict
def get_counts2(seq):
    counts = defaultdict(int)
    for x in seq:
        counts[x] += 1
    return counts

# 得到计数前10位的时区
def top_counts(count_dict, n=10):
    value_key_pairs = [(count, tz) for tz, count in count_dict.items()]
    value_key_pairs.sort()
    return value_key_pairs[-n:]

# 使用collections.Counter得到前10位的时区
from collections import Counter
counts = Counter(seq)
counts.most_common(10)
