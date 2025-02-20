def seconds_to_str(seconds):
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    if hours == 0:
        return "%02d:%02d" % (minutes, seconds)

    return "%02d:%02d:%02d" % (hours, minutes, seconds)