import global_constants
from train import CoveredHopperConsist, FreightCar

def main():
    #--------------- pony ----------------------------------------------------------------------
    consist = CoveredHopperConsist(roster = 'pony',
                                   base_numeric_id = 1270,
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


    consist = CoveredHopperConsist(roster = 'pony',
                                   base_numeric_id = 1230,
                                   vehicle_generation = 2)

    consist.add_unit(FreightCar(consist = consist,
                           capacity = 40,
                           vehicle_length = 6))

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = CoveredHopperConsist(roster = 'pony',
                                   base_numeric_id = 1240,
                                   vehicle_generation = 3)

    consist.add_unit(FreightCar(consist = consist,
                           capacity = 60,
                           vehicle_length = 8))

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    #--------------- llama ----------------------------------------------------------------------
    consist = CoveredHopperConsist(roster = 'llama',
                                   base_numeric_id = 1250,
                                   vehicle_generation = 2)

    consist.add_unit(FreightCar(consist = consist,
                            capacity = 40,
                            vehicle_length = 7))

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = CoveredHopperConsist(roster = 'llama',
                                   base_numeric_id = 1260,
                                   vehicle_generation = 3)

    consist.add_unit(FreightCar(consist = consist,
                           capacity = 65,
                           vehicle_length = 8))

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])

