# seconds_to_str(20) == '20s'
# seconds_to_str(60) == '01m00s'
# seconds_to_str(65) == '01m05s'
# seconds_to_str(3700) == '01h01m40s'
# seconds_to_str(93600) == '01d02h00m00s

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

print(seconds_to_str(2))
print(seconds_to_str(20))
print(seconds_to_str(60))
print(seconds_to_str(65))
print(seconds_to_str(3700))
print(seconds_to_str(93600))
