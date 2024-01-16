from datetime import datetime, timedelta


def stat(data):
    players_data_datetime =[datetime.strptime(time, "%H|%M|%S") for time in [player.strip(" ") for player in data.split(",")]]
    players_data = [time for time in [player.strip(" ") for player in data.split(",")]]
    data_range = max(players_data_datetime) - min(players_data_datetime)
    timedelta_list = [datetime.strptime(time, "%H|%M|%S") - datetime(1900, 1, 1) for time in players_data]
    data_average = sum(timedelta_list, timedelta()) / len(timedelta_list)
    data_median = 0

    return data_average


print(stat("01|15|59, 1|47|16, 01|17|20, 1|32|34, 2|17|17"))