from train import TGVMiddlePassengerEngineConsist, ElectricHighSpeedPaxUnit


def main(roster_id):
    consist = TGVMiddlePassengerEngineConsist(
        roster_id=roster_id,
        id="helm_wind_middle_passenger",
        base_numeric_id=2890,
        name="Helm Wind Passenger Coach",
        role="very_high_speed",
        role_child_branch_num=2,
        power=0,  # set power 0, when attached to correct cab, cab power will be increased
        # no pantographs for Helm Wind middle cars
        gen=5,
        intro_date_offset=-3,  # introduce earlier than gen epoch by design
        sprites_complete=True,
    )

    consist.add_unit(
        type=ElectricHighSpeedPaxUnit,
        weight=42,
        spriterow_num=0,
        chassis="4_axle_solid_express_32px",
        repeat=2,
    )

    consist.description = """Can we get there faster? That's what drives me."""
    consist.foamer_facts = (
        """BR InterCity 225 (Mk4 Coaches)), Shinkansen-style distributed traction"""
    )

    return consist
