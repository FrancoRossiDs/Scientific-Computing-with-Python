def add_time(start_time, duration_time, starting_day=''):
    days_of_the_week = ['monday', 'tuesday', 'wednesday', 
                        'thursday', 'friday', 'saturday', 'sunday']
    extra_day = 0
    final_day = ''
    
    # Separar la hora inicial y AM/PM
    final_time, period = start_time.split()
    hours, minutes = map(int, final_time.split(':'))
    extra_hours, extra_minutes = map(int, duration_time.split(':'))

    # Pasar todo a minutos desde las 00:00
    total_minutes = hours % 12 * 60 + minutes   # %12 para que 12:xx no rompa
    if period == "PM":
        total_minutes += 12 * 60
    total_minutes += extra_hours * 60 + extra_minutes

    # Calcular días y ajustar horas
    extra_day = total_minutes // (24 * 60)
    total_minutes %= (24 * 60)

    # Reconstruir la hora final en formato 12h
    final_hours = (total_minutes // 60) % 12
    final_hours = 12 if final_hours == 0 else final_hours
    final_minutes = total_minutes % 60
    period = "AM" if total_minutes < 12 * 60 else "PM"

    returned_time = f"{final_hours}:{final_minutes:02d} {period}"

    # Calcular el día de la semana si se da
    if starting_day:
        start_index = days_of_the_week.index(starting_day.lower())
        final_day = days_of_the_week[(start_index + extra_day) % 7].capitalize()
        returned_time += f", {final_day}"

    # Añadir info de días extra
    if extra_day == 1:
        returned_time += " (next day)"
    elif extra_day > 1:
        returned_time += f" ({extra_day} days later)"

    return returned_time



print(add_time('3:00 PM', '3:10'))