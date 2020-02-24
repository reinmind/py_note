import tensorflow as tf

def f():
    a = tf.constant('helloworld')
    sess = tf.Session()
    print(sess.run(a))
    print(tf.test.is_gpu_available())