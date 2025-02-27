from train import EngineConsist, ElectricEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="fury",
        base_numeric_id=2180,
        name="Fury",
        role="super_heavy_express",
        role_child_branch_num=1,
        power=3600,
        random_reverse=True,
        gen=5,
        pantograph_type="z-shaped-double",
        intro_date_offset=1,  # introduce later than gen epoch by design
        alternative_cc_livery="FREIGHTLINER_GBRF",
        force_default_pax_mail_livery=2,  # pax/mail cars default to second livery with this engine
        default_livery_extra_docs_examples=[
            ("COLOUR_GREEN", "COLOUR_YELLOW"),
            ("COLOUR_PALE_GREEN", "COLOUR_PALE_GREEN"),
            ("COLOUR_PALE_GREEN", "COLOUR_YELLOW"),
            ("COLOUR_LIGHT_BLUE", "COLOUR_WHITE"),
        ],
        sprites_complete=True,
    )

    consist.add_unit(
        type=ElectricEngineUnit, weight=82, vehicle_length=8, spriterow_num=0
    )

    consist.description = (
        """Rebuilt the Roarers. Very sound these are, last a long time they will."""
    )
    consist.foamer_facts = """BR Class 86"""

    return consist
