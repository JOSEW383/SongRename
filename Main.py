from SongRename import *
import pathlib
from colorama import init,Fore,Style
init()

if __name__ == '__main__':
    songs = [] #List of tuples than contains path and newNames of songs
    print(Fore.CYAN+"Files will be renamed: " + Style.RESET_ALL)

    for path in pathlib.Path(".").iterdir():
        if path.is_file():
            extension = path.suffix

            if extension==".mp3":
                name= path.name
                new_name = songRename(name=name)
                print(name+Fore.MAGENTA+" --> "+ Style.RESET_ALL+new_name)
                songs.append( (path.absolute() , new_name) )

    run= input("\nAre you sure to edit the name of all files?: ")
    run= run.upper()

    if run=="Y" or run=="YES" or run=="S":
        for songFile in songs:
            path= pathlib.Path(songFile[0])
            directory= path.parent
            newName= songFile[1]

            path.rename(pathlib.Path(directory, newName))

"""
*Future: Design graphic interface with
    https://docs.python.org/3/library/tkinter.html      TKinter
    https://github.com/ChrisKnott/Eel                   Eel
    
*Executable created with: 
    https://pypi.org/project/auto-py-to-exe/            auto-py-to-exe
"""