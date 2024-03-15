name = "Default"
volumeFFPlay = 20
city = "Batman"
country = "Turkey"
serverIP = "localhost"
serverPort = 8888
settingsFile = "Settings\settings.cfg"

def loadSettings():
    global settingsFile
    global name
    global volumeFFPlay
    global city
    global country
    global serverIP
    global serverPort

    settings = open(settingsFile, "r")
    for line in settings:
        if "Name:" in line:
            name = line.split(":")[1].strip()
        if "volumeFFPlay:" in line:
            volumeFFPlay = line.split(":")[1].strip()
        if 'City:' in line:
            city = line.split(':')[1].strip()
        if 'Country:' in line:
            country = line.split(':')[1].strip()
        if 'serverIP:' in line:
            serverIP = line.split(':')[1].strip()
        if 'serverPort:' in line:
            serverPort = int(line.split(':')[1].strip())

    settings.close()
    
    return True


def saveSettings():
    global settingsFile
    global name
    global volumeFFPlay
    global city
    global country
    global serverIP
    global serverPort

    with open(settingsFile, "r") as settings:
        lines = settings.readlines()

    with open( settingsFile, "w") as settings:
        for line in lines:
            if "Name:" in line:
                settings.write("Name: " + name)
            elif "volumeFFPlay:" in line:
                settings.write("volumeFFPlay: " + str(volumeFFPlay))
            elif "City:" in line:
                settings.write("City: " + city)
            elif "Country:" in line:
                settings.write("Country: " + country)
            elif "serverIP:" in line:
                settings.write("serverIP: " + serverIP)
            elif "serverPort:" in line:
                settings.write("serverPort: " + serverPort)
            else:
                settings.write(line)

    settings.close()