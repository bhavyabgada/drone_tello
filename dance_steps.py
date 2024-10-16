from drone_teaching_package.simulated_tello import EasyTelloToSimulatedDrone
from drone_teaching_package.real_tello import EasyTelloRealDrone
from time import sleep


class DroneDance:
    def __init__(self, drone):
        self.drone = drone

    def takeoff(self):
        self.drone.takeoff()
        print("Drone took off!")

    def land(self):
        self.drone.land()
        print("Drone landed!")

    def move_up(self, distance, speed=20):
        self.drone.go(0, 0, distance, speed)
        print(f"Drone moved up {distance} cm")

    def move_down(self, distance, speed=20):
        self.drone.go(0, 0, -distance, speed)
        print(f"Drone moved down {distance} cm")

    def move_forward(self, distance, speed=30):
        self.drone.go(0, distance, 0, speed)
        print(f"Drone moved forward {distance} cm")

    def move_backward(self, distance, speed=30):
        self.drone.go(0, -distance, 0, speed)
        print(f"Drone moved backward {distance} cm")

    def flip_left(self):
        self.drone.flip('l')
        print("Drone did a left flip")

    def flip_right(self):
        self.drone.flip('r')
        print("Drone did a right flip")

    def rotate_clockwise(self, degrees):
        self.drone.cw(degrees)
        print(f"Drone rotated clockwise {degrees} degrees")

    def rotate_counterclockwise(self, degrees):
        self.drone.ccw(degrees)
        print(f"Drone rotated counterclockwise {degrees} degrees")
