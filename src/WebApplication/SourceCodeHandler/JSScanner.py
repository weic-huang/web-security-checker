import re

class JSScanner():
    def __init__(self):
        pass

    def checkAutoDownload(self):
        # check if functions try to generate downloads without user interaction

        for f in functions:
            for s in re.findall(r'removeChild\((.*?)\)', f):
                click = s + '.click()'
                if click in f:
                    return True
        return False

    def checkPopUp(self):
        # check if the provided functions try to create popup windows without user-triggered events

        for f in functions:
            if ('window.open' in f) and not ('onclick' in f):
                return True
        return False

    def checkNotification(self, functions):
        # check if the provided functions contain a request for notification permission

        for f in functions:
            if 'Notification.requestPermission' in f:
                return True
        return False

    def checkHardwareAccess(self):
        # check if the provided functions try to access camera, microphone or other hardwares
        hardware_dict = {}

        for f in functions:
            # camera and mic
            for s in re.findall(r'(webkitG|mozG|g)etUserMedia\((.*?)\)', f):
                if 'video' in s[1]:
                    hardware_dict['camera'] = True
                if 'audio' in s[1]:
                    hardware_dict['microphone'] = True

            # ambient light sensor
            if ('AmbientLightSensor' in f) or ("addEventListener('devicelight'" in f):
                hardware_dict['Ambient Light Sensor'] = True

            # device motion sensor
            if ("addEventListener('devicemotion'" in f) or ("Accelerometer()" in f) or \
               ("Gyroscope()" in f) or ("Magnetometer()" in f) or \
               ("LinearAccelerationSensor()" in f) or ("GravitySensor()" in f):
                hardware_dict['Device Motion'] = True

            # device orientation sensor
            if ("addEventListener('deviceorientation'" in f) or \
               ("AbsoluteOrientationSensor()" in f) or \
               ("RelativeOrientationSensor()" in f):
                hardware_dict['Device Orientation'] = True

        return hardware_dict