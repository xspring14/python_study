# with a total word list and the list contains articles composed by word and count
# to build a matrix by row is the aritcle and column is the word

# for example:
articlew=[{'a':3,'b':4},{'a':2,'c':1},{'b':1, 'c':4}]
wordvec=['a','b','c']
l=[[(word in f and f[word] or 0) for word in wordvec] for f in articlew]

# output
l=[[3, 4, 0], [2, 0, 1], [0, 1, 4]]
