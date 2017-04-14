#include <ros/ros.h>
#include <tf/transform_broadcaster.h>

#include "sensor_msgs/Range.h"
#include "sensor_msgs/LaserScan.h"

// variables
int srf08_id;

// variables for publishers
sensor_msgs::LaserScan SRF08_1;

// publishers
ros::Publisher SRF08_1_pub;

void cmd_vel_callback(const sensor_msgs::Range data)
{ 
// srf08_id je variable ... nahore
    switch (srf08_id) {
        case 1:
            for (int i = 0; i < 5; i++) {
                SRF08_1.ranges[i] = data.range;
            }
            SRF08_1_pub.publish(SRF08_1);
            break;
    }
}

int main(int argc, char** argv)
{   
    srf08_id = 1;
    
    ros::init(argc, argv, "srf08_2_SRF08");
    
    ros::NodeHandle n;       
    
    SRF08_1_pub = n.advertise<sensor_msgs::LaserScan>("SRF08_1", 10); 
    
    SRF08_1.header.frame_id = "srf08_1";
    SRF08_1.range_min = 0.03;
    SRF08_1.range_max = 6.00;
    SRF08_1.angle_min = -0.4;
    SRF08_1.angle_max =  0.4;
    SRF08_1.angle_increment = 0.2;
    SRF08_1.ranges.resize(5);
        
    ros::Subscriber sub = n.subscribe("/srf08_1", 10, cmd_vel_callback);    

    ros::Rate loop_rate(10);
    
    while(ros::ok())
    {
        ros::spinOnce();
  
        loop_rate.sleep();
    }   
    
    return 0;
}
