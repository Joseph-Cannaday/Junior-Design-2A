import RPi.GPIO as GPIO
import pigpio

LED_PIN = 17
class Light:
    def __init__(self, name = "snapdragon_LED"):
        self.name = name
        return

    def testLed(self, ledPin):
        error = 0
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(ledPin, GPIO.OUT)
        GPIO.output(ledPin, GPIO.LOW)
        GPIO.setup(ledPin, GPIO.IN)
        if (GPIO.input(ledPin) == 0):
            error = 0
        else:
            error = 1

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(ledPin, GPIO.OUT)
        GPIO.output(ledPin, GPIO.HIGH)
        GPIO.setup(ledPin, GPIO.IN)
        if (GPIO.input(ledPin) == 1):
            error = 0
        else:
            error = 1
        print("LED Error: " + str(error))
        return

    def doLed(self, ledPin):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(ledPin, GPIO.OUT)
        # set ledPin to low to activate
        GPIO.output(ledPin, GPIO.LOW)
        return

if __name__ == '__main__':
    led = Light()
    led.testLed(LED_PIN)
