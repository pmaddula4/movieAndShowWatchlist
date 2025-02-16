import json
import os

WATCHLIST = "watchlist.json"

def loadWatchlist():
    if os.path.exists(WATCHLIST):
        with open(WATCHLIST, "r") as file:
            return json.load(file)
    return []

def saveWatchlist(watchlist):
    with open(WATCHLIST, "w") as file:
        json.dump(watchlist, file, indent = 4)
    
def addMovie():
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

def viewMovies():
    movies = loadWatchlist()
    if movies:
        print("\nYour Watchlist:\n")
        for i, entry in enumerate(movies, start = 1):
            print(f"{i}. {entry['name']} ({entry['type']})")
        print()
    else:
        print("\nYour movie watchlist is empty.\n")

def removeMovie(movie):
    movies = loadWatchlist()
    if movies:
        for entry in movies:
            if entry['name'] == movie:
                movies.remove(entry)
                saveWatchlist(movies)
                print(movie, "has been removed from the watchlist.\n")
                return
        print(movie, "is not in the watchlist.\n")
    else:
        print("Your watchlist is empty.\n")
    
    
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
        print("Input [w] to view the watchlist")
        print("Input [m] to view movie ranking")
        print("Input [t] to view TV show ranking")
        print("Input [a] to add a movie to the watchlist")
        print("Input [d] to delete a movie from the watchlist")
        print("Input [r] to rename a movie on the watchlist")
        print("Input [u] to update a movie's position on the watchlist")
        print("Input [c] to clear the watchlist")
        print("Input [e] to exit")
        choice = input("Enter choice: ")
        if choice == "w":
            viewMovies()
        elif choice == "a":
            addMovie()
        elif choice == "d":
            removed = input("Enter the movie you want to remove from the watchlist: ")
            removeMovie(removed)
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