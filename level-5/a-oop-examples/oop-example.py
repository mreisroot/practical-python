from robot import Robot
from robot import RoboticArm
from robot import PackagingSolution

my_robot = Robot("R2D2", 2)
robotic_arm_right = RoboticArm("Bob", 4, 300)
robotic_arm_left = RoboticArm("John", 2, 300)
packaging_solution = PackagingSolution(robotic_arm_right, robotic_arm_left)

# my_robot.print_info()
packaging_solution.package(1, 2, 3, 4, 5, 6)
