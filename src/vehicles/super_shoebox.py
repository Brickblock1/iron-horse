from train import EngineConsist, ElectroDieselEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="super_shoebox",
        base_numeric_id=880,
        name="Super Shoebox",
        role="express",
        role_child_branch_num=-1,
        power=1250,
        power_by_railtype={"RAIL": 1250, "ELRL": 2600},
        random_reverse=True,
        pantograph_type="z-shaped-single",
        gen=5,
        sprites_complete=True,
        # alternative_cc_livery="RAILFREIGHT_TRIPLE_GREY", # unfinished alt liveries, could be triple grey, or block colour?
        default_livery_extra_docs_examples=[
            ("COLOUR_PINK", "COLOUR_WHITE"),
            ("COLOUR_LIGHT_BLUE", "COLOUR_WHITE"),
            ("COLOUR_CREAM", "COLOUR_GREY"),
            ("COLOUR_ORANGE", "COLOUR_BROWN"),
        ],
    )

    consist.add_unit(
        type=ElectroDieselEngineUnit,
        weight=82,
        vehicle_length=8,
        effect_offsets=[(2, 0)],
        spriterow_num=0,
    )

    consist.description = """It's a bigger Shoebox. Well not bigger. But more power in it. Right new paint too."""
    consist.foamer_facts = """BR Class 73, Class 71/74, proposed Class 75"""

    return consist
