from train import EngineConsist, SteamEngineUnit, SteamEngineTenderUnit

consist = EngineConsist(id='bush_elephant',
                        base_numeric_id=2000,
                        title='2-6-6-2 Bush Elephant [Steam]',
                        power=2200,
                        track_type='NG',
                        speed=45,
                        type_base_buy_cost_points=35,  # dibble buy cost for game balance
                        type_base_running_cost_points=35,  # dibble running costs for game balance
                        intro_date=1915)

consist.add_unit(type=SteamEngineUnit,
                 weight=128,
                 vehicle_length=8,
                 spriterow_num=0)

consist.add_unit(type=SteamEngineTenderUnit,
                 weight=52,
                 vehicle_length=4,
                 spriterow_num=1)

consist.add_model_variant(spritesheet_suffix=0)
