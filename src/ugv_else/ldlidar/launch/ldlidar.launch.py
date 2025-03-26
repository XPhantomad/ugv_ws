#!/usr/bin/env python3
from launch import LaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory
from launch.actions import IncludeLaunchDescription
from launch.substitutions import LaunchConfiguration
import os

def generate_launch_description():
    turtle_namespace = LaunchConfiguration('turtle_namespace', default='robot_namespace_NOT_SET')
    LDLIDAR_MODEL = os.environ['LDLIDAR_MODEL']
    ldlidar_launch_file = LDLIDAR_MODEL + '.launch.py'
    
    laser_bringup_launch = IncludeLaunchDescription(PythonLaunchDescriptionSource(
        [os.path.join(get_package_share_directory('ldlidar'), 'launch/'),
         ldlidar_launch_file]),
        launch_arguments={
            'robot_namespace': turtle_namespace,
        }.items(),
    )
    print("WEQWEQWEQEQWEQWE")

    ld = LaunchDescription()
 
    ld.add_action(laser_bringup_launch)

    return ld
