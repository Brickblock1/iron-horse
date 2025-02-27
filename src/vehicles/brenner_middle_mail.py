from train import TGVMiddleMailEngineConsist, ElectricHighSpeedMailUnit


def main(roster_id):
    consist = TGVMiddleMailEngineConsist(
        roster_id=roster_id,
        id="brenner_middle_mail",
        base_numeric_id=6780,
        name="Brenner Mail Van",
        role="very_high_speed",
        role_child_branch_num=3,
        pantograph_type="z-shaped-single-with-base",
        power=0,  # set power 0, when attached to correct cab, cab power will be increased
        gen=6,
        intro_date_offset=-3,  # introduce earlier than gen epoch by design
        sprites_complete=True,
    )

    consist.add_unit(
        type=ElectricHighSpeedMailUnit,
        weight=52,
        spriterow_num=0,
        chassis="jacobs_solid_express_32px",
        repeat=2,
    )

    consist.description = """And you shall know this velocity."""
    consist.foamer_facts = """Alstom Class 390 <i>Pendolino</i>"""

    return consist
