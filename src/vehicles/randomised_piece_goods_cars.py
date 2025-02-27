from train import PieceGoodsCarRandomisedConsist, FreightCar


def main():
    # --------------- pony ----------------------------------------------------------------------

    consist = PieceGoodsCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=8040,
        gen=1,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_16px")

    # no new type A for gen 2, gen 1 type A continues

    consist = PieceGoodsCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=8050,
        gen=2,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_24px")

    consist = PieceGoodsCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=8060,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_16px")

    consist = PieceGoodsCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=8070,
        gen=3,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_24px")

    consist = PieceGoodsCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=8080,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_16px")

    consist = PieceGoodsCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=8090,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_24px")

    consist = PieceGoodsCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=8140,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_32px")

    consist = PieceGoodsCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=8100,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_24px")

    consist = PieceGoodsCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=8110,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_32px")

    consist = PieceGoodsCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=8120,
        gen=6,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_24px")

    consist = PieceGoodsCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=8130,
        gen=6,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_32px")
