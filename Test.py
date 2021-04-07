from SongRename import *
from colorama import init,Fore,Style
init()

#Enter values to test=  ("Name","Expected name")
SONGS = [
    ("artist - name of song.mp3","name of song - artist.mp3"),
    ("artist - name of song - others.mp3","name of song - artist - others.mp3"),
    ("artist Ft. other - name of song.mp3","name of song - artist Ft. other.mp3"),
]

#Clear console
def cls(): print ("\n" * 50)
cls()

print("Starting SongRename Testing...")
testPassed = True
for songFile in SONGS:
    name= songFile[0]
    NameExpected= songFile[1]
    nameEdited= songRename(name)

    if NameExpected!=nameEdited:
        print(Fore.RED + "TEST NOT PASSED!:" + Style.RESET_ALL)
        print(Fore.GREEN + "     Name:    " + name + Style.RESET_ALL)
        print(Fore.RED + "     Renamed: " + nameEdited + Style.RESET_ALL)
        print()
        testPassed = False

if testPassed:
    print(Fore.GREEN+"GOOD: ALL TEST PASSED!" + Style.RESET_ALL)
