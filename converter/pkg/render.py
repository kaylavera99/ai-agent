def box(text: str) -> str:
    lines = [l.strip() for l in text.splitlines() if l.strip() is not None]
    width = max((len(l) for l in lines), default=0)
    top = "┌" + "─" * (width + 2) + "┐"
    mid = ["│ " + l.ljust(width) + " │" for l in lines]
    bottom = "└" + "─" * (width + 2) + "┘"
    return "\n".join([top] + mid + [bottom])