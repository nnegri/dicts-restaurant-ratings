def sort_ratings(restaurant_file):
    with open(restaurant_file) as restaurant_ratings:

        alpha_ratings = {}

        for line in restaurant_ratings:
            data = line.rstrip().split(":")
            restaurant_name = data[0]
            restaurant_rating = data[1]

            alpha_ratings[restaurant_name] = restaurant_rating


        while True:
            user_response = raw_input("Would you like to See the ratings, Enter your own, or Quit? ")

            if user_response == "E":

                new_restaurant = raw_input("What is the name of the restaurant that are rating?: ")
                alpha_ratings[new_restaurant] = int(raw_input ("What rating would you give this restaurant?: "))

            elif user_response == "S":
                alpha_ratings = sorted(alpha_ratings.items())        

                for restaurant_info in alpha_ratings:
                    print "%s is rated at %d." % (restaurant_info[0], int(restaurant_info[1]))

            elif user_response == "Q":
                break

sort_ratings("scores.txt")