from .nvidia_racecar import NvidiaRacecar
import traitlets

car = NvidiaRacecar()

def check_config(vehicle):
    print("i2c_address: ", veh.i2c_address)
    print("steering_channel: ", veh.steering_channel)
    print("throttle_channel: ", veh.throttle_channel)
    
def performance_steering(vehicle):
    print("Check steering left-most to right-most")
    for i in [float(i)/20 for i in range(-20,21)]:
        vehicle.steering(i)
    
def performance_throttle(vehicle):
    print("Check throttle backrward to forward")
    for i in [float(i)/20 for i in range(-20,21)]:
        vehicle.throttle(i)

# def calibraion_steering_manual(vehicle):
# def calibration_steering_with_imu(vehicle):    
# def calibration_steering_with_camera(vehicle):
# def adjust_throttle_manual(vehicle):
# def adjust_throttle_with_imu(vehicle):

def print_steering(vehicle):
    print("Steering :" + vehicle.steering()*100 + "%")

def print_throttle(vehicle):
    print("Throttle :" + vehicle.throttle()*100 + "%")

def validate_car(vehicle):
    
    
if __name__ == "__main__":
    print("None Yet")
    
    