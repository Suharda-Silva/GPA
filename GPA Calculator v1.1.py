import GPA


def run():
    print("\n\n", "Your GPA = ",GPA.GPACalc())
    end()
   
def end():
    print("\n\n (c) Suharda Silva - 2021")
    Exit = input("\n\n Press Enter to Exit:")
    try:
        HELP.close()
    except:
        pass
    exit()

#Additional for exe conversion
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.environ.get("_MEIPASS2",os.path.abspath("."))

    return os.path.join(base_path, relative_path)


print ("Welcome to GPA Calculator v1.1 \n\n")
print ("The new GPA Calculator support HELP and RUN commands!!!\n")
print ("To access the HELP command type HELP and press Enter")
print ("To run the GPA Calculator v1.1 type RUN or x to exit insted\n\n")


while True:
    Command = input("#[Initial]:")
    print ("\n")

    if Command.upper() == "HELP":
        HELP = open(resource_path("Help.rtxt")).read()
        for i in HELP:
            print (i, end="")
        print ("\n\n")
        #HELP.close()
    elif Command.upper() == "RUN":
        print ("\n\n")
        run()
    elif Command.upper() == "X":
        end()
    else:
        print("Invalid Command")
