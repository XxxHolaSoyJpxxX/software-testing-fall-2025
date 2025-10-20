# -*- coding: utf-8 -*-
import unittest
from unittest import mock
from unittest.mock import patch

from white_box.examen_2_exercise_2 import (
    Song,
	SongStore,
    main,
)


class TestSongStore(unittest.TestCase):
    """Unit tests for Song and SongStore classes."""

    def setUp(self):
        """Set up test environment."""
        self.song1 = Song("Song One", "Author A", "Album X", 2000)
        self.song2 = Song("Song Two", "Author B", "Album Y", 2005)
        self.store = SongStore()

    @patch("builtins.print")
    def test_song_display(self, mock_print):
        """Test display of a Song instance."""
        self.song1.display()
        mock_print.assert_any_call("Title: Song One")
        mock_print.assert_any_call("Author: Author A")
        mock_print.assert_any_call("Album: Album X")
        mock_print.assert_any_call("Year: 2000")

	
    @patch("builtins.print")
    def test_add_song(self, mock_print):
        """Test adding a song to the store."""
        self.store.add_song(self.song1)
        self.assertIn(self.song1, self.store.songs)
        mock_print.assert_any_call("Song 'Song One' added to the store.")

    @patch("builtins.print")
    def test_display_store_empty(self, mock_print):
        """Test displaying songs when store is empty."""
        self.store.display_songs()
        mock_print.assert_any_call("No songs in the store.")

    @patch("builtins.print")
    def test_display_store_not_empty(self, mock_print):
        """Test displaying songs when store has songs."""
        self.store.add_song(self.song1)
        self.store.add_song(self.song2)
        self.store.display_songs()
        mock_print.assert_any_call("Songs available in the store:")
        mock_print.assert_any_call("Title: Song One")
        mock_print.assert_any_call("Title: Song Two")

    @patch("builtins.print")
    def test_search_song_found(self, mock_print):
        """Test searching for a song that exists."""
        self.store.add_song(self.song1)
        self.store.add_song(self.song2)
        self.store.search_song("Song One")
        mock_print.assert_any_call("Found 1 song(s) with title 'Song One':")
        mock_print.assert_any_call("Title: Song One")

    @patch("builtins.print")
    def test_search_song_not_found(self, mock_print):
        """Test searching for a song that does not exist."""
        self.store.add_song(self.song1)
        self.store.search_song("Nonexistent")
        mock_print.assert_any_call("No song found with title 'Nonexistent'.")

    @patch("builtins.input", side_effect=[
        "3", "New Song", "Author C", "Album Z", "2010",
        "1",
        "2", "New Song",
        "4"
    ])
    @patch("builtins.print")
    def test_main_flow(self, mock_print, mock_input):
        """Test main function flow."""
        main()
        mock_print.assert_any_call("Song 'New Song' added to the store.")
        mock_print.assert_any_call("Songs available in the store:")
        mock_print.assert_any_call("Title: New Song")
        mock_print.assert_any_call("Found 1 song(s) with title 'New Song':")
        mock_print.assert_any_call("Exiting...")


