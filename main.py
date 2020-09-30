from microbit import * 
# Servo control: 
# 100 = 1 millisecond pulse all right 
# 200 = 2 millisecond pulse all left 
# 150 = 1.5 millisecond pulse center 
pin1.set_analog_period(20)

while True: 
	pin1.write_analog(150)
	sleep(1000)
	pin1.write_analog(100)
	sleep(1000)
	pin1.write_analog(200)
	sleep(1000)
