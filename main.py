import json
import os

WATCHLIST = "watchlist.json"
MRANKING = "movie_rankings.json"
SRANKING = "show_rankings.json"

def loadWatchlist():
    if os.path.exists(WATCHLIST):
        with open(WATCHLIST, "r") as file:
            return json.load(file)
    return []

def saveWatchlist(watchlist):
    with open(WATCHLIST, "w") as file:
        json.dump(watchlist, file, indent = 4)

def loadMRankings():
    if os.path.exists(MRANKING):
        with open(MRANKING, "r") as file:
            return json.load(file)
    return []

def saveMRankings(ranking):
    with open(MRANKING, "w") as file:
        json.dump(ranking, file, indent = 4)

def loadSRankings():
    if os.path.exists(SRANKING):
        with open(SRANKING, "r") as file:
            return json.load(file)
    return []

def saveSRankings(ranking):
    with open(SRANKING, "w") as file:
        json.dump(ranking, file, indent = 4)
    
def addMovieShow():
    while True:
        which = input("Type [w] to add to the watchlist. Type [m] to add to the movie rankings. Type [t] to add to the TV show rankings. Type [b] to go back. ")
        if which == "b":
            print()
            break
        while True:
            if which == "w":
                added = input("Enter the movie/show you want to add to the watchlist: ")
                if added == "b":
                    print()
                    break
                valid = False
                while not valid:
                    addedType = input("Is this a movie or show? ")
                    if addedType == "movie" or addedType == "m" or addedType == "show" or addedType == "s":
                        valid = True
                    if addedType == 'b':
                        print()
                        return
                movies = loadWatchlist()
                if addedType == "m":
                    addedType = "movie"
                elif addedType == "s":
                    addedType = "show"
                newAdd = {"name": added, "type": addedType}
                if newAdd not in movies:
                    movies.append(newAdd)
                    saveWatchlist(movies)
                    print(added, "has been added to the watchlist.\n")
                else:
                    print(added, "already exists in the watchlist.\n")
            elif which == "m":
                added = input("Enter the movie you want to add to the rankings: ")
                if added == "b":
                    print()
                    break
                mRank = loadMRankings()
                if added not in mRank:
                    mRank.append(added)
                    saveMRankings(mRank)
                    print(added, "has been added to the movie rankings.\n")
                else:
                    print(added, "already exists in the movie rankings.\n")
            elif which == "t":
                if added == "b":
                    print()
                    break
                added = input("Enter the show you want to add to the rankings: ")
                sRank = loadSRankings()
                if added not in sRank:
                    sRank.append(added)
                    saveMRankings(sRank)
                    print(added, "has been added to the show rankings.\n")
                else:
                    print(added, "already exists in the show rankings.\n")
            elif which == "b":
                print()
                break
            else:
                print("\nInvalid input.")
                which = input("Type [w] to add to the watchlist. Type [m] to add to the movie rankings. Type [t] to add to the TV show rankings. Type [b] to go back. ")

def viewMovieShow():
    which = input("Type [w] to view the watchlist. Type [m] to view the movie rankings. Type [t] to view the TV show rankings. Type [b] to go back. ")
    while True:
        if which == "w":
            list = loadWatchlist()
            if list:
                print("\nYour Watchlist:\n")
                for i, entry in enumerate(list, start = 1):
                    print(f"{i}. {entry['name']} ({entry['type']})")
                print()
            else:
                print("\nYour watchlist is empty.\n")
            which = input("Type [w] to view the watchlist. Type [m] to view the movie rankings. Type [t] to view the TV show rankings. Type [b] to go back. ")
        elif which == "m":
            movies = loadMRankings()
            if movies:
                print("\nYour Movie Rankings:\n")
                for i, entry in enumerate(movies, start = 1):
                    print(f"{i}. {entry}")
                print()
            else:
                print("\nYour movie rankings are empty.\n")
            which = input("Type [w] to view the watchlist. Type [m] to view the movie rankings. Type [t] to view the TV show rankings. Type [b] to go back. ")
        elif which == "t":
            shows = loadSRankings()
            if shows:
                print("\nYour TV Show Rankings:\n")
                for i, entry in enumerate(shows, start = 1):
                    print(f"{i}. {entry['name']} ({entry['type']})")
                print()
            else:
                print("\nYour TV show rankings are empty.\n")
            which = input("Type [w] to view the watchlist. Type [m] to view the movie rankings. Type [t] to view the TV show rankings. Type [b] to go back. ")
        elif which == "b":
            print()
            break
        else:
            print("\nInvalid input.")
            which = input("Type [w] to view the watchlist. Type [m] to view the movie rankings. Type [t] to view the TV show rankings. Type [b] to go back. ")

def removeMovieShow():
    while True:
        which = input("Type [w] to remove from the watchlist. Type [m] to remove from the movie rankings. Type [t] to remove from the TV show rankings. Type [b] to go back. ")
        if which == "b":
            print()
            break
        while True:
            if which == "w":
                listRemove = input("Enter the movie/show you want to remove from the watchlist: ")
                if listRemove == "b":
                    print()
                    break
                list = loadWatchlist()
                if list:
                    for entry in list:
                        if entry['name'] == listRemove:
                            list.remove(entry)
                            saveWatchlist(list)
                            print(listRemove, "has been removed from the watchlist.\n")
                            return
                    print(listRemove, "is not in the watchlist.\n")
                else:
                    print("Your watchlist is empty.\n")
            elif which == "m":
                movieRemove = input("Enter the movie you want to remove from the movie rankings: ")
                if movieRemove == "b":
                    print()
                    break
                movies = loadMRankings()
                if movies:
                    for entry in movies:
                        if entry['name'] == movieRemove:
                            movies.remove(entry)
                            saveMRankings(movies)
                            print(movieRemove, "has been removed from the movie rankings.\n")
                            return
                    print(movieRemove, "is not in the movie rankings.\n")
                else:
                    print("Your movie rankings are empty.\n")
            elif which == "t":
                showRemove = input("Enter the show you want to remove from the show rankings: ")
                if showRemove == "b":
                    print()
                    break
                shows = loadSRankings()
                if shows:
                    for entry in shows:
                        if entry['name'] == showRemove:
                            shows.remove(entry)
                            saveSRankings(shows)
                            print(showRemove, "has been removed from the TV show rankings.\n")
                            return
                    print(showRemove, "is not in the TV show rankings.\n")
                else:
                    print("Your TV show rankings is empty.\n")
            elif which == "b":
                print()
                break
            else:
                print("\nInvalid input.")
                which = input("Type [w] to remove from the watchlist. Type [m] to remove from the movie rankings. Type [t] to remove from the TV show rankings. Type [b] to go back. ")
    
    
def renameMovieShow():
    while True:
        which = input("Type [w] to rename a movie/show in the watchlist. Type [m] to rename a movie in the movie rankings. Type [t] to rename a show in the TV show rankings. Type [b] to go back. ")
        if which == "b":
            print()
            break
        while True:
            if which == "w":
                oldName = input("Enter the movie/show you want to rename: ")
                if oldName == "b":
                    print()
                    break
                list = loadWatchlist()
                if list:
                    for i, entry in enumerate(list):
                        if entry['name'] == oldName:
                            typeO = entry['type']
                            oldNameX = oldName
                            newName = input("Enter the new name of the movie/show: ")
                            list[i] = {"name": newName, "type": typeO}
                            saveWatchlist(list)
                            print(oldNameX, " has been updated in the watchlist to ", newName, ".\n", sep = "")
                            return
                    print(oldName, "does not exist in the watchlist.\n")
                else:
                    print("Your watchlist is empty.\n")
            elif which == "m":
                oldName = input("Enter the movie you want to rename: ")
                if oldName == "b":
                    print()
                    break
                movies = loadMRankings()
                if movies:
                    for entry in movies:
                        if entry['name'] == input:
                            oldName = input
                            newName = input("Enter the new name of the movie/show: ")
                            i = movies.index(input)
                            movies[i] = newName
                            saveMRankings(movies)
                            print(oldName, " has been updated in the movie rankings to \n", newName, ".", sep = "")
                            return
                    print(input, "does not exist in the movie rankings.\n")
                else:
                    print("Your movie rankings are empty.\n")
            elif which == "w":
                oldName = input("Enter the show you want to rename: ")
                if oldName == "b":
                    print()
                    break
                shows = loadSRankings()
                if shows:
                    for entry in shows:
                        if entry['name'] == input:
                            oldName = input
                            newName = input("Enter the new name of the show: ")
                            i = shows.index(input)
                            shows[i] = newName
                            saveSRankings(shows)
                            print(oldName, " has been updated in the TV show rankings to \n", newName, ".", sep = "")
                            return
                    print(input, "does not exist in the TV show rankings.\n")
                else:
                    print("Your TV show rankings is empty.\n")
            elif which == "b":
                print()
                break
            else:
                print("\nInvalid input.")
                which = input("Type [w] to rename a movie/show in the watchlist. Type [m] to rename a movie in the movie rankings. Type [t] to rename a show in the TV show rankings. Type [b] to go back. ")

def updateOrder(input):
    which = input("Type [w] to update a movie/show's position in the watchlist. Type [m] to update a movie's position in the movie rankings. Type [t] to update a show's position in the TV show rankings. Type [b] to go back. ")
    while True:
        if which == "w":
            list = loadWatchlist()
            for entry in list:
                if input in list:
                    list.remove(input)
                    newPos = int(input("Enter which position you want to put the movie/show at: "))
                    list.insert(newPos - 1, input)
                    saveWatchlist(list)
                    print(input, "'s position has been updated.\n", sep = "")
                    which = input("Type [w] to update a movie/show's position in the watchlist. Type [m] to update a movie's position in the movie rankings. Type [t] to update a show's position in the TV show rankings. Type [b] to go back. ")
                    return
            list.append(input)
            saveWatchlist(list)
            print(input, "was not in the watchlist, so it has been added to the watchlist.\n")
            which = input("Type [w] to update a movie/show's position in the watchlist. Type [m] to update a movie's position in the movie rankings. Type [t] to update a show's position in the TV show rankings. Type [b] to go back. ")
        elif which == "m":
            movies = loadMRankings()
            for entry in movies:
                if input in movies:
                    movies.remove(input)
                    newPos = int(input("Enter which position you want to put the movie at: "))
                    movies.insert(newPos - 1, input)
                    saveMRankings(movies)
                    print(input, "'s position has been updated.\n", sep = "")
                    which = input("Type [w] to update a movie/show's position in the watchlist. Type [m] to update a movie's position in the movie rankings. Type [t] to update a show's position in the TV show rankings. Type [b] to go back. ")
                    return
            movies.append(input)
            saveMRankings(movies)
            print(input, "was not in the movie rankings, so it has been added to the movie rankings.\n")
            which = input("Type [w] to update a movie/show's position in the watchlist. Type [m] to update a movie's position in the movie rankings. Type [t] to update a show's position in the TV show rankings. Type [b] to go back. ")
        elif which == "t":
            shows = loadSRankings()
            for entry in shows:
                if input in shows:
                    shows.remove(input)
                    newPos = int(input("Enter which position you want to put the show at: "))
                    shows.insert(newPos - 1, input)
                    saveSRankings(shows)
                    print(input, "'s position has been updated.\n", sep = "")
                    which = input("Type [w] to update a movie/show's position in the watchlist. Type [m] to update a movie's position in the movie rankings. Type [t] to update a show's position in the TV show rankings. Type [b] to go back. ")
                    return
            shows.append(input)
            saveSRankings(shows)
            print(input, "was not in the TV show rankings, so it has been added to the TV show rankings.\n")
            which = input("Type [w] to update a movie/show's position in the watchlist. Type [m] to update a movie's position in the movie rankings. Type [t] to update a show's position in the TV show rankings. Type [b] to go back. ")
        elif which == "b":
            print()
            break
        else:
            print("\nInvalid input.")
            which = input("Type [w] to update a movie/show's position in the watchlist. Type [m] to update a movie's position in the movie rankings. Type [t] to update a show's position in the TV show rankings. Type [b] to go back. ")

def clear():
    which = input("Type [w] to clear the watchlist. Type [m] to clear the movie rankings. Type [t] to clear the TV show rankings. Type [r] to clear both rankings. Type [b] to go back. ")
    while True:
        if which == "w":
            list = loadWatchlist()
            list.clear()
            saveWatchlist(list)
            print("Your watchlist has been cleared.\n")
        elif which == "m":
            movies = loadMRankings()
            movies.clear()
            saveMRankings(movies)
            print("Your movie rankings have been cleared.")
        elif which == "s":
            shows = loadSRankings()
            shows.clear()
            saveSRankings(shows)
            print("Your TV show rankings have been cleared.")
        elif which == "r":
            movies = loadMRankings()
            shows = loadSRankings()
            movies.clear()
            shows.clear()
            saveMRankings(movies)
            saveSRankings(shows)
            print("Your movie rankings have been cleared.")
            print("Your TV show rankings have been cleared.")
        elif which == "b":
            print()
            break
        else:
            print("\nInvalid input.")
            which = input("Type [w] to clear the watchlist. Type [m] to clear the movie rankings. Type [t] to clear the TV show rankings. Type [r] to clear both rankings. Type [b] to go back. ")

def main():
    while True:
        print("Input [v] to view the watchlist/rankings")
        print("Input [a] to add a movie to the watchlist/rankings")
        print("Input [d] to delete a movie from the watchlist/rankings")
        print("Input [r] to rename a movie on the watchlist/rankings")
        print("Input [u] to update a movie's position on the watchlist/rankings")
        print("Input [c] to clear the watchlist/rankings")
        print("Input [e] to exit")
        choice = input("Enter choice: ")
        if choice == "v":
            viewMovieShow()
        elif choice == "a":
            addMovieShow()
        elif choice == "d":
            removeMovieShow()
        elif choice == "r":
            renameMovieShow()
        elif choice == "u":
            posUpdate = input("Enter the movie/show whose position you want to update: ")
            updateOrder(posUpdate)
        elif choice == "e":
            print()
            break
        elif choice == "c":
            clear()

main()