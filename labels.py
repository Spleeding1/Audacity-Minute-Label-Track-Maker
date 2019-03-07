import os

def make_track_labels(number_of_tracks):
    for i in range(number_of_tracks):
        n = i + 1
        number = format(n, '02')
        _file = open(f'/Users/CrazyCarl/Desktop/Label_Tracks/{number}_min_label_track.txt', 'w+')
        for r in range(n):
            start = r * 60
            end = (r + 1) * 60
            track_number = r + 1
            burn_number = format(track_number, '02')
            
            _file.write('%d.000000	%d.000000	%s\n' % (start, end, burn_number))
        _file.close()