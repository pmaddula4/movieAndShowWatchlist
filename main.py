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
    which = input("Type [w] to add to the watchlist. Type [m] to add to the movie rankings. Type [t] to add to the TV show rankings. Type [b] to go back. ")
    while True:
        if which == "w":
            added = input("Enter the movie/show you want to add to the watchlist: ")
            valid = False
            while not valid:
                addedType = input("Is this a movie or show? ")
                if addedType == "movie" or addedType == "show":
                    valid = True
                if addedType == 'n':
                    print()
                    return
            movies = loadWatchlist()
            newAdd = {"name": added, "type": addedType}
            if newAdd not in movies:
                movies.append(newAdd)
                saveWatchlist(movies)
                print(added, "has been added to the watchlist.\n")
            else:
                print(added, "already exists in the watchlist.\n")
            which = input("Type [w] to add to the watchlist. Type [m] to add to the movie rankings. Type [t] to add to the TV show rankings. Type [b] to go back. ")
        elif which == "m":
            added = input("Enter the movie you want to add to the rankings: ")
            mRank = loadMRankings()
            if added not in mRank:
                mRank.append(added)
                saveMRankings(mRank)
                print(added, "has been added to the movie rankings.\n")
            else:
                print(added, "already exists in the movie rankings.\n")
            which = input("Type [w] to add to the watchlist. Type [m] to add to the movie rankings. Type [t] to add to the TV show rankings. Type [b] to go back. ")
        elif which == "t":
            added = input("Enter the show you want to add to the rankings: ")
            sRank = loadSRankings()
            if added not in sRank:
                sRank.append(added)
                saveMRankings(sRank)
                print(added, "has been added to the show rankings.\n")
            else:
                print(added, "already exists in the show rankings.\n")
                which = input("Type [w] to add to the watchlist. Type [m] to add to the movie rankings. Type [t] to add to the TV show rankings. Type [b] to go back. ")
        elif which == "b":
            break
        else:
            print("\nInvalid input.")
            which = input("Type [w] to add to the watchlist. Type [m] to add to the movie rankings. Type [t] to add to the TV show rankings. Type [b] to go back. ")

def viewMovieShow():
    which = input("Type [w] to add to the watchlist. Type [m] to add to the movie rankings. Type [t] to add to the TV show rankings. Type [b] to go back. ")
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
            which = input("Type [w] to add to the watchlist. Type [m] to add to the movie rankings. Type [t] to add to the TV show rankings. Type [b] to go back. ")

        elif which == "m":
            movies = loadMRankings()
            if movies:
                print("\nYour Movie Rankings:\n")
                for i, entry in enumerate(movies, start = 1):
                    print(f"{i}. {entry['name']} ({entry['type']})")
                print()
            else:
                print("\nYour movie rankings are empty.\n")
            which = input("Type [w] to add to the watchlist. Type [m] to add to the movie rankings. Type [t] to add to the TV show rankings. Type [b] to go back. ")
        elif which == "t":
            shows = loadSRankings()
            if shows:
                print("\nYour TV Show Rankings:\n")
                for i, entry in enumerate(shows, start = 1):
                    print(f"{i}. {entry['name']} ({entry['type']})")
                print()
            else:
                print("\nYour TV show rankings are empty.\n")
            which = input("Type [w] to add to the watchlist. Type [m] to add to the movie rankings. Type [t] to add to the TV show rankings. Type [b] to go back. ")
        elif which == "b":
            break
        else:
            print("\nInvalid input.")
            which = input("Type [w] to add to the watchlist. Type [m] to add to the movie rankings. Type [t] to add to the TV show rankings. Type [b] to go back. ")

def removeMovieShow(input):
    which = input("Type [w] to add to the watchlist. Type [m] to add to the movie rankings. Type [t] to add to the TV show rankings. Type [b] to go back. ")
    while True:
        if which == "w":
            list = loadWatchlist()
            if list:
                for entry in list:
                    if entry['name'] == input:
                        list.remove(entry)
                        saveWatchlist(list)
                        print(input, "has been removed from the watchlist.\n")
                        return
                print(input, "is not in the watchlist.\n")
            else:
                print("Your watchlist is empty.\n")
            which = input("Type [w] to add to the watchlist. Type [m] to add to the movie rankings. Type [t] to add to the TV show rankings. Type [b] to go back. ")
        elif which == "m":
            movies = loadMRankings()
            if movies:
                for entry in movies:
                    if entry['name'] == input:
                        movies.remove(entry)
                        saveMRankings(movies)
                        print(input, "has been removed from the movie rankings.\n")
                        return
                print(input, "is not in the movie rankings.\n")
            else:
                print("Your movie rankings are empty.\n")
            which = input("Type [w] to add to the watchlist. Type [m] to add to the movie rankings. Type [t] to add to the TV show rankings. Type [b] to go back. ")
        elif which == "t":
            shows = loadSRankings()
            if shows:
                for entry in shows:
                    if entry['name'] == input:
                        shows.remove(entry)
                        saveSRankings(shows)
                        print(input, "has been removed from the TV show rankings.\n")
                        return
                print(input, "is not in the TV show rankings.\n")
            else:
                print("Your TV show rankings is empty.\n")
            which = input("Type [w] to add to the watchlist. Type [m] to add to the movie rankings. Type [t] to add to the TV show rankings. Type [b] to go back. ")
        elif which == "b":
            break
        else:
            print("\nInvalid input.")
            which = input("Type [w] to add to the watchlist. Type [m] to add to the movie rankings. Type [t] to add to the TV show rankings. Type [b] to go back. ")
    
    
def renameMovieShow(input):
    which = input("Type [w] to add to the watchlist. Type [m] to add to the movie rankings. Type [t] to add to the TV show rankings. Type [b] to go back. ")
    while True:
        if which == "w":
            list = loadWatchlist()
            if list:
                for entry in list:
                    if entry['name'] == input:
                        oldName = input
                        newName = input("Enter the new name of the movie/show: ")
                        i = list.index(input)
                        list[i] = newName
                        saveWatchlist(list)
                        print(oldName, " has been updated in the watchlist to \n", newName, ".", sep = "")
                        return
                print(input, "does not exist in the watchlist.\n")
            else:
                print("Your watchlist is empty.\n")
            which = input("Type [w] to add to the watchlist. Type [m] to add to the movie rankings. Type [t] to add to the TV show rankings. Type [b] to go back. ")
        elif which == "m":
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
            which = input("Type [w] to add to the watchlist. Type [m] to add to the movie rankings. Type [t] to add to the TV show rankings. Type [b] to go back. ")
        elif which == "w":
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
            which = input("Type [w] to add to the watchlist. Type [m] to add to the movie rankings. Type [t] to add to the TV show rankings. Type [b] to go back. ")
        elif which == "b":
            break
        else:
            print("\nInvalid input.")
            which = input("Type [w] to add to the watchlist. Type [m] to add to the movie rankings. Type [t] to add to the TV show rankings. Type [b] to go back. ")

def updateOrder(input):
    which = input("Type [w] to add to the watchlist. Type [m] to add to the movie rankings. Type [t] to add to the TV show rankings. Type [b] to go back. ")
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
                    which = input("Type [w] to add to the watchlist. Type [m] to add to the movie rankings. Type [t] to add to the TV show rankings. Type [b] to go back. ")
                    return
            list.append(input)
            saveWatchlist(list)
            print(input, "was not in the watchlist, so it has been added to the watchlist.\n")
            which = input("Type [w] to add to the watchlist. Type [m] to add to the movie rankings. Type [t] to add to the TV show rankings. Type [b] to go back. ")
        elif which == "m":
            movies = loadMRankings()
            for entry in movies:
                if input in movies:
                    movies.remove(input)
                    newPos = int(input("Enter which position you want to put the movie at: "))
                    movies.insert(newPos - 1, input)
                    saveMRankings(movies)
                    print(input, "'s position has been updated.\n", sep = "")
                    which = input("Type [w] to add to the watchlist. Type [m] to add to the movie rankings. Type [t] to add to the TV show rankings. Type [b] to go back. ")
                    return
            movies.append(input)
            saveMRankings(movies)
            print(input, "was not in the movie rankings, so it has been added to the movie rankings.\n")
            which = input("Type [w] to add to the watchlist. Type [m] to add to the movie rankings. Type [t] to add to the TV show rankings. Type [b] to go back. ")
        elif which == "t":
            shows = loadSRankings()
            for entry in shows:
                if input in shows:
                    shows.remove(input)
                    newPos = int(input("Enter which position you want to put the show at: "))
                    shows.insert(newPos - 1, input)
                    saveSRankings(shows)
                    print(input, "'s position has been updated.\n", sep = "")
                    which = input("Type [w] to add to the watchlist. Type [m] to add to the movie rankings. Type [t] to add to the TV show rankings. Type [b] to go back. ")
                    return
            shows.append(input)
            saveSRankings(shows)
            print(input, "was not in the TV show rankings, so it has been added to the TV show rankings.\n")
            which = input("Type [w] to add to the watchlist. Type [m] to add to the movie rankings. Type [t] to add to the TV show rankings. Type [b] to go back. ")
        elif which == "b":
            break
        else:
            print("\nInvalid input.")
            which = input("Type [w] to add to the watchlist. Type [m] to add to the movie rankings. Type [t] to add to the TV show rankings. Type [b] to go back. ")

def clear():
    movies = loadWatchlist()
    movies.clear()
    saveWatchlist(movies)
    print("Your watchlist has been cleared.\n")

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
            removed = input("Enter the movie/show you want to remove from the watchlist: ")
            removeMovieShow(removed)
        elif choice == "r":
            oldName = input("Enter the movie/show you want to rename: ")
            renameMovieShow(oldName)
        elif choice == "u":
            posUpdate = input("Enter the movie/show who's position you want to update: ")
            updateOrder(posUpdate)
        elif choice == "e":
            print()
            break
        elif choice == "c":
            clear()

main()