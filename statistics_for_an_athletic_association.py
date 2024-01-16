from datetime import datetime, timedelta


def stat(data):
    players_data_datetime =[datetime.strptime(time, "%H|%M|%S") for time in [player.strip(" ") for player in data.split(",")]]
    players_data = [time for time in [player.strip(" ") for player in data.split(",")]]
    data_range = max(players_data_datetime) - min(players_data_datetime)
    timedelta_list = [datetime.strptime(time, "%H|%M|%S") - datetime(1900, 1, 1) for time in players_data]
    data_average = sum(timedelta_list, timedelta()) / len(timedelta_list)
    data_average_list = []
    data_median = 0
    data_median_list = []

    for i in str(data_average).split(":"):
        if "." in i:
            i = i.split(".")[0]
        data_average_list.append(i)

    sorted_timedelta_list = sorted(timedelta_list)
    middle_index = len(sorted_timedelta_list) // 2

    if len(sorted_timedelta_list) % 2 == 0:
        median = (sorted_timedelta_list[middle_index - 1] + sorted_timedelta_list[middle_index]) / 2
    else:
        median = sorted_timedelta_list[middle_index]

    # Format the median timedelta as HH:MM:SS
    data_median = str(datetime(1900, 1, 1) + median).split()[1]

    for i in str(data_median).split(":"):
        if "." in i:
            i = i.split(".")[0]
        data_median_list.append(i)

    data_range = str(data_range).split(":")
    data_average = data_average_list
    data_median = data_median_list
    data_range = str(f"{int(data_range[0]):02d}") + "|" + data_range[1] + "|" + data_range[2]
    data_average = str(f"{int(data_average[0]):02d}") + "|" + data_average[1] + "|" + data_average[2]
    data_median = str(f"{int(data_median[0]):02d}") + "|" + data_median[1] + "|" + data_median[2]

    return f"Range: {data_range} Average: {data_average} Median: {data_median}"


print(stat("01|15|59, 1|47|16, 01|17|20, 1|32|34, 2|17|17"))