def study_schedule(permanence_period, target_time):

    if target_time is None:
        return None
    contador = 0
    if not all(
        isinstance(start, int) and isinstance(end, int)
        for start, end in permanence_period
    ):
        return None
    for start, end in permanence_period:
      if start <= target_time <= end:
         contador += 1
    

    return contador
