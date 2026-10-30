# ==========FILE: tracker_my_first_app.py==========

# This is a mood tracker app
# I collects mood data once a day
# Use case: you can't actively change your mood if you don't know 

from datetime import date as dt_date
import csv

# CONSTANTS:
FILENAME = "stats.csv"

# Collect data
def log_entry():
    today = str(dt_date.today())
    moods = ["Happy", "Sad", "Carefree", "Reckless"]
    current_mood = input(f"Choose from the list ONLY ONE that applies: {moods} ").capitalize()

    with open(FILENAME, mode = "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([today, current_mood])

    print(f"Logged: {today} --> {current_mood}")

# Read and calculate stats
def read_entries():

    with open(FILENAME, mode = "r") as file:
        reader = csv.reader(file)
        entries = [row for row in reader]
    return entries

def calculate_stats(entries):
    count_happy = 0
    count_sad = 0
    count_carefree = 0
    count_reckless = 0
    number_of_days = 0

    for day, mood in entries:
        if day:
            mood_count = {
                "Happy" : count_happy,
                "Sad" : count_sad,
                "Carefree" : count_carefree,
                "Reckless" : count_reckless
            }

    average_happy = count_happy/number_of_days
    average_sad = count_sad/number_of_days
    average_carefree = count_carefree/number_of_days
    average_reckless = count_reckless/number_of_days

    highest_recorded_mood = max(mood_count, key=mood_count.get)
    least_recorded_mood = min(mood_count, key=mood_count.get)

    best_day = "" #not sure how to iimplement this line
    worst_day = "" #not sure how to implement this line

    return highest_recorded_mood, least_recorded_mood, average_happy, average_sad,average_carefree, average_reckless

        