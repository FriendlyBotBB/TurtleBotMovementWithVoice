import speech_recognition as sr
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

r = sr.Recognizer()
while not rospy.is_shutdown():
    publisher_turtlebot.publish(movement)
    with sr.Microphone() as source:
        print("Speak Anything :")
        a = r.listen(source)
        try:
            text = r.recognize_google(a)
            if(text == "come here" or text == "come" ):
                movement.linear.x = 1
                print "geliyor"
            elif(text == "go away" or text == "go" ):
                movement.linear.x = -1
                print "gidiyor"
        except:
            print("Sorry could not recognize what you said")