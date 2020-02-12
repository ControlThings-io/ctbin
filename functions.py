import math

def progress_bar(percentage: float, width: int) -> str:
    ''' 
    Return a unicode percentage bar for given percentage
    
    :PARAM percentage: 0 <= percentage <= 1
    '''
    percentage = min(1, max(0, percentage))
    whole_width = math.floor(percentage * width)
    remainder_width = (percentage * width) % 1
    part_width = math.floor(remainder_width * 8)
    part_char = [" ", "▏", "▎", "▍", "▌", "▋", "▊", "▉"][part_width]
    if (width - whole_width - 1) < 0:
        part_char = ""
    bar = "[" + "█" * whole_width + part_char + " " * (width - whole_width - 1) + "]"
    return bar
    