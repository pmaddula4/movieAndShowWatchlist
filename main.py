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
    
def addMovie(movie):
    movies = loadWatchlist()
    if movie not in movies:
        movies.append(movie)
        saveWatchlist(movies)
        print(movie, "has been added to the watchlist.")
        print()
    else:
        print(movie, "already exists in the watchlist.")
        print()

def viewMovies():
    movies = loadWatchlist()
    if movies:
        print()
        print("Your Movie Watchlist:")
        print()
        for idx, movie in enumerate(movies, start=1):
            print(f"{idx}. {movie}")
        print()
    else:
        print("Your movie watchlist is empty.")
        print()

def removeMovie(movie):
    movies = loadWatchlist()
    if movie in movies:
        movies.remove(movie)
        saveWatchlist(movies)
        print(movie, "has been removed from the watchlist.")
        print()
    else:
        print(movie, "is not in the watchlist.")
        print()
    
def renameMovie(movie):
    movies = loadWatchlist()
    if movie in movies:
        oldName = movie
        newName = input("Enter the new name of the movie: ")
        i = movies.index(movie)
        movies[i] = newName
        saveWatchlist(movies)
        print(oldName, " has been updated in the watchlist to ", newName, ".", sep = "")
        print()
    else:
        print(movie, "does not exist in the watchlist.")
        print()

def updateOrder(movie):
    movies = loadWatchlist()
    if movie in movies:
        movies.remove(movie)
        newPos = int(input("Enter which position you want to put the movie at: "))
        movies.insert(newPos - 1, movie)
        saveWatchlist(movies)
        print(movie, "'s position has been updated.", sep = "")
        print()
    else:
        movies.append(movie)
        saveWatchlist(movies)
        print(movie, "has been added to the watchlist.")
        print()

def main():
    while True:
        print("Input [1] to view the watchlist")
        print("Input [2] to add a movie to the watchlist")
        print("Input [3] to remove a movie to the watchlist")
        print("Input [4] to rename a movie on the watchlist")
        print("Input [5] to update a movie's position on the watchlist")
        print("Input [6] to exit")
        choice = input("Enter choice: ")
        if choice == "1":
            viewMovies()
        elif choice == "2":
            added = input("Enter the movie you want to add to the watchlist: ")
            addMovie(added)
        elif choice == "3":
            removed = input("Enter the movie you want to remove from the watchlist: ")
            removeMovie(removed)
        elif choice == "4":
            oldName = input("Enter the movie you want to rename: ")
            renameMovie(oldName)
        elif choice == "5":
            posUpdate = input("Enter the movie who's position you want to update: ")
            updateOrder(posUpdate)
        elif choice == "6":
            print()
            break

main()