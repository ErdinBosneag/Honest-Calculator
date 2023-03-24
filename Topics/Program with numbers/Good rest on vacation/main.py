# put your python code here
duration_in_days = int(input())
food_cost = int(input())
flight_cost = int(input())
hotel_cost = int(input())
print((duration_in_days - 1) * hotel_cost + duration_in_days * food_cost + 2 * flight_cost)