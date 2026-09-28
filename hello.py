import time
from datetime import date


def main():
    print("Hello, world! I am Wayne518.")
    print(f"Today is {date.today()}.")

    print("Countdown starting:")
    for i in range(3, 0, -1):
        print(f"{i}...")
        time.sleep(1)
    print("Blast off!")


if __name__ == "__main__":
    main()
