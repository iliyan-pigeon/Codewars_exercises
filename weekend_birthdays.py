import datetime
import calendar


def most_weekend_birthdays(friends, conversation_date):
    conversation_date = [int(i) for i in conversation_date.split('-')]
    loser_that_wins = ['a', [0, 0]]
    for friend in friends:
        name = friend[0]
        date_of_birth = [int(i) for i in friend[1].split('-')]
        date = date_of_birth
        year = date[0] + 1
        weekends = 0
        while True:
            date[0] = year
            if date[1] > conversation_date[1]:
                break
            elif date[1] == conversation_date[1] and date[2] > conversation_date[2]:
                break
            if datetime.date(*date).weekday() > 4:
                weekends += 1
            if year <  conversation_date[0]:
                year += 1
                continue
            break
        if loser_that_wins[1][0] < weekends:
            loser_that_wins = [name, [weekends, date_of_birth]]
        elif loser_that_wins[1][0] == weekends:
            if loser_that_wins[1][1] > date_of_birth:
                loser_that_wins = [name, [weekends, date_of_birth]]
    return loser_that_wins[0]




print(most_weekend_birthdays([("Alice", "2010-11-10"), ("Bob", "2010-11-23")], "2022-12-31"))
