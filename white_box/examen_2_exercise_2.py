# -*- coding: utf-8 -*-
# pylint: disable=R0903
"""Simple Song and SongStore management system with CLI interface."""


class Song:
    """Represents a song with title, author, album, and year."""

    def __init__(self, title, author, album, year):
        """Initialize a Song instance."""
        self.title = title
        self.author = author
        self.album = album
        self.year = year

    def display(self):
        """Print the details of the song."""
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Album: {self.album}")
        print(f"Year: {self.year}")


class SongStore:
    """Stores and manages a collection of songs."""

    def __init__(self):
        """Initialize the song list."""
        self.songs = []

    def add_song(self, song):
        """Add a song to the store."""
        self.songs.append(song)
        print(f"Song '{song.title}' added to the store.")

    def display_songs(self):
        """Display all songs in the store."""
        if not self.songs:
            print("No songs in the store.")
        else:
            print("Songs available in the store:")
            for song in self.songs:
                song.display()

    def search_song(self, title):
        """Search for songs by title (case-insensitive)."""
        found_songs = [
            song for song in self.songs if song.title.lower() == title.lower()
        ]
        if not found_songs:
            print(f"No song found with title '{title}'.")
        else:
            print(f"Found {len(found_songs)} song(s) with title '{title}':")
            for song in found_songs:
                song.display()


def main():
    """Command-line interface for interacting with the SongStore."""
    songstore = SongStore()

    while True:
        print(
            "\n1. Display all songs\n2. Search for a song\n3. Add a new song\n4. Exit"
        )
        choice = input("Enter your choice: ")

        if choice == "1":
            songstore.display_songs()
        elif choice == "2":
            title = input("Enter the title of the song you want to search: ")
            songstore.search_song(title)
        elif choice == "3":
            title = input("Enter the title of the song: ")
            author = input("Enter the author of the song: ")
            album = input("Enter the album of the song: ")
            year = int(input("Enter the year of the song: "))
            new_song = Song(title, author, album, year)
            songstore.add_song(new_song)
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
