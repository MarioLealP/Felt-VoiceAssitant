name = "Default"
FFPlayVolume = 20
city = "Batman"
country = "Turkey"

def loadSettings():
    global name
    global FFPlayVolume
    global city
    global country
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
                elif "City:" in line:
                    settings.write("City: " + city)
                elif "Country:" in line:
                    settings.write("Country: " + country)
                else:
                    settings.write(line)

        settings.close()