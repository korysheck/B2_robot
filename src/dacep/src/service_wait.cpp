#include "ros/ros.h"
#include "std_msgs/Bool.h"

bool sleep_function(std_msgs::Bool data)
{
  ROS_INFO("getting sleep");
  ros::Duration(1.0).sleep();
  ROS_INFO("sleeping done");
  return true;
}

int main(int argc, char **argv)
{
  ros::init(argc, argv, "sleep_server");
  ros::NodeHandle n;

  //ros::ServiceServer service = n.advertiseService("sleep_service", sleep_function);
  //ROS_INFO("Ready to sleep.");
 
  ros::spin();

  return 0;
}
