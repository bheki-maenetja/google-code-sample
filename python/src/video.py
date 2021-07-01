"""A video class."""

from typing import Sequence


class Video:
    """A class used to represent a Video."""

    def __init__(self, video_title: str, video_id: str, video_tags: Sequence[str]):
        """Video constructor."""
        self._title = video_title
        self._video_id = video_id
        self._is_flagged = False
        self._flag_reason = ""
        # Turn the tags into a tuple here so it's unmodifiable,
        # in case the caller changes the 'video_tags' they passed to us
        self._tags = tuple(video_tags)

    @property
    def title(self) -> str:
        """Returns the title of a video."""
        return self._title

    @property
    def video_id(self) -> str:
        """Returns the video id of a video."""
        return self._video_id

    @property
    def tags(self) -> Sequence[str]:
        """Returns the list of tags of a video."""
        return self._tags
    
    @property
    def is_flagged(self):
        return self._is_flagged
    
    @property
    def flag_reason(self):
        return self._flag_reason
    
    def flag(self, reason=None):
        self._is_flagged = True
        self._flag_reason = reason
    
    def unflag(self):
        self._is_flagged = False
        self._flag_reason = ""
    
    def get_flag_reason(self):
        if self._flag_reason:
            return f"(reason: {self._flag_reason})"
        return "(reason: Not supplied)"
    
    def __repr__(self):
        return f"{self.title} ({self.video_id}) [{' '.join(self.tags)}]"
    
    def __lt__(self, other):
        return self.title < other.title