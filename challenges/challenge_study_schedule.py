def study_schedule(permanence_period, target_time):

    if target_time is None:
        return None

    contador = 0
    for entrada, saida in permanence_period:
        if entrada <= target_time < saida:
            contador += 1

    return contador
