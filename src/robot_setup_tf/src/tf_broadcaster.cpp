#include <ros/ros.h>
#include <tf/transform_broadcaster.h>

int main(int argc, char** argv){
  ros::init(argc, argv, "robot_tf_publisher");
  ros::NodeHandle n;

  ros::Rate r(20);

  tf::TransformBroadcaster broadcaster;

  while(n.ok()){
	broadcaster.sendTransform(
      tf::StampedTransform(
        tf::Transform(tf::Quaternion(0, 0, 0, 1), tf::Vector3(0.0, 0.0, 0.0)),
        ros::Time::now(),"map", "odom"));
    /*broadcaster.sendTransform(
      tf::StampedTransform(
        tf::Transform(tf::Quaternion(0, 0, 0, 1), tf::Vector3(0.17, 0.0, 0.2)),
        ros::Time::now(),"base_link", "laser"));*/
        
    /*broadcaster.sendTransform(
      tf::StampedTransform(
        tf::Transform(tf::Quaternion(0, 0, 180, 1), tf::Vector3(-0.30, 0.0, 0.0)),
        ros::Time::now(),"base_link", "sonar"));*/
    /*broadcaster.sendTransform(
      tf::StampedTransform(
        tf::Transform(tf::Quaternion(0, 0, 0, 1), tf::Vector3(-0.15, 0.0, 0.2)),
        ros::Time::now(),"base_link", "battery"));*/
    r.sleep();
  }
}
