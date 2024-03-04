import cc_dat_utils 
from cc_classes import CCCoordinate,CCLevel,CCLevelPack, CCField, CCMapTitleField, CCEncodedPasswordField, CCMapHintField, CCMonsterMovementField
import json 

#Part 3
#Load your custom JSON file
input_json_file = "data/elugo_cc_level_pack(5).json"


#Convert JSON data to CCLevelPack

def convert_json_to_CCLevelPack(json_data):
    level_pack = CCLevelPack()

    level_number = 1
    levels_data = json_data['levels'] 
    for i, level_json in enumerate(levels_data):
        level = CCLevel() 
        level.level_number = 1 #level_json['level_num']
        level_number += i
        level.time = level_json['time']
        level.num_chips = level_json["numberOfChips"]
        password_str = level_json['password']
        password_list = [int(part) for part in password_str.split(',')]
        level.add_field(CCEncodedPasswordField(password_list))
        level.add_field(CCMapTitleField(level_json["title"]))
        level.add_field(CCMapHintField(level_json["hintText"]))
        level.upper_layer = level_json["upperLayer"]
    # level.upper_layer = upper_layer[2:10]
        level_pack.add_level(level)
    
    return level_pack


  
with open(input_json_file, "r") as reader:
    #load the JSON data and store it in the variable json_data
    json_data = json.load(reader)

#Save converted data to DAT file
if __name__ == "__main__":
    LevelPack = convert_json_to_CCLevelPack(json_data)
    cc_dat_utils.write_cc_level_pack_to_dat(LevelPack,'.\data\elugo_cc_level.dat')