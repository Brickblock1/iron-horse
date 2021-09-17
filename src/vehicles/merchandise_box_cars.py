from train import BoxCarMerchandiseConsist, FreightCar


def main():
    # --------------- pony NG ----------------------------------------------------------------------
    consist = BoxCarMerchandiseConsist(
        roster_id="pony",
        base_numeric_id=6130,
        gen=1,
        subtype="U",
        base_track_type="NG",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_ng_16px")

    # no gen 2 for NG, straight to gen 3

    consist = BoxCarMerchandiseConsist(
        roster_id="pony",
        base_numeric_id=6140,
        gen=3,
        subtype="U",
        base_track_type="NG",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_ng_16px")

    consist = BoxCarMerchandiseConsist(
        roster_id="pony",
        base_numeric_id=6150,
        gen=4,
        subtype="U",
        base_track_type="NG",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_ng_16px")

    # --------------- pony ----------------------------------------------------------------------

    # only type A for gen 1

    consist = BoxCarMerchandiseConsist(
        roster_id="pony",
        base_numeric_id=6160,
        gen=1,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_filled_16px")

    # no new type A for gen 2, gen 1 type A continues

    consist = BoxCarMerchandiseConsist(
        roster_id="pony", base_numeric_id=6170, gen=2, subtype="B", sprites_complete=True
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_gapped_24px")

    consist = BoxCarMerchandiseConsist(
        roster_id="pony", base_numeric_id=6180, gen=3, subtype="A", sprites_complete=True
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_filled_16px")

    consist = BoxCarMerchandiseConsist(
        roster_id="pony",
        base_numeric_id=6190,
        gen=3,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_filled_24px")

    consist = BoxCarMerchandiseConsist(
        roster_id="pony", base_numeric_id=6200, gen=4, subtype="A", sprites_complete=True
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_filled_16px")

    consist = BoxCarMerchandiseConsist(
        roster_id="pony",
        base_numeric_id=6210,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_filled_24px")

    consist = BoxCarMerchandiseConsist(
        roster_id="pony",
        base_numeric_id=6220,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(
        type=FreightCar,
        suppress_roof_sprite=True,  # non-standard roof for this wagon
        chassis="4_axle_1cc_filled_32px",
    )

    consist = BoxCarMerchandiseConsist(
        roster_id="pony",
        base_numeric_id=6230,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_filled_greebled_24px")

    consist = BoxCarMerchandiseConsist(
        roster_id="pony",
        base_numeric_id=6240,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_1cc_filled_32px")

    consist = BoxCarMerchandiseConsist(
        roster_id="pony",
        base_numeric_id=6250,
        gen=6,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_filled_greebled_24px")

    consist = BoxCarMerchandiseConsist(
        roster_id="pony",
        base_numeric_id=6260,
        gen=6,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_1cc_filled_32px")
