with open('input.txt', 'rt') as f:
    input_data = f.readlines()

seat_ids = []
for seat in input_data:
    row = int(seat[0:7].strip().replace('F', '0').replace('B', '1'), 2)
    col = int(seat[-4:].strip().replace('L', '0').replace('R', '1'), 2)
    seat_id = (row * 8) + col
    seat_ids.append((seat.strip(), row, col, seat_id))

print("Highest seat ID:", max([x[3] for x in seat_ids]))
