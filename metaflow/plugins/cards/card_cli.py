@contextmanager
def timeout(time):
    import sys

    if sys.platform == "win32":
        raise RuntimeError(
            "Card timeout is not supported on Windows (SIGALRM is POSIX-only)."
        )

    # Register a function to raise a TimeoutError on the signal.
    signal.signal(signal.SIGALRM, raise_timeout)

    # Schedule the signal to be sent after ``time``.
    signal.alarm(time)

    try:
        yield
    finally:
        # Unregister the signal so that it won't be triggered
        # if the timeout is not reached.
        signal.signal(signal.SIGALRM, signal.SIG_IGN)
