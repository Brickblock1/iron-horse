from train import EngineConsist, SteamEngineUnit, SteamEngineTenderUnit

consist = EngineConsist(id='cooke',
                        base_numeric_id=150,
                        title='4-6-0 Cooke [Steam]',
                        power=1500,
                        speed=65,
                        intro_date=1885)

consist.add_unit(type=SteamEngineUnit,
                 weight=75,
                 vehicle_length=6,
                 spriterow_num=0)

consist.add_unit(type=SteamEngineTenderUnit,
                 weight=40,
                 vehicle_length=5,
                 spriterow_num=1)

consist.add_model_variant(spritesheet_suffix=0)
