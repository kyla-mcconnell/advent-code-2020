import math 

file = "data/input5.txt"

#Challenge 1: Given a series of letters referring to halves of the data, return the largest seat number
def seat_finder(filename):
    with open(filename, "r") as f:
        all_seats = []
        for row in f:
            row_min = 0
            row_max = 127
            col_min = 0
            col_max = 7
            for letter in row: 
                if letter == "F":
                    row_max = row_max - math.ceil((row_max - row_min)/2)
                elif letter == "B":
                    row_min = row_min + math.ceil((row_max - row_min)/2)
                elif letter == "R":
                    col_min = col_min + math.ceil((col_max - col_min)/2)
                elif letter == "L":
                    col_max = col_max - math.ceil((col_max - col_min)/2)

            if row_min == row_max and col_min == col_max:
                all_seats.append(row_min * 8 + col_min)
            else:
                print("ERROR")
        return all_seats
        
print(f'The highest seat ID is {max(seat_finder(file))}.')

#Challenge 2: Find the seat which is missing from the sequence, where ID + 1 and ID - 1 is present

def lost_seater(file):
    all_seats = set(seat_finder(file))
    possible_seats = set(range(min(all_seats), max(all_seats)))
    leftover_seats = all_seats.symmetric_difference(possible_seats)
    for seat in leftover_seats:
        if seat not in all_seats and seat + 1 in all_seats and seat - 1 in all_seats:
            your_seat = seat
    return your_seat
    
print(f'Your seat ID is {(lost_seater(file))}.')