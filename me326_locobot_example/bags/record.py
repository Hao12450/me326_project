   1 import rosbag
   2 bag = rosbag.Bag('true_2023-02-04-12-36-43.bag')
   3 for topic, msg, t in bag.read_messages(topics=['chatter', 'numbers']):
   4     print(msg)
   5 bag.close()
