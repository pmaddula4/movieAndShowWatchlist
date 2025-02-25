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
    which = input("Type [w], [m], or [t] to add to the watchlist, movie rankings, or show rankings: ")
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
    elif which == "m":
        added = input("Enter the movie you want to add to the rankings: ")
        mRank = loadMRankings()
        if added not in mRank:
            mRank.append(added)
            saveMRankings(mRank)
            print(added, "has been added to the movie rankings.\n")
        else:
            print(added, "already exists in the movie rankings.\n")
    elif which == "t":
        added = input("Enter the show you want to add to the rankings: ")
        sRank = loadSRankings()
        if added not in sRank:
            sRank.append(added)
            saveMRankings(sRank)
            print(added, "has been added to the show rankings.\n")
        else:
            print(added, "already exists in the show rankings.\n")

def viewMovieShow():
    which = input("Type [w], [m], or [t] to view the watchlist, movie rankings, or show rankings: ")
    if which == "w":
        list = loadWatchlist()
        if list:
            print("\nYour Watchlist:\n")
            for i, entry in enumerate(list, start = 1):
                print(f"{i}. {entry['name']} ({entry['type']})")
            print()
        else:
            print("\nYour watchlist is empty.\n")
    elif which == "m":
        movies = loadMRankings()
        if movies:
            print("\nYour Movie Rankings:\n")
            for i, entry in enumerate(movies, start = 1):
                print(f"{i}. {entry['name']} ({entry['type']})")
            print()
        else:
            print("\nYour movie rankings are empty.\n")
    elif which == "t":
        shows = loadSRankings()
        if shows:
            print("\nYour TV Show Rankings:\n")
            for i, entry in enumerate(shows, start = 1):
                print(f"{i}. {entry['name']} ({entry['type']})")
            print()
        else:
            print("\nYour TV show rankings are empty.\n")

def removeMovieShow(input):
    which = input("Type [w], [m], or [t] to remove to the watchlist, movie rankings, or show rankings: ")
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
    if which == "m":
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
    if which == "t":
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
    
    
def renameMovie(movie):
    movies = loadWatchlist()
    if movies:
        for entry in movies:
            if entry['name'] == movie:
                oldName = movie
                newName = input("Enter the new name of the movie: ")
                i = movies.index(movie)
                movies[i] = newName
                saveWatchlist(movies)
                print(oldName, " has been updated in the watchlist to \n", newName, ".", sep = "")
                return
        print(movie, "does not exist in the watchlist.\n")
    else:
        print("Your watchlist is empty.\n")


def updateOrder(movie):
    movies = loadWatchlist()
    for entry in movies:
        if movie in movies:
            movies.remove(movie)
            newPos = int(input("Enter which position you want to put the movie at: "))
            movies.insert(newPos - 1, movie)
            saveWatchlist(movies)
            print(movie, "'s position has been updated.\n", sep = "")
            return
    movies.append(movie)
    saveWatchlist(movies)
    print(movie, "has been added to the watchlist.\n")

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
            removed = input("Enter the movie you want to remove from the watchlist: ")
            removeMovieShow(removed)
        elif choice == "r":
            oldName = input("Enter the movie you want to rename: ")
            renameMovie(oldName)
        elif choice == "u":
            posUpdate = input("Enter the movie who's position you want to update: ")
            updateOrder(posUpdate)
        elif choice == "e":
            print()
            break
        elif choice == "c":
            clear()

main()