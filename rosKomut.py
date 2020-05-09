import rospy
from  geometry_msgs.msg import Twist

rospy.init_node('burak_bilge_node')

publisher_turtlebot = rospy.Publisher('/cmd_vel_mux/input/navi', Twist, queue_size = 1)

movement = Twist()

movement.linear.x = 0.0
movement.linear.y = 0.0
movement.linear.z = 0.0
movement.angular.x = 0.0
movement.angular.y = 0.0
movement.angular.z = 0.0

f = open("/home/burak/PycharmProjects/sesDeneme/sesKomutu.txt", "r")

while not rospy.is_shutdown():
    text = f.read()
    if text == "come":
        movement.linear.x = 0.06
    elif text == "go":
        movement.linear.x = -0.06
    elif text == "stop":
        movement.linear.x = 0
        movement.angular.z = 0
    elif text == "turn around":
        movement.angular.z = -0.2
    f.flush()
    publisher_turtlebot.publish(movement)
