from train import EngineConsist, SteamEngineUnit, SteamEngineTenderUnit

consist = EngineConsist(id='super_mountain',
                        base_numeric_id=510,
                        title='4-8-4 Super Mountain [Steam]',
                        power=2100,
                        speed=75,
                        intro_date=1935)

consist.add_unit(type=SteamEngineUnit,
                 weight=110,
                 vehicle_length=8,
                 spriterow_num=0)

consist.add_unit(type=SteamEngineTenderUnit,
                 weight=60,
                 vehicle_length=6,
                 spriterow_num=1)

consist.add_model_variant(spritesheet_suffix=0)
