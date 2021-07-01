"""A video player class."""

from .video_playlist import Playlist
from .video_library import VideoLibrary
from random import choice


class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self._playlists = {}
        self._current_video = None
        self._is_paused = False 

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        print("Here's a list of all available videos:")
        for video in sorted(self._video_library.get_all_videos()):
            if video.is_flagged:
                print(f"  {video} - FLAGGED {video.get_flag_reason()}")
                continue
            print(f"  {video}")

    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """
        video = self._video_library.get_video(video_id)
        if not video:
            print("Cannot play video: Video does not exist")
            return None
        
        if video.is_flagged:
            print(f"Cannot play video: Video is currently flagged {video.get_flag_reason()}")
            return None
        
        if self._current_video:
            self.stop_video()
        print(f"Playing video: {video.title}")
        self._current_video = video
        self._is_paused = False

    def stop_video(self):
        """Stops the current video."""
        if self._current_video:
            print(f"Stopping video: {self._current_video.title}")
        else:
            print("Cannot stop video: No video is currently playing")
        self._current_video = None
        self._is_paused = False

    def play_random_video(self):
        """Plays a random video from the video library."""
        valid_videos = [
            video.video_id
            for video in self._video_library.get_all_videos()
            if not video.is_flagged
        ]

        if valid_videos == []:
            print("No videos available")
            return None

        random_video_id = choice(valid_videos)
        self.play_video(random_video_id)

    def pause_video(self):
        """Pauses the current video."""
        if not self._current_video:
            print("Cannot pause video: No video is currently playing")
            return None

        if not self._is_paused:
            print(f"Pausing video: {self._current_video.title}")
            self._is_paused = True
        else:
            print(f"Video already paused: {self._current_video.title}")
        
    def continue_video(self):
        """Resumes playing the current video."""
        if not self._current_video:
            print("Cannot continue video: No video is currently playing")
        elif not self._is_paused:
            print("Cannot continue video: Video is not paused")
        else:
            print(f"Continuing video: {self._current_video.title}")
            self._is_paused = False

    def show_playing(self):
        """Displays video currently playing."""
        if not self._current_video:
            print("No video is currently playing")
            return
        
        if self._is_paused:
            print(f"Currently playing: {self._current_video} - PAUSED")
        else:
            print(f"Currently playing: {self._current_video}")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        if playlist_name.lower() in list(self._playlists.keys()):
            print("Cannot create playlist: A playlist with the same name already exists")
            return None
        
        new_playlist = Playlist(playlist_name)
        self._playlists[playlist_name.lower()] = new_playlist
        print(f"Successfully created new playlist: {new_playlist}")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        video = self._video_library.get_video(video_id)
        playlist = self._playlists.get(playlist_name.lower(), None)

        if not playlist:
            print(f"Cannot add video to {playlist_name}: Playlist does not exist")
            return None
        
        if not video:
            print(f"Cannot add video to {playlist_name}: Video does not exist")
            return None
        
        if video.is_flagged:
            print(f"Cannot add video to {playlist_name}: Video is currently flagged {video.get_flag_reason()}")
            return None

        if playlist.in_playlist(video.video_id):
            print(f"Cannot add video to {playlist_name}: Video already added")
        else:
            playlist.add_video(video)
            print(f"Added video to {playlist_name}: {video.title}")

    def show_all_playlists(self):
        """Display all playlists."""
        if len(self._playlists) == 0:
            print("No playlists exist yet")
        else:
            print("Showing all playlists:")
            for playlist in sorted(self._playlists.values()):
                print(f"  {playlist}")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        playlist = self._playlists.get(playlist_name.lower(), None)
        if not playlist:
            print(f"Cannot show playlist {playlist_name}: Playlist does not exist")
            return None
        
        print(f"Showing playlist: {playlist_name}")
        if playlist.videos == []:
            print("No videos here yet")
        else:
            for video in playlist.videos:
                if video.is_flagged:
                    print(f"  {video} - FLAGGED {video.get_flag_reason()}")
                    continue
                print(f"  {video}")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        playlist = self._playlists.get(playlist_name.lower(), None)
        video = self._video_library.get_video(video_id)

        if not playlist:
            print(f"Cannot remove video from {playlist_name}: Playlist does not exist")
            return None
        
        if not video:
            print(f"Cannot remove video from {playlist_name}: Video does not exist")
            return None
        
        if not playlist.in_playlist(video.video_id):
            print(f"Cannot remove video from {playlist_name}: Video is not in playlist")
            return None
        
        playlist.remove_video(video.video_id)
        print(f"Removed video from {playlist_name}: {video.title}")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        playlist = self._playlists.get(playlist_name.lower(), None)
        if not playlist:
            print(f"Cannot clear playlist {playlist_name}: Playlist does not exist")
            return None
        
        playlist.clear()
        print(f"Successfully removed all videos from {playlist_name}")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        playlist = self._playlists.get(playlist_name.lower(), None)
        if not playlist:
            print(f"Cannot delete playlist {playlist_name}: Playlist does not exist")
            return None
        
        del self._playlists[playlist_name.lower()]
        print(f"Deleted playlist: {playlist_name}")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        search_term = search_term.lower()
        search_results = sorted([
            video for video in self._video_library.get_all_videos() 
            if search_term in video.title.lower() and not video._is_flagged
        ])

        if search_results == []:
            print(f"No search results for {search_term}")
        else:
            print(f"Here are the results for {search_term}:")
            for index, video in enumerate(search_results):
                print(f"  {index + 1}) {video}")
            self.video_selector(search_results)
    
    def video_selector(self, search_results):
        """Allows the user to select a video from a set of search results
        
        Args:
            search_results: a sorted list of videos resulting from a search
        """
        print("Would you like to play any of the above? If yes, specify the number of the video.")
        print("If your answer is not a valid number, we will assume it's a no.")
        index = input()

        if index.isdigit():
            index = int(index)
            if index in range(1, len(search_results) + 1):
                video = search_results[index - 1]
                self.play_video(video.video_id)

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        search_results = sorted([
            video for video in self._video_library.get_all_videos() 
            if video_tag in video.tags and not video.is_flagged
        ])

        if search_results == []:
            print(f"No search results for {video_tag}")
        else:
            print(f"Here are the results for {video_tag}:")
            for index, video in enumerate(search_results):
                print(f"  {index + 1}) {video}")
            self.video_selector(search_results)

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        video = self._video_library.get_video(video_id)
        if not video:
            print("Cannot flag video: Video does not exist")
            return None
        
        if video.is_flagged:
            print("Cannot flag video: Video is already flagged")
            return None
        
        if video == self._current_video:
            self.stop_video()
        
        video.flag(flag_reason)
        print(f"Successfully flagged video: {video.title} {video.get_flag_reason()}")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        video = self._video_library.get_video(video_id)
        if not video:
            print("Cannot remove flag from video: Video does not exist")
            return None
        
        if not video.is_flagged:
            print("Cannot remove flag from video: Video is not flagged")
            return None
        
        video.unflag()
        print(f"Successfully removed flag from video: {video.title}")


