import math

#Usage info at the bottom. Note that usage in this file is purely theoretical, so that you guys actually do some work.

gravity = 9.81 # gravity (Possible to use 9.80 m/s^2 as well)
x_dist = 2 #Distance from target

y_height = 0.5 #Height of flag
angle = (30/360) * 2*math.pi # launch angle

numerator = (-9.81) *x_dist*x_dist


denominator = (2*math.cos(angle)*math.cos(angle)*y_height)-(x_dist*math.sin(angle)*math.cos(angle)*2)


if numerator/denominator>0:
    velocity = math.sqrt(numerator/denominator)
    print(velocity)

else:
    print("Invalid parameters")



wheel_size = 4

ballvelocity = 75

print(wheel_size)

wheelrpm = 6000*ballvelocity/(wheel_size*math.pi*2.54)



print(wheelrpm)

"""Theory::What to do in PROS/VCS code when  at DRC::

Wheelvel/25<200, or don't run

Abstract:
if(wheelrpm<5000){
    flywheel.moveVelocity(wheelrpm/25);   //Accounting for the 25:1 gear ratio
    pros::delay(1000)/wait(1000)         //Add wait to ensure that your flywheel actually hits the rpm you need. May be replaced with a bs wait loop 
    elevate.moveRelative(10,200);       //that keeps going while the shaft rpm is not at the wheelrpm
    flywheel.moveVelocity(0)           //Stopping flywheel
"""