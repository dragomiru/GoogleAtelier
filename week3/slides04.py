# Memory savers

"""lambda  = not recommended"""
# my_lambda = lambda x, y: x + y
# my_sum = my_lambda(2, 4)
# print('my_sum = ', my_sum)

"""lambda recommended"""
players = [{
    "first_name": "John",
    "last_name": "Doe",
    "rank": 3
}, {
    "first_name": "Kevin",
    "last_name": "McDonald",
    "rank": 1
}]

sorted_players = sorted(players, key=lambda player: player["rank"])
# print(sorted_players)

"""map"""
# import copy
# def check_top_3_player(player):
#     updated_player = copy.deepcopy(player)
#     updated_player["is_top_3"] = True if updated_player["rank"] <= 3 else False
#     return updated_player
#
# players_with_top_3_value = map(check_top_3_player, players)
# print("players_with_top_3_value = ", list(players_with_top_3_value))

"""filter"""
# all_mcdonalds = filter(lambda player: True if player["last_name"] == "McDonald" else False, players)
# print("all_mcdonalds = ", list(all_mcdonalds))

"""zip"""
# list_1 = [1, 2, 3]
# list_2 = [10, 20, 30]
# list_3 = [100, 200, 300]
# for zip_item in zip(list_1, list_2, list_3):
#     list_1_element, list_2_element, list_3_element = zip_item
#     print(list_1_element, list_2_element, list_3_element)

"""list comprehension"""
# my_numbers = [1, 2, 3, 4, 5]
# squared_numbers = [item ** 2 for item in my_numbers]
# even_squared_numbers = [item ** 2 for item in my_numbers if item % 2 == 0]
# print(squared_numbers)
# print(even_squared_numbers)

