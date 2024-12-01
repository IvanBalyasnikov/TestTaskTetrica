def get_insertion(interval1:list[int], interval2:list[int]) -> list[int]:
    start = max(interval1[0], interval2[0])
    end = min(interval1[1], interval2[1])
    
    if start < end:
        return [start, end]
    else:
        return None


def get_true(interval1:list[int], interval2:list[int]) -> list[int]:
    start = min(interval1[0], interval2[0])
    end = max(interval1[1], interval2[1])
    return [start, end]
    
    

def appearance(intervals: dict[str, list[int]]) -> int:
    abs_time = 0
    pupil_on_lesson_times = []
    tutor_on_lesson_times = []

    for i in range(0, len(intervals['pupil']) - 1, 2):
        insertion = get_insertion([intervals['pupil'][i], intervals['pupil'][i+1]], intervals['lesson'])
        if insertion:
            pupil_on_lesson_times.append(insertion)
        
    
    for i in range(0, len(intervals['tutor']) - 1, 2):
        insertion = get_insertion([intervals['tutor'][i], intervals['tutor'][i+1]], intervals['lesson'])
        if insertion:
            tutor_on_lesson_times.append(insertion)

    


    for i in tutor_on_lesson_times:
        for j in pupil_on_lesson_times:
            insertion = get_insertion(i, j)
            if insertion:
                abs_time += insertion[1] - insertion[0]
            
    return abs_time


   