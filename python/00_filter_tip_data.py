# -*- coding: utf-8 -*-
"""
Filter Yelp tip data

@author: MariaAthena
"""

import pandas as pd
import json
import feather


# Read tip data file into a python array
with open('../data/yelp_academic_dataset_tip.json', 'rb') as f:
	tip_data = f.readlines()

# Read business data file into a python array
with open('../data/yelp_academic_dataset_tip.json', 'rb') as f:
	bus_data = f.readlines()


# remove the trailing "\n" from each line
tip_data = map(lambda x: x.rstrip(), bus_data)
bus_data = map(lambda x: x.rstrip(), bus_data)
# put individual business JSON objects into list
tip_json = "[" + ','.join(bus_data) + "]"
bus_json = "[" + ','.join(bus_data) + "]"


# List of all food and drinks categories in data set
food_drink = ['Afghan', 'Creperies', 'Canadian (New)', 'Szechan', 
				'Restarants', 'Cantonese', 'Crry Sasage', 'Chicken Wings',
				'Food Stands', 'Eastern Eropean', 'Persian/Iranian', 
				'Cajun', 'Creole', 'Scandinavian', 'Greek', 'Pretzels', 
				'Chinese', 'Food Trcks', 'Middle Eastern', 'Macarons', 
				'Brazilian', 'Shanghainese', 'Empanadas', 'Hngarian', 'Diners',
				'Russian', 'Vegetarian', 'Chicken Shop', 'Kosher', 
				'Jice Bars & Smoothies', 'Pita', 'German', 'Taiwanese', 
				'Haitian', 'Laotian', 'Basqe', 'Vietnamese', 'Astralian',
				'Pizza', 'Venezelan', 'Wine Tasting Room', 'Falafel', 'Food Cort',
				'Beer Garden', 'Seafood', 'British', 'Beer Gardens', 'Japanese', 
				'Pb Food', 'Hot Dogs', 'Salvadoran', 'Sandwiches', 'Swiss Food',
				'Dim Sm', 'Armenian', 'Patisserie', 'Cake', 'Cocktail Bars', 
				'Dive Bars', 'Scottish', 'Wok', 'Distilleries', 'Coffee & Tea', 
				'Cheesesteaks', 'Tapas Bars', 'Cban', 'Brgers', 'Bavarian', 
				'Tex-Mex', 'Cpcakes', 'Food Tors', 'Barbeqe', 
				'American (Traditional)', 'Wine Tasting Classes', 'Delicatessen', 
				'Egyptian', 'Food', 'Moroccan', 'Convenience Stores', 
				'Comfort Food', 'Portgese', 'Chocolatiers & Shops', 'Cheese Shops',
				'Cafeteria', 'Glten-Free', 'Tea Rooms', 'French', 'Slovakian',
				'Fonde', 'Irish', 'Food Delivery Services', 'Italian', 
				'Mediterranean', 'Astrian', 'Internet Cafes', 'Personal Chefs', 
				'Irish Pb', 'Caribbean', 'American (New)', 'Caterers', 
				'Breakfast & Brnch', 'Do-It-Yorself Food', 'Indonesian', 
				'Hawaiian', 'Argentine', 'Thai', 'Sri Lankan', 'Fish & Chips', 
				'Food Banks', 'Brmese', 'Beer Bar', 'Singaporean', 'Asian Fsion', 
				'Ethiopian', 'Trkish', 'African', 'Live/Raw Food', 'Bangladeshi',
				'Gay Bars', 'Sothern', 'Cooking Schools', 'Rhinelandian', 
				'Champagne Bars', 'Pawn Shops', 'Candy Stores', 'Kebab', 
				'Wine Tors', 'Wine Bars', 'Donts', 'Bagels', 'Dominican', 
				'Beer, Wine & Spirits', 'Himalayan/Nepalese', 'Local Flavor', 
				'Lebanese', 'Sop', 'Coffeeshops', 'Pervian', 'krainian', 
				'Tapas/Small Plates', 'Arabian', 'Belgian', 'Pasta Shops', 
				'Salad', 'Ethnic Grocery', 'Steakhoses', 'Gelato', 'Desserts', 
				'Perto Rican', 'Polish', 'Frits & Veggies', 'International', 
				'Beer Hall', 'Bbble Tea', 'Cafes', 'Wineries', 
				'Ice Cream & Frozen Yogrt', 'Bars', 'Pop-p Shops', 'Korean', 
				'Pakistani', 'Vegan', 'Gastropbs', 'Popcorn Shops', 'Bakeries', 
				'Breweries', 'Malaysian', 'Modern Eropean', 'Potineries', 'Czech',
				'Ramen', 'Fast Food', 'Colombian', 'Serbo Croatian', 'Cambodian',
				'Hot Pot', 'Mexican', 'Meat Shops', 'Specialty Food', 'Spanish']

food_drink = [unicode(word) for word in food_drink]


# Helper function to determine if business sells food or drink
def is_food_drink(business_categories):
    is_food_drink = 0
    
    if len(set(business_categories).intersection(food_drink)) != 0:
        is_food_drink = int('1')
    else:
        pass
        
    return is_food_drink


# Create column signifying data is 
bus_df['food_drink'] = bus_df.categories.apply(lambda x: is_food_drink(x))
bus_df = bus_df[['business_id', 'latitude', 'longitude', 'name', 
'city', 'stars', 'review_count', 'food_drink']]

# Join business info onto tip data frame
output_df = pd.merge(tip_df, 
	bus_df, 
	left_on='business_id',
	right_on='business_id', 
	how='left')

# Filter taking only data point from food_drink selling businesses
output_df = output_df[output_df.food_drink > 0]
# Only keep data from three cities that are to be analysed
output_df  = output_df[(
	output_df.city == 'Montreal') | (
	output_df.city == 'Pittsburgh') | (
	output_df.city == 'Edinburgh')]

feather.write_dataframe(output_df, '../parsed_data/filtered_tip_data.feather')
