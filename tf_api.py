#encoding: utf-8
# command to start tensorboard
# tensorboard --logdir="path/to/logs"

# 交换维度顺序
x = tf.Variables(img, name='x')
x = tf.transpose(x, perm=[1, 0, 2])

# reverse_sequence
# 详见http://learningtensorflow.com/lesson3/

# tf.split
# parameters: input, begin, size, name
# begin[i]表示第i抽取数据时从begin[i]开始
# size[i]表示第i维抽取的长度

# tf.expand_dims(tensor, dim)
# 为张量＋１维
# 假设t是一个shape为[2]的tensor
tf.shape(tf.expand_dim(t, 0)) # [1, 2]
tf.shape(tf.expand_dim(t, 1)) # [2, 1]

# tf.to_int32(), 转换数据格式

# tf.concat(values, axis, name='concat'), joined along axis
# for example
t1 = [[1, 2, 3], [4, 5, 6]]
t2 = [[7, 8, 9], [10, 11, 12]]
tf.concat([t1, t2], 0) ==> [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]

tf.concat([tf.expand_dims(t, axis) for t in tensors], axis)
# can be rewritten as
tf.stack(tensors, axis=axis)

# tf.dynamic_partition(data, partitions, num_partitions, name=None)
# Partitions data into num_partitions tensors using indices from partitions.
outputs[i].shape = [sum(partitions == i)] + data.shape[partitions.ndim:]
outputs[i] = pack([data[js, ...] for js if partitions[js] == i])

# for loop in tf
x = tf.Variable(0., name='x')
threshold = tf.constant(5.)
init_op = tf.global_variables_initializer()

with tf.Session() as session:
    session.run(init_op)
    while session.run(tf.less(x, threshold)):
        x = x + 1
        x_value = session.run(x)
        print(x_value)
