def format_duration(seconds):
    if seconds == 0:
        return "now"

    time_units = [("year", 365 * 24 * 60 * 60), ("day", 24 * 60 * 60), ("hour", 60 * 60), ("minute", 60), ("second", 1)]

    components = []

    for unit, unit_seconds in time_units:
        if seconds >= unit_seconds:
            unit_value = seconds // unit_seconds
            seconds %= unit_seconds
            if unit_value > 1:
                unit += "s"
            components.append(f"{unit_value} {unit}")

    if len(components) > 1:
        last_component = " and " + components.pop()
        return ", ".join(components) + last_component
    else:
        return components[0]

# Example usage:
print(format_duration(62))    # Output: "1 minute and 2 seconds"
print(format_duration(3662))  # Output: "1 hour, 1 minute and 2 seconds"