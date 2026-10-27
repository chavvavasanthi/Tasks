# 2 The Captain's Room
# https://www.hackerrank.com/challenges/py-the-captains-room/problem

K = int(input())
room_numbers = list(map(int, input().split()))

unique_rooms = set(room_numbers)

captain_room = (sum(unique_rooms) * K - sum(room_numbers)) // (K - 1)

print(captain_room)
