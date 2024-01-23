def decode_smoke_signals(days):
    signals = {}

    for day in days:
        current_signals = {}

        for signal in day[0]:
            if signal not in current_signals:
                current_signals[signal] = []

        for message in day[1]:
            for current_signal in current_signals:
                if message not in current_signals[current_signal]:
                    current_signals[current_signal].append(message)

        for signal, messages in current_signals.items():
            if signal not in signals:
                signals[signal] = []
                for message in messages:
                    signals[signal].append(message)
            else:
                for message in messages:
                    if message in signals[signal]:
                        signals[signal].append(message)

    filtered_data = {}

    for signal, messages in signals.items():
        message_counts = {message: messages.count(message) for message in set(messages)}
        max_count = max(message_counts.values())
        filtered_messages = [message for message, count in message_counts.items() if count == max_count]

        if signal not in filtered_data:
            filtered_data[signal] = filtered_messages
        else:
            filtered_data[signal].extend(filtered_messages)

    signals = filtered_data
    result = {}
    while signals:
        for signal, messages in signals.items():
            if len(messages) == 1:
                result[signal] = messages[0]
                del signals[signal]
                break
            for key, value in result.items():
                for message in messages:
                    if value == message:
                        messages.remove(message)
                        break

    return result



the_days =[(["8.2.1", "4.3.4", "1"], ["Ambush in the jungle", "General assassinated", "Ambush in the jungle"]),
 (["1", "2.2", "9.3"], ["Ambush in the jungle", "Orange army retreats", "Push into the mountains"]),
 (["4.3.4", "6"], ["Ambush in the jungle", "Orange general goes on vacation"]),
 (["8.2.1", "9.3", "1"], ["Ambush in the jungle", "General assassinated", "Push into the mountains"])]
print(decode_smoke_signals(the_days))