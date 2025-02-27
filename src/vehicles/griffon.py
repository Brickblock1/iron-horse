from train import EngineConsist, DieselEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="griffon",
        base_numeric_id=2840,
        name="Griffon",  # Griffon and Shredder names are wrong way round, but seems to suit the shapes so eh, leave it :)
        role="branch_express",
        role_child_branch_num=1,
        power=1650,
        random_reverse=True,
        fixed_run_cost_points=100,  # give a bonus so this can be a genuine mixed-traffic engine
        gen=5,  # not replaced by anything (?)
        force_caboose_families={"caboose_car": "pony_railfreight_2"},
        alternative_cc_livery="RAILFREIGHT_TRIPLE_GREY",
        default_livery_extra_docs_examples=[
            ("COLOUR_GREY", "COLOUR_YELLOW"),
            ("COLOUR_WHITE", "COLOUR_GREY"),
            ("COLOUR_GREY", "COLOUR_GREY"),
            ("COLOUR_LIGHT_BLUE", "COLOUR_WHITE"),
        ],
        sprites_complete=True,
    )

    consist.add_unit(
        type=DieselEngineUnit, weight=74, vehicle_length=6, spriterow_num=0
    )

    consist.description = """Kelpie were right good, this is the rebuilt version."""
    consist.foamer_facts = """BR Class 33"""

    return consist
