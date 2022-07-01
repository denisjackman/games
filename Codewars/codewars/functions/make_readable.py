def make_readable(seconds):
    time = seconds
    secs = seconds % 60
    rest = time - secs
    time = rest / 60
    minutes = time % 60
    rest = time - minutes
    hours = rest / 60
    tsec = '{:0>2}'.format(secs)
    tmin = '{:0>2}'.format(minutes)
    thour = '{:0>2}'.format(hours)
    return thour + ":" + tmin + ":" + tsec


print make_readable(0)
print make_readable(5)
print make_readable(60)
print make_readable(86399)
print make_readable(359999)


print make_readable(0) == "00:00:00"
print make_readable(5) == "00:00:05"
print make_readable(60) == "00:01:00"
print make_readable(86399) == "23:59:59"
print make_readable(359999) == "99:59:59"