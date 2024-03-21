grand_clock_time = "15:00"
clock_times = ["14:45", "15:05", "15:00", "14:40"]

def time_difference(grand_clock_time, clock_times):
    """
    두 시계 시간 사이의 시간 차이를 분 단위로 계산합니다.

    파라미터:
        clock_time (str): 시간은 "HH:MM" 형식입니다.
        grand_clock_time (str): 시간은 "HH:MM" 형식입니다.

    반환값 :
        int: 시계 2개의 시간 차이를 분(minute)으로 나타냅니다.
    """



def synchronize_clocks(clock_times, grand_clock_time):
    """
    Synchronizes the given clock times with the grand clock time by calculating the time difference between each clock time and the grand clock time.

    Parameters:
        clock_times (list): A list of clock times in the format of 'hh:mm'.
        grand_clock_time (str): The grand clock time in the format of 'hh:mm'.

    Returns:
        list: A list of time differences between each clock time and the grand clock time.
    """
    time_diffs = []
    for time in clock_times:
        hour_diff = int(time.split(':')[0]) - int(grand_clock_time.split(':')[0])
        minute_diff = int(time.split(':')[1]) - int(grand_clock_time.split(':')[1])
        total_diff = hour_diff * 60 + minute_diff
        time_diffs.append(total_diff)
    return time_diffs

print(synchronize_clocks(clock_times, grand_clock_time)) 