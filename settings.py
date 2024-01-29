
def loadSettings():

    global Name

    settings = open("settings.cfg", "r")
    for line in settings:
        if "Name:" in line:
            Name = line.split(":")[1].strip()

    settings.close()
    return True


def saveSettings():    
        settings = open("settings.cfg", "w")

        for line in settings:
            if "Name:" in line:
                settings.write("Name: " + Name)
            else:
                settings.write(line)

        settings.close()