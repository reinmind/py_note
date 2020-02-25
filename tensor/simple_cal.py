# 1+2+3+4+5+6+...+10
import tensorflow as tf

logdir = '/home/reinmind/log'
tf.reset_default_graph()
b = tf.constant(1, name='b')
a = tf.Variable(0, dtype=tf.int32, name='a')
c = tf.add(a, b, name='c')
a_inc = tf.assign(a, c, name='a_inc')
sum1 = tf.Variable(0, dtype=tf.int32, name='sum1')
d = tf.add(sum1, a, name='d')
sum1_inc = tf.assign(sum1, d, name='sum_inc')
init_op = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init_op)
    for _ in range(10):
        sess.run(a_inc)
        sess.run(sum1_inc)
        print(sum1.eval())
        writer = tf.summary.FileWriter(logdir, tf.get_default_graph())
