"""A video playlist class."""


class Playlist:
    """A class used to represent a Playlist."""

    def __init__(self, playlist_name):
        self._playlist_name = playlist_name
        self._videos = []

    @property
    def playlist_name(self):
        return self._playlist_name
    
    @property
    def videos(self):
        return self._videos

    def get_video(self, video_id):
        for video in self._videos:
            if video.video_id == video_id:
                return video

    def add_video(self, video):
        self._videos.append(video)
    
    def in_playlist(self, video_id):
        return any(
            video for video in self._videos 
            if video.video_id == video_id
        )
    
    def remove_video(self, video_id):
        chosen_video = self.get_video(video_id)
        self._videos.remove(chosen_video)
    
    def clear(self):
        self._videos = []
    
    def __repr__(self) -> str:
        return self._playlist_name

    def __eq__(self, o: object) -> bool:
        return self._playlist_name == o._playlist_name
    
    def __lt__(self, other):
        return self._playlist_name < other._playlist_name
