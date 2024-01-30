name = "Default"
FFPlayVolume = 20

def loadSettings():
    global name
    global FFPlayVolume
    settings = open("settings.cfg", "r")
    for line in settings:
        if "Name:" in line:
            name = line.split(":")[1].strip()
        if "FFPlayVolume:" in line:
            FFPlayVolume = line.split(":")[1].strip()

    settings.close()
    
    return True


def saveSettings():    
        global name
        global FFPlayVolume
        with open("settings.cfg", "r") as settings:
            lines = settings.readlines()

        with open("settings.cfg", "w") as settings:
            for line in lines:
                if "Name:" in line:
                    settings.write("Name: " + name)
                elif "FFPlayVolume:" in line:
                    settings.write("FFPlayVolume: " + str(FFPlayVolume))
                else:
                    settings.write(line)

        settings.close()