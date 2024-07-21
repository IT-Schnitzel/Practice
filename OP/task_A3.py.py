def bus(stops):
    passenger_count = 0
    
    for stop in stops:
        passenger_count += stop[0]  # Пассажиры, зашедшие на текущей остановке
        passenger_count -= stop[1]  # Пассажиры, вышедшие на текущей остановке
    
    return passenger_count
