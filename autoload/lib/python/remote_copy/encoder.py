import base64

from .utils import is_under_tmux


class OSC52Encoder:
    """
    Encoding string with osc52, also support tmux env.
    """

    @staticmethod
    def _encode_under_regular_env(s: str) -> str:
        s_b64 = base64.b64encode(s.encode("utf-8")).decode("utf-8")
        data = "\033]52;c;" + s_b64 + "\007"
        return data

    @staticmethod
    def _encode_under_tmux_env(s: str) -> str:
        s_b64 = base64.b64encode(s.encode("utf-8")).decode("utf-8")
        data = "\033Ptmux;\033\033]52;c;" + s_b64 + "\007\033\\"
        return data

    @classmethod
    def encode(cls, s: str) -> str:
        if is_under_tmux():
            return cls._encode_under_tmux_env(s)

        return cls._encode_under_regular_env(s)
