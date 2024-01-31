name = "Default"
FFPlayVolume = 20
city = "Batman"
country = "Turkey"
ServerIP = "localhost"
ServerPort = 8888

def loadSettings():
    global name
    global FFPlayVolume
    global city
    global country
    global ServerIP
    global ServerPort

    settings = open("settings.cfg", "r")
    for line in settings:
        if "Name:" in line:
            name = line.split(":")[1].strip()
        if "FFPlayVolume:" in line:
            FFPlayVolume = line.split(":")[1].strip()
        if 'City:' in line:
            city = line.split(':')[1].strip()
        if 'Country:' in line:
            country = line.split(':')[1].strip()
        if 'ServerIP:' in line:
            ServerIP = line.split(':')[1].strip()
        if 'ServerPort:' in line:
            ServerPort = int(line.split(':')[1].strip())

    settings.close()
    
    return True


def saveSettings():    
        global name
        global FFPlayVolume
        global city
        global country
        global ServerIP
        global ServerPort

        with open("settings.cfg", "r") as settings:
            lines = settings.readlines()

        with open("settings.cfg", "w") as settings:
            for line in lines:
                if "Name:" in line:
                    settings.write("Name: " + name)
                elif "FFPlayVolume:" in line:
                    settings.write("FFPlayVolume: " + str(FFPlayVolume))
                elif "City:" in line:
                    settings.write("City: " + city)
                elif "Country:" in line:
                    settings.write("Country: " + country)
                elif "ServerIP:" in line:
                    settings.write("ServerIP: " + ServerIP)
                elif "ServerPort:" in line:
                    settings.write("ServerPort: " + ServerPort)
                else:
                    settings.write(line)

        settings.close()