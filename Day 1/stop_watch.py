import time


def stop_watch():
    """
    Implements a simple stopwatch.

    The stopwatch starts when the user presses Enter and stops when they press Enter again.
    It then calculates and displays the elapsed time in hours, minutes, and seconds.
    """
    input("Press Enter to start the stopwatch...")
    start = time.time()

    input("Stopwatch started... Press Enter to stop.")
    elapsed_time = int(time.time() - start)

    hrs, remainder = divmod(elapsed_time, 3600)
    minutes, sec = divmod(remainder, 60)

    print("\n-----------------------")
    print(f"| {hrs:02} HRS : {minutes:02} MIN : {sec:02} SEC |")
    print("-----------------------")


if __name__ == "__main__":
    stop_watch()
