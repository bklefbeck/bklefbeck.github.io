import math
from datetime import datetime

current_date_and_time = datetime.now()

print(f"{current_date_and_time:%Y-%m-%d}")

width = float(input("Enter the width of the tire in mm (e.g. 205): "))
aspect_ratio = float(input("Enter the aspect ratio of the tire (e.g. 60): "))
diameter = float(input("Enter the diameter of the wheel in inches (e.g. 15): "))

volume = (
    math.pi * width ** 2 * aspect_ratio *
    (width * aspect_ratio + 2540 * diameter)
) / 10000000000

print(f"\nThe approximate volume is {volume:.2f} liters")

with open("volume.txt", "a") as volume_file:
    volume_file.write(
        f"{current_date_and_time}, {width}, {aspect_ratio}, {diameter}, {volume:.2f}\n"
    )
