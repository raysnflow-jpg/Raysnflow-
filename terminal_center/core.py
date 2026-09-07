import re

_ANSI_RE = re.compile(r'\x1B[@-_][0-?]*[ -/]*[@-~]')


def strip_ansi(s: str) -> str:
    """Remove ANSI escape sequences from a string."""
    if not s:
        return s
    return _ANSI_RE.sub("", s)


def printable_width(s: str) -> int:
    """Return the printable width of s (ignoring ANSI escape sequences)."""
    return len(strip_ansi(s))


def center_line(text: str, width: int) -> str:
    """Center `text` into a field `width` characters wide.

    - If printable width of text >= width: return original `text` unchanged.
    - Preserves any ANSI sequences in `text`.
    - Pads with spaces; left pad = total//2, right pad = total - left pad.
    """
    if width is None:
        return text
    pw = printable_width(text)
    if pw >= width:
        return text
    total_pad = width - pw
    left = total_pad // 2
    right = total_pad - left
    return " " * left + text + " " * right
