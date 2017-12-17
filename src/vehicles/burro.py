from train import EngineConsist, SteamEngineUnit

consist = EngineConsist(id='burro',
                        base_numeric_id=90,
                        title='0-4-2 Burro [Steam]',
                        power=650,
                        speed=55,
                        type_base_buy_cost_points=-10,  # dibble buy cost for game balance
                        type_base_running_cost_points=-15,  # dibble running costs for game balance
                        intro_date=1850)

consist.add_unit(type=SteamEngineUnit,
                 weight=40,
                 vehicle_length=6,
                 spriterow_num=0)

consist.add_model_variant(spritesheet_suffix=0)
