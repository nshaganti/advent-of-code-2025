from typing import Iterable, List, Tuple


def parse_input(lines: Iterable[str]) -> List[str]:
    """
    Accepts an iterable of lines (file or string splitlines()) and returns cleaned rotation strings.
    Example rotation: "L68" or "R14".
    """
    return [line.strip() for line in lines if line and line.strip()]


def validate_start_pos(start_pos: int) -> None:
    if not isinstance(start_pos, int):
        raise TypeError("start_pos must be an integer")
    if not (0 <= start_pos < 100):
        raise ValueError("start_pos must be in range [0, 99]")


def parse_rotation(rotation: str) -> Tuple[str, int]:
    rotation = rotation.strip()
    if not rotation:
        raise ValueError("empty rotation")
    dir_char = rotation[0].upper()
    if dir_char not in ("L", "R"):
        raise ValueError(f"invalid rotation direction: {rotation!r}")
    try:
        moves = int(rotation[1:])
    except Exception:
        raise ValueError(f"invalid rotation moves: {rotation!r}")
    if moves < 0:
        raise ValueError("moves must be non-negative")
    return dir_char, moves
