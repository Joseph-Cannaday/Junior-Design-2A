import subprocess
import os.path


class Speaker:
    def __init__(self, name = "snapdragon_speaker"):
        self.name = name
        return

    def testSpeaker(self, filename):
        # check if sound file exists
        error = 0
        path = '/home/pi/Documents/' + filename
        if (os.path.isfile(path)):
            error = 0
        else:
            error = 1
        print("Speaker File Error: " + str(error))
        return

    def sayLine(self, filename):
        sys_cmd = 'cvlc ' + filename
        subprocess.call(sys_cmd, shell = True)
        return

speaker = Speaker()
speaker.testSpeaker('StarWars60.wav')
speaker.sayLine('StarWars60.wav')



