import cc_dat_utils 
from cc_classes import CCCoordinate,CCLevel,CCLevelPack, CCField, CCMapTitleField, CCEncodedPasswordField, CCMapHintField, CCMonsterMovementField
import json 

#Part 3
#Load your custom JSON file
input_json_file = "data/elugo_cc1.json"


#Convert JSON data to CCLevelPack

def convert_json_to_CCLevelPack(json_data):
    level_pack = CCLevelPack()

    levels_data = json_data['Levels'] 
    level = CCLevel()
    level.level_number = levels_data['level_num']
    level.time = levels_data['time']
    level.num_chips = levels_data["chip number"]
    fields = levels_data["fields"]
    for field_name, field_value in fields.items():
        if field_name == "field 3":
            level.add_field(CCMapTitleField(field_value))
        elif field_name == "field 6":
            level.add_field(CCEncodedPasswordField(field_value))
        elif field_name == "field 7":
            level.add_field(CCMapHintField(field_value))
        elif field_name == "field 10":
            monster_coordinates = [CCCoordinate(field_value[0],field_value[1])]
            level.add_field(CCMonsterMovementField(monster_coordinates))
    upper_layer = json_data["upper layer"]
    level.upper_layer = upper_layer[:1024]
    level_pack.add_level(level)
    
    return level_pack


  
with open(input_json_file, "r") as reader:
    #load the JSON data and store it in the variable json_data
    json_data = json.load(reader)

#Save converted data to DAT file
if __name__ == "__main__":
    LevelPack = convert_json_to_CCLevelPack(json_data)
    cc_dat_utils.write_cc_level_pack_to_dat(LevelPack,'.\data\elugo_cc1.dat')