weight = 41.5
flat_rate = 20.00
premium_ground = 125.00

#Ground Shipping
if weight <= 2:
  print("Ground Shipping $" + str(weight * 1.50 + flat_rate))
elif weight <= 6:
  print("Ground Shipping $" + str(weight * 3.00 + flat_rate))
elif weight <= 10:
  print("Ground Shipping $" + str(weight * 4.00 + flat_rate))
else:
  print("Ground Shipping $" + str(weight * 4.75 + flat_rate))


#Premium Ground Shipping
print("Premium Ground Shipping $" + str(premium_ground))

#Drone Shipping
if weight <= 2:
  print("Drone Shipping $" + str(weight * 4.50))
elif weight <= 6:
  print("Drone Shipping $" + str(weight * 9.00))
elif weight <= 10:
  print("Drone Shipping $" + str(weight * 12.00))
else:
  print("Drone Shipping $" + str(weight * 14.25))