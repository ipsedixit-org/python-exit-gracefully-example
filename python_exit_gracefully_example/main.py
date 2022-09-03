import signal
import time


def handler(signum, frame):
    msg = "\nCtrl-c was pressed, exit gracefully"
    print(msg, end="\n")
    exit(0)


signal.signal(signal.SIGINT, handler)


def main():
    count = 0
    while True:
        print(f"Seconds elapsed {count}", end="\r", flush=True)
        time.sleep(1)
        count += 1


if __name__ == "__main__":
    main()
