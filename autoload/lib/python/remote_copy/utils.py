import os


def is_under_tmux() -> bool:
    """
    Return `True` if running under tmux.
    """

    return os.getenv("TMUX", "").strip() != ""
