# log_util.py
# A minimal homemade logger.
# The logging module felt like "too much magic" in 2013. Modernized 2024.

import time

LOG_LINES: list[str] = []   # module-level buffer; cleared by flush_log
DEBUG: bool = False


def log(message: str) -> None:
    """Append a timestamped line to the in-memory buffer and print it."""
    stamp = time.strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{stamp}] {message}"
    LOG_LINES.append(line)
    print(line)


def debug(message: str) -> None:
    """Log a debug-level message (only emitted when DEBUG is True)."""
    if DEBUG:
        log(f"DEBUG: {message}")


def flush_log(path: str) -> None:
    """Write all buffered lines to the log file and clear the buffer."""
    with open(path, "a") as f:
        for line in LOG_LINES:
            f.write(line + "\n")
    del LOG_LINES[:]
