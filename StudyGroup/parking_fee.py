total_cars = 4
parking_fee = [0] * total_cars
parking_time = [0] * total_cars
cars_start = [0] * total_cars
cars_end = [0] * total_cars
cars_timepoint = []
cars_count = 0
period_start = 0
period_end = 0
result = 0

input_string_fee = input(f"enter fee ({total_cars} numbers): ")
for i in range(total_cars):
    parking_fee[i] = int(input_string_fee.split()[i])

for i in range(total_cars):
    input_string_car = input(f"enter arrival and leaving time for car #{i+1}: ")
    cars_start[i] = int(input_string_car.split()[0])
    cars_end[i] = int(input_string_car.split()[1])
cars_timepoint = cars_start + cars_end

while bool(cars_timepoint):
    period_start = period_end
    period_end = min(cars_timepoint)
    cars_timepoint.remove(period_end)
    if cars_count == 0:  # 원래 한대도 없었을 때, period_end in cars_start == True 일 수 밖에 없음
        cars_count += 1
        cars_start.remove(period_end)
    elif period_end in cars_start:  # 차 추가
        parking_time[cars_count - 1] += period_end - period_start
        cars_count += 1
        cars_start.remove(period_end)
    else:  # 차 뺌, period_end in cars_end
        parking_time[cars_count - 1] += period_end - period_start
        cars_count -= 1
        cars_end.remove(period_end)

print(parking_time)

for i in range(total_cars):
    result += parking_fee[i] * parking_time[i] * (i+1)
    # print(result)

print(f"fee is {result}")
