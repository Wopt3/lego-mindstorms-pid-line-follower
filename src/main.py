motor_AB = MotorPair('A', 'B')
color = ColorSensor('F')
timer = Timer()
P_0 = 25
Kp = 0.02
Ki = 0.0003
Kd=0.00005
r = 350
integral = 0
derivative = 0 
lasterror = 0
num = 1
timer.reset()
  while timer.now() < 11:
      light = color.get_blue()
      e = (light - r)
      integral += e
      derivative = e - lasterror
      Skret = Kpe + Kiintegral+Kd*derivative
      powerA = P_0 + Skret
      powerC = P_0 - Skret
      lasterror=e
      motor_AB.start_tank_at_power(int(-powerA), int(-powerC))
       wait_for_seconds(0.05)
motor_AB.stop()
