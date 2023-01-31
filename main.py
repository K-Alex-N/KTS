def seconds_to_str(seconds: int) -> str:
    res = []
    s = seconds % 60
    res.append(f'{s:02}s')
    seconds //= 60
    if seconds:
        m = seconds % 60
        res.append(f'{m:02}m')
        seconds //= 60 * (m if m else 1)
        if seconds:
            h = seconds % 24
            res.append(f'{h:02}h')
            seconds //= 24 * (h if h else 1)
            if seconds:
                res.append(f'{seconds:02}d')

    return ''.join(reversed(res))
