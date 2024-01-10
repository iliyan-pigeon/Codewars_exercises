import datetime
import calendar


def most_weekend_birthdays(friends, conversation_date):
    conversation_date = [int(i) for i in conversation_date.split('-')]
    friends_data = []
    winner = None

    for i in range(len(friends)):
        friends_data.append({'name': friends[i][0], 'birthday': [int(i) for i in friends[i][1].split("-")], 'weekends_count': 0})

    for friend in friends_data:
        friend_birthday = friend['birthday']
        year = friend_birthday[0]
        month = friend_birthday[1]
        day = friend_birthday[2]

        while True:
            year += 1

            if not calendar.isleap(year) and day == 29:
                day -= 1
            if datetime.date(year, month, day) < datetime.date(*conversation_date):
                if datetime.date(year, month, day).weekday() > 4:
                    friend['weekends_count'] += 1
            else:
                break

    for friend in friends_data:
        if winner is None:
            winner = friend
        elif winner['weekends_count'] < friend['weekends_count']:
            winner = friend
        elif winner['weekends_count'] == friend['weekends_count']:
            if datetime.date(*winner['birthday']) < datetime.date(*friend['birthday']):
                winner = friend
            else:
                pass

    return winner['name']


print(most_weekend_birthdays([("Steve", "2010-11-18"), ("Dave", "2010-11-22")], "2022-12-31"))
