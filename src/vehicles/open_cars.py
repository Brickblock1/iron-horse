import global_constants
from train import OpenConsist, FreightCar

def main():
    #--------------- pony ----------------------------------------------------------------------
    consist = OpenConsist(roster = 'pony',
                          base_numeric_id = 820,
                          vehicle_generation = 1)

    consist.add_unit(FreightCar(consist = consist,
                            capacity = 20,
                            vehicle_length = 4))

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = OpenConsist(roster = 'pony',
                          base_numeric_id = 830,
                          vehicle_generation = 2)

    consist.add_unit(FreightCar(consist = consist,
                            capacity = 35,
                            vehicle_length = 4))

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = OpenConsist(roster = 'pony',
                          base_numeric_id = 840,
                          vehicle_generation = 3)

    consist.add_unit(FreightCar(consist = consist,
                            capacity = 55,
                            vehicle_length = 6))

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = OpenConsist(roster = 'pony',
                          base_numeric_id = 1450,
                          vehicle_generation = 4)

    consist.add_unit(FreightCar(consist = consist,
                            capacity = 55,
                            vehicle_length = 8))

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = OpenConsist(roster = 'pony',
                          base_numeric_id = 850,
                          vehicle_generation = 1,
                          track_type = 'NG')

    consist.add_unit(FreightCar(consist = consist,
                           capacity = 12,
                           vehicle_length = 3))

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    #--------------- llama ----------------------------------------------------------------------
    consist = OpenConsist(roster = 'llama',
                          base_numeric_id = 860,
                          vehicle_generation = 1)

    consist.add_unit(FreightCar(consist = consist,
                            capacity = 25,
                            vehicle_length = 5))

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = OpenConsist(roster = 'llama',
                          base_numeric_id = 1330,
                          vehicle_generation = 2)

    consist.add_unit(FreightCar(consist = consist,
                            capacity = 45,
                            vehicle_length = 5))

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = OpenConsist(roster = 'llama',
                          base_numeric_id = 870,
                          vehicle_generation = 1,
                          track_type = 'NG')

    consist.add_unit(FreightCar(consist = consist,
                            capacity = 20,
                            vehicle_length = 5))

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = OpenConsist(roster = 'llama',
                          base_numeric_id = 1320,
                          vehicle_generation = 2,
                          track_type = 'NG')

    consist.add_unit(FreightCar(consist = consist,
                            capacity = 35,
                            vehicle_length = 5))

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    #--------------- antelope ----------------------------------------------------------------------
    consist = OpenConsist(roster = 'antelope',
                          base_numeric_id = 1760,
                          vehicle_generation = 1)

    consist.add_unit(FreightCar(consist = consist,
                            capacity = 55,
                            vehicle_length = 5))

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = OpenConsist(roster = 'antelope',
                          base_numeric_id = 1770,
                          vehicle_generation = 2)

    consist.add_unit(FreightCar(consist = consist,
                            capacity = 70,
                            vehicle_length = 8))

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = OpenConsist(roster = 'antelope',
                          base_numeric_id = 2090,
                          vehicle_generation = 1,
                          track_type = 'NG')

    consist.add_unit(FreightCar(consist = consist,
                            capacity = 20,
                            vehicle_length = 5))

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = OpenConsist(roster = 'antelope',
                          base_numeric_id = 1830,
                          vehicle_generation = 2,
                          track_type = 'NG')

    consist.add_unit(FreightCar(consist = consist,
                            capacity = 30,
                            vehicle_length = 6))

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = OpenConsist(roster = 'antelope',
                          base_numeric_id = 1820,
                          vehicle_generation = 3,
                          track_type = 'NG')

    consist.add_unit(FreightCar(consist = consist,
                            capacity = 40,
                            vehicle_length = 6))

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])
