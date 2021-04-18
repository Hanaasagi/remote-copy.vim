import os

from .encoder import OSC52Encoder


# echo -e "\ePtmux;\e\e]52;c;aGVsbG8=\x07\e\\"
# echo "\ePtmux;\e\e]52;c;aGVsbG8=\x07\e\\"
# print("\033Ptmux;\033\033]52;c;aGVsbG8=\x07\033\\")
# data = "\033Ptmux;\033\033]52;c;aGVsbG8=\x07\033\\"
def copy2clipboard(s: str) -> None:
    """Copy the data to system clipboard"""
    data = OSC52Encoder.encode(s)
    stdout_fd = os.path.join("/proc/", str(os.getppid()), "fd/1")

    with open(stdout_fd, "a") as f:
        f.write(data)
        f.flush()
