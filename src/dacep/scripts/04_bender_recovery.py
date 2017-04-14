#!/usr/bin/env python

#____________________MOJE POZNAMKY______________________________________
#__1)__"cmd_vel" ustane publikovat, jakmile si bot nevi rady. Bylo by ji mozne tedy
# sledovat za ucelem zjisteni erroru, ale zaroven do ni musim publikovat....
# ALE da se zarucit, ze nebudu sledovat "cmd_vel", behem me publikace do nej 
#__2)__jak zajistit, ze mi nebude rusit moji publikaci "cmd_vel" uzel "move_base",
# ktery do ni puvodne ma publikovat - pomoci dalsiho skriptu, kam posilam True/False (ma ho Honza M)
# a ten rozhoduje, zda bude do 'cmd_vel' publikovat 'move_base' nebo on (Twist s recovery rychlosti)
#__3)__bylo by mozne zmenit(docasne) zadani - "goal" misto posilani "cmd_vel"
#__4)__nutno aby skript vyhodnotil nekolik hodnot behem jisteho casu, jinak by se mohlo
# stat, ze pouze bot prechazi pres nulu a pritom zacne recovery cyklus
#__5) snimat a posilat jen pouze pokud dostane zpravu - udelas tak ze inicializujes v cb pomocnou 
# promennou a pak ji na konci whilu znulujes. Do whilu vstoupi jen pokud je inicializovana. PRY NECHAT TAK, KDYZ FUNGUJE
# 
#____________________POPIS ALGORITMU____________________________________
# V prvni fazi by to mohlo fungovat nasledovne. Program kontroluje topic
# "/speed_actual" "/move_base/status", "/move_base/result" a
# "/move_base_simple/goal". Algoritmus je priblizne nasledujici. Pokud ma
# robot prikaz dojet nekam a jeste tam nedojel, kontroluj rychlost x a rotaci
# z. Pokud za poslednich treba 10 vterin robot neujel alespon 5 centimetru
# nebo se neotocil alespon o 10 stupnu, vysli do "/cmd_vel" po dobu 3 sekund prikaz
# k couvani. V prvni fazi klidne rovne, v dalsich etapach vyvoje pokud mozno
# do zatacky, aby si robot pomohl...
#
# ____________________POPIS TOPICU_______________________________________
# /speed_actual - Twist
# /move_base/status - actionlib_msgs/GoalStatusArray - posila 1-jede nebo 3-dosazeno ve "status" ... posila se porad
# /move_base/result - move_base_msgs/MoveBaseActionResult - posila se pri zmene stavu 2/3/4
# /move_base_simple/goal - geometry_msgs/PoseStamped - posle zadani pri zadani do topicu, ktery odposlouchava move_base

#____________________IMPORT KNIHOVEN____________________________________
import rospy
from geometry_msgs.msg import Twist
from actionlib_msgs.msg import GoalStatusArray
from move_base_msgs.msg import MoveBaseActionResult
from geometry_msgs.msg import PoseStamped
from geometry_msgs.msg import Twist
from std_msgs.msg import String
import numpy as np
from std_msgs.msg import Bool

#____________________DEFINICE FUNKCI____________________________________
# callback funkce jsou pouzity vzdy okamzite, kdyz se objevi nova zprava 
# v topicu ... vsimni si, ze se vypisuji nejdrive vsechny krom cmd_speed
# a cmd_speed az potom, co je do ni zapsano v cyklu recovery
def callback_speed(data):
    global speed
    speed = data
    print('cb_speed')
    
def callback_status(data):
    #global status
    #status = data.status_list.status # dela tam bordel, ptze nemuzu najit spravny format spravy
    print('cb_status')
    
def callback_result(data):
    global result
    result = data.status.status
    print('cb_result')
    
def callback_goal(data):
    global goal
    goal = data
    print('cb_goal')
    
def callback_cmd_speed(data):
    global cmd_speed
    cmd_speed = data
    print('cb_cmd_speed')

def my_recovery():
    #global speed, status, result, goal, speed_recovery, cmd_speed
    
    rospy.init_node('my_recovery', anonymous=True) # jak se jmenuje tenhle uzel - nemusi to byt nazev skriptu
    
    rospy.Subscriber("/speed_actual", Twist, callback_speed) # nazev topicu z nehoz odposlouchavam - speed_actual, ve formatu Twist, zpracovava to funkce callback_...
    rospy.Subscriber("/move_base/status", GoalStatusArray, callback_status) # /move_base/status; GoalStatusArray - K PREPSANI
    rospy.Subscriber("/move_base/result", MoveBaseActionResult, callback_result) # /move_base/result; MoveBaseActionResult - K PREPSANI
    rospy.Subscriber("/move_base_simple/goal", PoseStamped, callback_goal) # /move_base_simple/goal; PoseStamped
    rospy.Subscriber("/cmd_vel", Twist, callback_cmd_speed)
    
    pub = rospy.Publisher('/cmd_vel', Twist,queue_size = 10) # nazev topicu do nehoz posilam cmd_vel
    pubRecovery = rospy.Publisher('/dacep_recovery', Twist,queue_size = 10) # nazev topicu do nehoz posilam cmd_vel
    pubRecoveryInfo = rospy.Publisher('/dacep_recovery_info', Bool,queue_size = 10) # nazev topicu do nehoz posilam cmd_vel
    list_speed = list()
    list_cmd_speed = list()
    start_time = rospy.get_time()
    
    while not rospy.is_shutdown():
        print('my_recovery')
        try:
            #print(speed)
            #print(status)
            #print(result)
            #print(cmd_vel)
            #print(goal)
            #print(rospy.get_time())
            pass
        except:
            pass
        rospy.sleep(0.1)

# zjistim celkovou normu rychlosti pro porovnani se vstupnimi podminkami do recovery cyklu
        matrix_speed = np.array([[speed.linear.x, speed.linear.y, speed.linear.z],[speed.angular.x, speed.angular.y, speed.angular.z]]) # muzu znulovat ang x,y, lin z
        matrix_cmd_speed = np.array([[cmd_speed.linear.x, cmd_speed.linear.y, cmd_speed.linear.z],[cmd_speed.angular.x, cmd_speed.angular.y, cmd_speed.angular.z]])
        norm_speed = np.linalg.norm(matrix_speed)
        norm_cmd_speed = np.linalg.norm(matrix_cmd_speed)
        #print("norm_speed is %s" % norm_speed)
        #print("norm_cmd_speed is %s" % norm_cmd_speed)
        #print(type(status))
        #print(status == String())

# zjisteni klouzaveho prumeru pro normy rychlosti - abych okamzite neexekuoval
# recovery, ale opravdu odhalil zasekly moment
        avg_move = 40 # ZJISTIT kolik je idealni hodnota
        list_speed.append(norm_speed)
        list_cmd_speed.append(norm_cmd_speed)
        len_list_speed = len(list_speed)
        len_list_cmd_speed = len(list_cmd_speed)
        if len_list_speed > avg_move or len(list_cmd_speed) > avg_move:
            try:
                list_speed = list_speed[len_list_speed-avg_move:len_list_speed+1]
            except:
                pass
            try:
                list_cmd_speed = list_cmd_speed[len_list_cmd_speed-avg_move:len_list_cmd_speed+1]
            except:
                pass
        avg_speed = np.mean(list_speed)
        avg_cmd_speed = np.mean(list_cmd_speed)
        #print(len(list_speed))
        #print(len(list_cmd_speed))
        print("avg_speed is %s" % avg_speed)
        print("avg_cmd_speed is %s" % avg_cmd_speed)


# smycka obstaravajici zasilani recovery povelu do /cmd_vel - nemuze ji nijak narusit 
# zvyseni rychlosti jejim vlastnim zasahem!!!
        tol = 0.010 # tolerance pro normu rychlosti - ZJISTIT
        
        if avg_speed < tol and rospy.get_time() > (start_time + 10) and not result == 3: # and avg_cmd_speed < tol
            #speed_cmd = Twist()
            #speed_cmd.angular.z = cmd_speed.angular.z
            #speed_cmd.linear.x = -0.1
            print("Jsem v recovery cyklu")
            start_time = rospy.get_time()
            timeout = 2.5
            r = rospy.Rate(10) # 10hz ... posilam 10x za sekundu
            while (rospy.get_time() - start_time) < timeout:
                rospy.loginfo(True)
                pubRecoveryInfo.publish(True)
                #pubRecovery.publish(speed_cmd)
                r.sleep()
                
            '''    
            start_time = rospy.get_time()
            speed_cmd.linear.x = 0.1
            speed_cmd.angular.z = -speed_cmd.angular.z
            while (rospy.get_time() - start_time) < timeout:
                rospy.loginfo(True)
                pubRecovery.publish(speed_cmd)
                pubRecoveryInfo.publish(True)
                r.sleep()
            '''
        else:
            rospy.loginfo(False)
            pubRecoveryInfo.publish(False)

#____________________HLAVNI SMYCKA______________________________________
if __name__ == '__main__':
    global speed, status, result, goal, speed_recovery, cmd_speed
# definovat nezname (ikdyz jsou global) je treba, abych prosel bez erroru
# pokud nemam zadne zpravy z topicu 
    speed = Twist()
    #status = GoalStatusArray()
    result = 0 # je to integer
    goal = PoseStamped()
    cmd_speed = Twist()
    speed_recovery = Twist()
    speed_recovery.linear.x = -0.1

    try:
        my_recovery()
    except rospy.ROSInterruptException:
        pass


