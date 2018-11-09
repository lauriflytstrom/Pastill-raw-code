import board
import busio
import adafruit_tsl2561
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_tsl2561.TSL2561(i2c)

print('Lux: {}'.format(sensor.lux))
print('Broadband: {0:0.2f}'.format(sensor.broadband))
print('Infrared: {0:0.2f}'.format(sensor.infrared))
#print('Luminosity: {}'.format(sensor.luminosity))
