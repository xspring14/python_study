# with a total word list and the list contains articles composed by word and count
# to build a matrix by row is the aritcle and column is the word

# for example:
articlew=[{'a':3,'b':4},{'a':2,'c':1},{'b':1, 'c':4}]
wordvec=['a','b','c']
l=[[(word in f and f[word] or 0) for word in wordvec] for f in articlew]

# output
l=[[3, 4, 0], [2, 0, 1], [0, 1, 4]]


# for cross validation, here k = 3 
X_folds = np.array_split(X_digits, 3)
y_folds = np.array_split(y_digits, 3)

for k in range(3):
  X_train = X_folds
  X_test = X_train.pop(k)
  X_train = np.concatenate(X_train)
  
  y_train = y_folds
  y_test = y_train.pop(k)
  y_train = np.concatenate(y_train)

# convet the num string to a num list
nums = '1 2 3 4 5'
data = map(int, nums.split())
>>> data = [1, 2, 3, 4, 5]


# sort the dict by key or by value, reverse=True means sort descending, or not.
# by key
d = sorted(d.items(), key=lambda item: item[0], reverse=True)

# by value
d = sorted(d.items(), key=lambda item: item[1], reverse=True)

# another method
import operator
# by key
d = sorted(d.iteritems(), key=operator.itemgetter(0), reverse=True)
# by value
d = sorted(d.iteritems(), key=operator.itemgetter(1), reverse=True)

# 返回的是排序好的list,每项为一个元祖(key, value)
