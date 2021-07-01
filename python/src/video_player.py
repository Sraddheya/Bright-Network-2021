"""A video player class."""

from src.video_playlist import Playlist
from .video_library import VideoLibrary
import operator
import random

class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self._video_playing = ""
        self._video_paused = False
        self._playlist_list = []

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def tags_to_strings(self, video):
        """Helper function to turn tags into string"""

        temp_tags = ""
        for tag in video.tags:
            temp_tags+= tag + " "
        return temp_tags[:-1]

    def show_all_videos(self):
        """Returns all videos."""

        list_all_videos = self._video_library.get_all_videos()
        sorted_videos = sorted(list_all_videos, key=operator.attrgetter('title'))

        print("Here's a list of all available videos:")
        for self._video in sorted_videos:
            print(self._video.title + " (" + self._video.video_id + ") [" + self.tags_to_strings(self._video) + "]")

    def list_of_all_video_ids(self):
        """Make list of all video ids"""
        list_video_ids = []
        for self._video in self._video_library.get_all_videos(): 
            list_video_ids.append(self._video.video_id)
        return list_video_ids

    def play_video(self, video_id): 
        """Plays the respective video."""
        
        if video_id in self.list_of_all_video_ids():
            if self._video_playing != "":
                print("Stopping video: " + self._video_library.get_video(self._video_playing).title)
            self._video_playing = video_id
            self._video_paused = False
            print("Playing video: " + self._video_library.get_video(video_id).title)
        else:
            print ("Cannot play video: Video does not exist")

    def stop_video(self):
        """Stops the current video."""

        if self._video_playing != "":
            print("Stopping video: " + self._video_library.get_video(self._video_playing).title)
        else:
            print("Cannot stop video: No video is currently playing")
        self._video_playing = ""
            
    def play_random_video(self):
        """Plays a random video from the video library."""

        list_all_videos = self._video_library.get_all_videos()
        random_index = random.randint(0,len(list_all_videos)-1)
        self.play_video(list_all_videos[random_index].video_id)

    def pause_video(self):
        """Pauses the current video."""

        if self._video_playing != "":
            title = self._video_library.get_video(self._video_playing).title
            if self._video_paused ==False:
                print("Pausing video: " + title)
                self._video_paused = True
            else:
                print("Video already paused: " + title)
        else:
            print("Cannot pause video: No video is currently playing")

    def continue_video(self):
        """Resumes playing the current video."""

        if self._video_playing != "":
            title = self._video_library.get_video(self._video_playing).title
            if self._video_paused == True:
                print("Continuing video: " + title)
                self._video_paused = False
            else:
                print("Cannot continue video: Video is not paused")
        else:
            print("Cannot continue video: No video is currently playing")

    def show_playing(self):
        """Displays video currently playing."""

        if self._video_playing != "":
            current_video = self._video_library.get_video(self._video_playing)
            if self._video_paused == True:
                print("Currently playing: " + current_video.title + " (" + current_video.video_id + ") [" + self.tags_to_strings(current_video) + "] - PAUSED")
            else:
                print("Currently playing: " + current_video.title + " (" + current_video.video_id + ") [" + self.tags_to_strings(current_video) + "]")
        else:
            print("No video is currently playing")

    def is_playlist_new(self, playlist_name):
        """Helper function to check if playlist already exists."""
        for i in range(len(self._playlist_list)):
            if playlist_name.lower() == self._playlist_list[i].title:
                return i
        return -1

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name."""

        if self.is_playlist_new(playlist_name)>=0:
            print("Cannot create playlist: A playlist with the same name already exists")
        else:
            new_playlist = Playlist(playlist_name.lower())
            self._playlist_list.append(new_playlist)
            print("Successfully created new playlist: " + playlist_name)

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name."""
        
        playlist_index = self.is_playlist_new(playlist_name)

        if playlist_index>=0:
            if video_id in self._playlist_list[playlist_index].video_ids:
                print("Cannot add video to " + playlist_name + ": Video already added")
            elif video_id not in self.list_of_all_video_ids():
                print("Cannot add video to " + playlist_name + ": Video does not exist")
            else:
                self._playlist_list[playlist_index].video_ids.append(video_id)
                print("Added video to " + playlist_name + ": " + self._video_library.get_video(video_id).title)
        else:
            print("Cannot add video to " + playlist_name + ": Playlist does not exist")

    def show_all_playlists(self):
        """Display all playlists."""

        print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
