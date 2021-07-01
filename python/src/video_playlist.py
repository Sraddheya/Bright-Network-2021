"""A video playlist class."""


from typing import List


class Playlist:
    """A class used to represent a Playlist."""

    def __init__(self, playlist_title: str):
        """Playlist constructor."""
        self._title = playlist_title
        self._video_ids = []

    @property
    def title(self) -> str:
        """Returns the title of the playlist."""
        return self._title

    @property
    def video_ids(self) -> List[str]:
        """Returns the list of tags of a video."""
        return self._video_ids
