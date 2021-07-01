"""A video player class."""

from .video_library import VideoLibrary
import random
from random import seed
from random import randint

playing = False
current = None
new = None
paused= False
playlists = []

class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        videos = self._video_library.get_all_videos()
        list = []
        print("Here's a list of all available videos:")

        # for each video on the list
        for x in videos:
            #
            # The following for loop removes the brackets and apostrophes from tags
            # Initialise a variable i
            i = 0
            newtags = ""
            for tag in x.tags:
                # Increment i by 1 each loop
                i += 1
                newtags += tag
                # As long as i is not equal to the length of x.tags (the number of tags), put a space " "
                # this is to separate the tags out
                # Otherwise, the space is not added, so there will be no space before the square bracket to close it
                if i !=len(x.tags):
                    newtags = newtags + " "
            #
            # Add information to list, using x.title to get the title of the xth video in the list
            # Use just {newtags} because we have a new tags list for every x (in the loop)
            # Indent inside string for formatting
            list += [f" {j.title} ({j.video_id}) [{newtags}]"]
        # sorted() sorts the list in alphabetical order
        for item in sorted(list):
            print(item)

    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """
        global playing
        global current
        global new
        global paused
        new = self._video_library.get_video(video_id)

        if not new:
            print(f"Cannot play video: Video does not exist")
        else:
            if playing is True:
                print(f"Stopping video: {current}")
                print(f"Playing video: {new.title}")
                current = new.title
                paused = False
            else:
                print(f"Playing video: {new.title}")
                playing = True
                current = new.title


    def stop_video(self):
        """Stops the current video."""
        global playing
        global current
        global paused

        if playing is True:
            print(f"Stopping video: {current}")
            current = None
            playing = False
            paused = False
        else:
            print(f"Cannot stop video: No video is currently playing")

    def play_random_video(self):
        """Plays a random video from the video library."""
        global playing
        global current
        global paused
        global new

        new = random.choice(self._video_library.get_all_videos())

        if playing is True:
            print(f"Stopping video: {current}")
            print(f"Playing video: {new.title}")
            current = new.title
        else:
            print(f"Playing video: {new.title}")
            playing = True
            current = new.title
            paused = False

    def pause_video(self):
        """Pauses the current video."""
        global playing
        global paused
        global current

        if paused is True:
            print(f"Video is already paused: {current}")
        if playing is True:
            if paused is False:
                paused = True
                print(f"Cannot pause video: No video is currently playing")

    def continue_video(self):
        """Resumes playing the current video."""
        global playing
        global paused
        global current

        if playing is True:
            if paused is False:
                print(f"Cannot continue video: Video is not paused")
                if paused is True:
                    print(f"Continuting video: {current}")
                    paused = False
            if playing is False:
                print(f"Cannot continue video: No video is currently playing")

    def show_playing(self):
        """Displays video currently playing."""
        global playing
        global paused
        global current
        global new

        if playing is False:
            print(f"No video is currently playing")
        if playing is True:
            #
            i = 0
            newtags = ""
            for tag in new.tags:
                i += 1
                newtags += tag
                if i != len(new.tags):
                    newtags = newtags + " "
            #
            if paused is False:
                print(f"Currently playing: {current} ({new.video_id} [{newtags}]")
            if paused is True:
                print(f"Currently playing: {current} ({new.video_id}) [{newtags}] - PAUSED")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        global playlists

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        print("add_to_playlist needs implementation")

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
        all_vids = self._video_library.get_all_videos()

        response = []
        for vid in all_vids:
            if search_term.lower() in vid._title.lower():
                response.append(vid)

        if (len(response) !=0):
            i = 1
            print("Here are the results for "+ search_term + ":")
            for x in response:

                details = str(x.title + " (" + x._video_id +") [" + ' '.join(list(x.tags)) + "]")

                print(f"{details})")
                i += 1
            print("Would you like to play any of the above? If so, specify the number of the video.")
            print("If your answer is not a valid number, it will be assumed as a no")

            num = input()

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
