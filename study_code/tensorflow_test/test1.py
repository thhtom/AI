import tensorflow as tf



# sess = tf.Session()
#
# result = sess.run(product)
#
# print (result)

# sess.close()

with tf.Session() as sess:
    # with tf.device("/cpu:1"):
       a = tf.constant([[3.,3.]])

       b = tf.constant([[2.],[2.]])

       product = tf.matmul(a,b)
       result = sess.run([product])
       print (result)
