import global_constants

from roster import Roster

from vehicles import snowplough_moose_gen_2


def main(disabled=False):
    roster = Roster(
        id="moose",
        numeric_id=3,
        # ELRL, ELNG is mapped to RAIL, NG etc
        # default intro dates per generation, can be over-ridden if needed by setting intro_date kw on consist
        intro_dates={
            "RAIL": [1860, 1900, 1930, 1960, 1990, 2020],
            "METRO": [1900, 1950, 2000],
            "NG": [1860, 1905, 1950, 2000],
        },
        # default speeds per generation, can be over-ridden if needed by setting speed kw arg on consist
        # speeds roughly same as RH trucks of same era + 5mph or so, and a bit higher at the top end (back and forth on this many times eh?),
        # NG is Corsican-style 1000mm, native brit NG is not a thing for gameplay
        speeds={
            "RAIL": {
                # gen 5 and 6 held down by design, really fast freight is imbalanced
                "standard": [
                    45,
                    45,
                    60,
                    75,
                    87,
                    87,
                ],
                # match standard, except gen 6
                "suburban": [45, 45, 60, 75, 87, 99],
                # smaller steps in gen 5 and 6, balances against faster HSTs
                "express": [
                    60,
                    75,
                    90,
                    105,
                    115,
                    125,
                ],
                "hst": [0, 0, 0, 112, 125, 125],
                "hst_on_lgv": [0, 0, 0, 112, 125, 140],
                "very_high_speed": [0, 0, 0, 0, 125, 125],
                "very_high_speed_on_lgv": [0, 0, 0, 0, 140, 186],
            },
            "METRO": {
                "standard": [45, 55, 65]
                # only standard for metro in Pony
            },
            "NG": {
                "standard": [
                    45,
                    45,
                    55,
                    65,
                ],
                # NG standard/suburban/express same in Pony, balanced against trams, RVs
                # suburban has to be provided as the mail railcar expects it, just copying it in is easiest solution
                "suburban": [45, 45, 55, 65],
                # suburban has to be provided as the coaches/mail vans etc expect it, just copying it in is easiest solution
                "express": [45, 45, 55, 65],
            },
        },
        # capacity factor per generation, will be multiplied by vehicle length
        freight_car_capacity_per_unit_length={
            "RAIL": [4, 4, 5, 5.5, 6, 6.5],
            "NG": [3, 3, 4, 4],
        },
        pax_car_capacity_per_unit_length={
            "RAIL": [3, 3.75, 4.5, 5.25, 6, 6],
            "NG": [3, 5, 5, 6],
        },
        pax_car_capacity_types={
            "default": {
                "multiplier": 1,
                "loading_speed_multiplier": 1,
            },
            "high_capacity": {
                "multiplier": 1.5,
                "loading_speed_multiplier": 1.75,
            },
            # very specifically tuned multiplier against a single pony vehicle
            "autocoach_combine": {
                "multiplier": 2.7,
                "loading_speed_multiplier": 1.75,
            },
            "restaurant": {
                "multiplier": 0.45,
                "loading_speed_multiplier": 1,
            },
        },
        # freight car weight factor varies slightly by gen, reflecting modern cars with lighter weight
        train_car_weight_factors=[0.5, 0.5, 0.5, 0.48, 0.44, 0.40],
        # caboose families (family names and caboose names are arbitrary strings)
        # caboose names map to labelled spriterows, as defined in the vehicle files
        caboose_families={
            "RAIL": {
                "caboose_car": {
                    "pony_caboose_car_default_1": ["caboose_1"],
                    "pony_caboose_car_default_2": ["caboose_2"],
                    "pony_caboose_car_default_3": ["caboose_3"],
                    "pony_caboose_car_default_4": ["caboose_4"],
                    "pony_caboose_car_default_5": ["caboose_5"],
                    "pony_caboose_car_default_6": ["caboose_6"],
                    "pony_gwr_1": ["caboose_1"],
                    #"pony_gwr_1": ["caboose_1", "gwr_1"],
                    "pony_railfreight_1": ["railfreight_1", "brown_1"],
                    "pony_railfreight_2": ["caboose_6"],
                    #"pony_railfreight_2": ["railfreight_2"],
                },
                "goods_caboose_car": {
                    "pony_goods_caboose_car_default_1": ["caboose_1"],
                    "pony_goods_caboose_car_default_2": ["caboose_2"],
                    "pony_goods_caboose_car_default_3": ["caboose_3"],
                    "pony_goods_caboose_car_default_4": ["caboose_4"],
                    "pony_goods_caboose_car_default_5": ["caboose_5"],
                    "pony_goods_caboose_car_default_6": ["caboose_6"],
                    "pony_railfreight_1": ["railfreight_1", "brown_1"],
                },
            },
            "NG": {
                "caboose_car": {
                    "pony_ng_caboose_car_1": ["ng_caboose_1"],
                    "pony_ng_caboose_car_2": ["ng_caboose_2"],
                    "pony_ng_caboose_car_3": ["ng_caboose_3"],
                },
            },
        },
        # lists of one default family name per generation, ascending
        caboose_default_family_by_generation={
            "RAIL": [
                {
                    "caboose_car": "pony_caboose_car_default_1",
                    "goods_caboose_car": "pony_goods_caboose_car_default_1",
                },
                {
                    "caboose_car": "pony_caboose_car_default_2",
                    "goods_caboose_car": "pony_goods_caboose_car_default_2",
                },
                {
                    "caboose_car": "pony_caboose_car_default_3",
                    "goods_caboose_car": "pony_goods_caboose_car_default_3",
                },
                {
                    "caboose_car": "pony_caboose_car_default_4",
                    "goods_caboose_car": "pony_goods_caboose_car_default_4",
                },
                {
                    "caboose_car": "pony_caboose_car_default_5",
                    "goods_caboose_car": "pony_goods_caboose_car_default_5",
                },
                {
                    "caboose_car": "pony_caboose_car_default_6",
                    "goods_caboose_car": "pony_goods_caboose_car_default_6",
                },
            ],
            "NG": [
                # ng caboose don't have much variation
                {"caboose_car": "pony_ng_caboose_car_1"},
                {"caboose_car": "pony_ng_caboose_car_1"},
                {"caboose_car": "pony_ng_caboose_car_2"},
                {"caboose_car": "pony_ng_caboose_car_3"},
            ],
        },
        # specify lists of cc2 colours, and an option to remap all the cc1 to a specific other cc (allowing multiple input colours to map to one result)
        livery_presets={
            "FOO": {
                "cc2": [
                    "COLOUR_PALE_GREEN",
                    "COLOUR_GREEN",
                    "COLOUR_DARK_GREEN",
                    # includes GBRF
                    "COLOUR_MAUVE",
                ],
                # note the remap to yellow, allowing 1cc wagons to be whatever player chooses
                "remap_to_cc": "COLOUR_YELLOW",
                "docs_image_input_cc": [
                    ("COLOUR_YELLOW", "COLOUR_PALE_GREEN"),
                    ("COLOUR_ORANGE", "COLOUR_DARK_GREEN"),
                    ("COLOUR_ORANGE", "COLOUR_GREEN"),
                    ("COLOUR_CREAM", "COLOUR_MAUVE"),
                ],
            },
        },
        # this list is manually maintained deliberately, even though it could be mostly automated using tech tree
        engines=[
            # challenger, # for NA roster
            # branch express
            #foo,
            # express (electro-diesels with non-standard position in power/length tree)
            #foo,
            # express
            #foo,
            # driving cab cars
            #foo,
            # branch freight
            #foo,
            # freight
            #foo,
            # joker engines / snowploughs
            snowplough_moose_gen_2,
            # cargo sprinter
            #foo,
            # auto-coach (only one as autoreplace can't handle mixed cargo articulated consists)
            #foo,
            # railbuses
            #foo,
            # diesel railcars
            #foo,
            # electric railcars
            #foo,
            # express electric railcars
            #foo,
            # high speed pax
            #foo,
            # metro
            #foo,
            # ng engines
            #foo,
            # ng railcars
            #foo,
        ],
    )
    roster.register(disabled=disabled)
