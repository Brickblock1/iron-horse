from train import EngineConsist, DieselEngineUnit


def main(roster_id):
    consist = EngineConsist(roster_id=roster_id,
                            id='tug',
                            base_numeric_id=5070,
                            name='Tug',
                            role='heavy_freight',
                            role_child_branch_num=-2, # Joker eh
                            power=4450, # 850hp steps Revolution -> Endeavor -> Toaster
                            # dibble for game balance, assume super-slip control
                            tractive_effort_coefficient=0.4,
                            random_reverse=True,
                            intro_date_offset=3,  # let's be a little bit later for this one
                            gen=5,
                            fixed_run_cost_points=210, # unrealism: run cost nerf for being so high-powered
                            alternative_cc_livery='RAILFREIGHT_TRIPLE_GREY',
                            sprites_complete=False)

    consist.add_unit(type=DieselEngineUnit,
                     weight=125,
                     vehicle_length=8,
                     effect_offsets=[(1, 0)],
                     spriterow_num=0)

    consist.description = """"""
    consist.foamer_facts = """"""

    return consist
