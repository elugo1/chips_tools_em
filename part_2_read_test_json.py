import test_data
import json



#Creates and returns a GameLibrary object(defined in test_data) from loaded json_data
def make_game_library_from_json( json_data ):
    #Initialize a new GameLibrary
    game_library = test_data.GameLibrary()

    ### Begin Add Code Here ###
    for game_value, game_value in json_data.items():
        #Create a new Game object from the json_data by reading
        title = game_value["title"]
        year = game_value["year"]

        platform_data = game_value["platform"]
        name = platform_data["name"]
        launch_year = platform_data["launch year"]  
        
        #  platform (which requires reading name and launch_year)
        platform = test_data.Platform(name,launch_year)
        game_object = test_data.Game(title,platform,year)
        #Add that Game object to the game_library
        game_library.add_game(game_object)
    ### End Add Code Here ### 
    return game_library


#Part 2
input_json_file = "data/test_data.json"
 
### Begin Add Code Here ###
with open(input_json_file, "r") as reader:
    #load the JSON data and store it in the variable game_json_data
    json_data = json.load(reader)
    #Use the json module to load the data from the file
    game_lib_data = make_game_library_from_json(json_data)
print(game_lib_data)
### End Add Code Here ###
