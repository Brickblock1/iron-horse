from train import HopperCarOreConsist, FreightCar


def main():
    # --------------- pony NG ----------------------------------------------------------------------

    consist = HopperCarOreConsist(
        roster_id="pony",
        base_numeric_id=5920,
        gen=1,
        subtype="U",
        base_track_type="NG",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_ng_16px")

    consist = HopperCarOreConsist(
        roster_id="pony",
        base_numeric_id=5930,
        gen=3,
        subtype="U",
        base_track_type="NG",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_ng_16px")

    consist = HopperCarOreConsist(
        roster_id="pony",
        base_numeric_id=5940,
        gen=4,
        subtype="U",
        base_track_type="NG",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_ng_16px")

    # --------------- pony ----------------------------------------------------------------------

    # also just type A for gen 1, 2 and 3

    consist = HopperCarOreConsist(
        roster_id="pony",
        base_numeric_id=5700,
        gen=1,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_16px")

    # gen 1 also covers gen 2

    consist = HopperCarOreConsist(
        roster_id="pony",
        base_numeric_id=4110,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_16px")

    consist = HopperCarOreConsist(
        roster_id="pony",
        base_numeric_id=4390,
        gen=3,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_gapped_24px")

    consist = HopperCarOreConsist(
        roster_id="pony",
        base_numeric_id=4120,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_16px")

    consist = HopperCarOreConsist(
        roster_id="pony",
        base_numeric_id=4130,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_gapped_24px")

    consist = HopperCarOreConsist(
        roster_id="pony",
        base_numeric_id=4380,
        gen=5,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_filled_16px")

    consist = HopperCarOreConsist(
        roster_id="pony",
        base_numeric_id=4140,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_filled_greebled_24px")

    consist = HopperCarOreConsist(
        roster_id="pony",
        base_numeric_id=4150,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_filled_greebled_32px")

    consist = HopperCarOreConsist(
        roster_id="pony",
        base_numeric_id=4160,
        gen=6,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_filled_greebled_24px")

    consist = HopperCarOreConsist(
        roster_id="pony",
        base_numeric_id=4170,
        gen=6,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_filled_greebled_32px")
