import RPi.GPIO as GPIO
import time

# Pin-nummers van de ultrasonensensor
TRIG = 23
ECHO = 24

# Pin-modus instellen
GPIO.setmode(GPIO.BCM)

# Pins voor de ultrasonensensor instellen
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

def meten_afstand():
    # Trigger de sensor
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    # Bewaar de start- en stoptijd
    start_tijd = time.time()
    stop_tijd = time.time()

    # Wacht tot de echo pin hoog wordt
    while GPIO.input(ECHO) == 0:
        start_tijd = time.time()

    # Wacht tot de echo pin weer laag wordt
    while GPIO.input(ECHO) == 1:
        stop_tijd = time.time()

    # Bereken de afstand
    afstand = (stop_tijd - start_tijd) * 17150

    return afstand

def koffiebonen_meten():
    afstand = meten_afstand()
    if afstand < 5:
        print("Er zijn nog maar weinig koffiebonen over.")
    elif afstand < 15:
        print("Er zijn nog genoeg koffiebonen over.")
    else:
        print("De koffiebonen zijn bijna op.")

def water_meten():
    afstand = meten_afstand()
    if afstand < 5:
        print("Er is nog maar weinig water over.")
    elif afstand < 10:
        print("Er is nog genoeg water over.")
    else:
        print("De waterreservoir is bijna vol.")

# Test de functies
koffiebonen_meten()
water_meten()

# Schoon de pinnen op
GPIO.cleanup()
