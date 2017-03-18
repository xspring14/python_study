#encoding:utf-8
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

# 求一个行向量与一个矩阵各行的欧氏距离
dataSetSize = dataSet.shape[0]
diffMat = np.tile(inX, (dataSetSize, 1)) - dataSet
sqDiffMat = diffMat ** 2
sqDistance = sqDiffMat.sum(axis=1)
distances = sqDistance ** 0.5


# 根据轨迹序列画轨迹图
from PIL import Image
from PIL import ImageDraw

def draw(points):
  im = Image.fromarray(np.zeros((64, 64)))
  draw = ImageDraw.Draw(im)
  for i in xrange(0, points.shape[0]-1):
    draw.line((tuple(points[i+1]), tuple(points[i])), fill=255)
  # 显示图片
  im.convert('RGB').show()
  # 保存图片
  im.convert('RGB').save('img.jpg', 'JPEG') # save时，im必须先convert
  
  

# 取列表的倒数k个元素,并倒序返回
a = range(10)
a[:-(k + 1):-1]
# 若k=5, 返回的为[9, 8, 7, 6, 5]

# 关于np.nonzero(), 放回bool为True的index
# a 为np.array时，np.nonzero(a[0, :] == var)[0]
# a 为np.mat时，np.nonzeros(a[0, :] == var)[1]
