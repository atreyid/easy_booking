import sys
class EasyBooking:
    def __init__(self):
        self.hotels = []
        self.users = []
        self.reviews = []


    def add_hotel(self):
        #adds new hotel information
        print("Enter new hotel information: ")
        hotel_id = len(self.hotels) + 1
        name = input("Enter name: ")
        price_per_night = int(input("Enter nightly price: "))
        is_available = True
        hotel = Hotel(hotel_id, name, price_per_night, is_available)
        self.hotels.append(hotel)
    

    def del_hotel(self):
        #deletes a hotel
        print("Deletes and existing hotel information")
        del_id = int(input("Enter hotel id to delete: "))
        for hotel in self.hotels:
            if hotel.hotel_id == del_id:
                self.hotels.remove(hotel)
        return len(self.hotels)
    
    
    def edit_hotel(self):
        #edits a pre-existing hotel information
        print("Edit a pre-existing hotel information")
        edit_id = int(input("Enter hotel id to edit"))
        for hotel in self.hotels:
            if hotel.hotel_id == edit_id:
                name = input("Enter name: ")
                price_per_night = int(input("Enter nightly price: "))
                is_available = True
                hotel.name = name
                hotel.price_per_night = price_per_night
                hotel.is_available = is_available
            
    def add_user(self):
        #Adds a new user to the database
        print("Enter new user information: ")
        user_id = len(self.users) + 1
        name = input("Enter user name: ")
        user = User(user_id, name)
        self.users.append(user)
            
    def pretty_print(self):
        #prints all hotel information
        for hotel in self.hotels:
            print("Hotel ID: ", hotel.hotel_id)
            print("Hotel Name: ", hotel.name)
            print("Price per night: ", hotel.price_per_night)
            print("Rating: ",hotel.rating)

    def add_review(self):
        #adds review for a hotel
        print("Enter hotel review here: ")
        user_id = int(input("Enter your user_id: "))
        hotel_id = int(input("Enter the hotel_id: "))
        rating = float(input("Enter your rating out of 5: "))
        text_review = input("Enter your text_review: ")
        review = Review(user_id,hotel_id,rating,text_review)
        self.reviews.append(review)
        hotel_ratings = []
        for hotel in self.hotels:
            if hotel.hotel_id == hotel_id:
                for review in self.reviews:
                    if review.hotel_id == hotel_id:
                        hotel_ratings.append(review.rating)
                hotel.update_review(hotel_ratings)

    def list_review(self):
        #lists reviews for a hotel
        print("Reviews for all hotels and all users are listed here: ")
        hotel_id = int(input("Enter hotel id you stayed at: "))
        for review in self.reviews:
            if review.hotel_id == hotel_id:
                for user in self.users:
                    if user.user_id == review.user_id:
                        reviewer_name = user.name
                for hotel in self.hotels:
                    if hotel.hotel_id == hotel_id:
                        hotel_name = hotel.name
                print("{} has given {} a rating of {} out of 5 and said {}".format(reviewer_name,hotel_name,review.rating,review.text_review))
            


            
class Hotel:
    def __init__(self,hotel_id,name,price_per_night,is_available,rating = -1):
        self.hotel_id = hotel_id
        self.name = name
        self.price_per_night = price_per_night
        self.is_available = is_available
        self.rating = rating

    def update_review(self, ratings):
        # ratings -> List[int]
        self.rating = sum(ratings)/len(ratings)


class User:
    def __init__(self,user_id,name):
        self.user_id = user_id
        self.name = name

class Review:
    def __init__(self,user_id,hotel_id,rating,text_review):
        self.user_id = user_id
        self.hotel_id = hotel_id
        self.rating = rating
        self.text_review = text_review
    
def show_menu():
    print('''
    Type 1: Add a new hotel information
    Type 2: Edit a existing hotel information
    Type 3: Add a new user
    Type 4: Review a hotel
    Type 5: See all hotel information and rating
    Type 6: See all reviews for a particular hotel
    Type 0: Quit program''')

    choice = int(input("Enter your choice: "))
    if choice == 1:
        easy_booking.add_hotel()
        show_menu()
    if choice == 2:
        easy_booking.edit_hotel()
        show_menu()
    if choice == 3:
        easy_booking.add_user()
        show_menu()
    if choice == 4:
        easy_booking.add_review()
        show_menu()
    if choice == 5:
        easy_booking.pretty_print()
        show_menu()
    if choice == 6:
        easy_booking.list_review()
        show_menu()
    if choice == 0:
        exit()

if __name__ == "__main__":
    easy_booking = EasyBooking()
    show_menu()


