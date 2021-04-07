def songRename(name):
    newName=name

    extension= name.split(".")
    extension= extension[len(extension)-1]

    chain= name.split(" - ")
    if len(chain)==2:
        nameSong= chain[1].split(".")[0]
        newName= nameSong+" - "+chain[0]+"."+extension
    else:
        #Put the name of the song first
        newName= chain[1]+" - "+chain[0]

        #Put the rest of interpreters
        for x in range(2, len(chain)):
            newName+= " - "+chain[x]

    return newName