import tensorflow as tf


def f():
    cube = tf.constant([
        [[1, 2, 3], [3, 4, 5], [6, 7, 8]],
        [[1, 2, 3], [3, 4, 5], [5, 6, 7]]
    ], name='cube')
    matrix = tf.constant([
        [1, 2, 3],
        [4, 5, 6]
    ], name='matrix')
    vector = tf.constant([4, 5, 6, 7])
    scalar = tf.constant(1)
    print(cube.get_shape())
    print(matrix.get_shape())
    print(vector.get_shape())
    print(scalar.get_shape())
    sess = tf.Session()
    print(sess.run(cube)[1, 1, 1])
