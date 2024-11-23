import sys
if sys.prefix == '/Users/felipemesa/miniconda3/envs/ros2':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/Users/felipemesa/miniconda3/envs/ros2/src/tarea_ros/install/tarea_ros'
