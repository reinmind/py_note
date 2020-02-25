import tensorflow as tf

logdir = '/home/reinmind/log'


def f_log_init():
    # clean graph
    tf.reset_default_graph()


def f_log_draw():
    writer = tf.summary.FileWriter(logdir, tf.get_default_graph())
    writer.close()


def f1():
    input1 = tf.constant([1.0, 2.0, 3.0], name='input1')
    input2 = tf.Variable([2.0, 3.0, 4.0], name='input2')
    sum1 = tf.add_n([input1, input2], name='add')


def f2():
    f_log_init()
    node1 = tf.constant(3.0, name='node1')
    node2 = tf.constant(4.0, name='node2')
    node3 = tf.add(node1, node2, name='node3')
    f_log_draw()
