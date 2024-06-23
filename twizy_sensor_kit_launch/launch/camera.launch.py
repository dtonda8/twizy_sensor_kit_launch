import os
import stat
from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch.actions import OpaqueFunction
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
from ament_index_python.packages import get_package_share_directory

def launch_setup(context, *args, **kwargs):
    camera_feed_port = LaunchConfiguration("camera_feed_port").perform(context)
    # Find the package share directory
    package_share_directory = get_package_share_directory('twizy_sensor_kit_launch')
    
    # Define the path to the script within the package
    script_path = os.path.join(package_share_directory, 'scripts', 'gstream_to_ros.sh')

    # Ensure the script is executable
    if not os.access(script_path, os.X_OK):
        os.chmod(script_path, os.stat(script_path).st_mode | stat.S_IEXEC)
    
    return [ExecuteProcess(
            cmd=['bash', '-c', f'{script_path} {camera_feed_port}']
        )]

def generate_launch_description():
    launch_arguments = []
    # Define the argument for camera feed port
    launch_arguments.append(
            DeclareLaunchArgument("camera_feed_port", default_value='5000', description="Port to receive gstreamer feed")
        )
        
    return LaunchDescription(
        # Execute the shell script with the specified port
        launch_arguments + [OpaqueFunction(function=launch_setup)]
    )
