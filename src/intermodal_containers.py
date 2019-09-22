# intermodal containers are sandboxed into their own module to avoid them spawning tentacles into gestalt graphics, global constants, train.py etc

from gestalt_graphics.pipelines import GenerateCompositedIntermodalContainers
import polar_fox

class IntermodalContainerGestalt(object):
    """ Sparse class to hold container gestalts """
    # a gestalt is a set of containers of specific length and appearance
    # each set corresponds to a spritesheet which will be generated by the graphics processor
    # each set is used for a specific group of cargo labels or classes
    # - multiple container types exist, e.g. box, tank, flat, bulk etc
    # - unknown and generic cargos default to box containers)
    # ====== #
    # each container set may have one or more spriterows
    # spriterows are chosen randomly when vehicles load new cargo
    # rows are composed by the graphics processor, and may include variations for
    # - combinations of container lengths
    # - combinations of container types
    # - container colours
    # !!! containers are going to need 'base sets' to allow double stack, cropped for well cars etc
    # !!! the consist needs to encode the set type to fetch the right spritesets
    # !!! base sets will also have to be encoded in gestalts here, unless they're done by (sets * gestalts) combinatorially?
    def __init__(self):
        self.pipeline = GenerateCompositedIntermodalContainers()

    @property
    def floor_height_variants(self):
        # used to handle, e.g. low floor, narrow gauge etc by putting a yoffset in the generated container sprites
        # extend to accomodate double stack later (only one floor height probably)?
        # format is (label, yoffset for floor-height) - leave floor height as 0 for default floor heights
        if self.stack_type == 'single':
            return (('default', 0), ('low_floor', 1))
        else:
            # other values not implemented yet
            raise ValueError()

    @property
    def id(self):
        return "intermodal_" + self.type + "_" + str(self.length) + "px"


# containers without visible cargo
# --------------------------------

class IntermodalBox16px(IntermodalContainerGestalt):
    def __init__(self):
        super().__init__()
        self.length = 16
        self.type = 'box'
        self.stack_type = 'single'
        self.variants = [['box_30_foot_1CC'],
                         ['box_30_foot_2CC'],
                         ['box_30_foot_red']]


class IntermodalBox24px(IntermodalContainerGestalt):
    def __init__(self):
        super().__init__()
        self.length = 24
        self.type = 'box'
        self.stack_type = 'single'
        self.variants = [['box_20_foot_1CC', 'box_20_foot_red'],
                         ['box_20_foot_red', 'box_20_foot_1CC'],
                         ['box_40_foot_1CC'],
                         ['box_40_foot_2CC'],
                         ['box_40_foot_red']]


class IntermodalBox32px(IntermodalContainerGestalt):
    def __init__(self):
        super().__init__()
        self.length = 32
        self.type = 'box'
        self.stack_type = 'single'
        self.variants = [['box_20_foot_1CC', 'box_20_foot_1CC', 'box_20_foot_red'],
                         ['box_20_foot_red', 'box_20_foot_red', 'box_20_foot_red'],
                         ['box_20_foot_2CC', 'box_20_foot_2CC', 'box_20_foot_2CC'],
                         ['box_20_foot_1CC', 'box_20_foot_1CC', 'box_20_foot_1CC'],
                         ['box_20_foot_1CC', 'box_40_foot_1CC'],
                         ['box_20_foot_2CC', 'box_40_foot_1CC'],
                         ['box_20_foot_red', 'box_40_foot_red'],
                         ['box_40_foot_1CC', 'box_20_foot_1CC'],
                         ['box_40_foot_2CC', 'box_20_foot_2CC'],
                         ['box_40_foot_2CC', 'box_20_foot_1CC'],
                         ['box_30_foot_1CC', 'box_30_foot_1CC']]


class IntermodalBulk16px(IntermodalContainerGestalt):
    def __init__(self):
        super().__init__()
        self.length = 16
        self.type = 'bulk'
        self.stack_type = 'single'
        self.variants = [['box_30_foot_1CC'],
                         ['box_30_foot_2CC']]


class IntermodalBulk24px(IntermodalContainerGestalt):
    def __init__(self):
        super().__init__()
        self.length = 24
        self.type = 'bulk'
        self.stack_type = 'single'
        self.variants = [['box_20_foot_1CC', 'box_20_foot_red'],
                         ['box_20_foot_red', 'box_20_foot_1CC'],
                         ['box_40_foot_1CC'],
                         ['box_40_foot_2CC'],
                         ['box_40_foot_red']]


class IntermodalBulk32px(IntermodalContainerGestalt):
    def __init__(self):
        super().__init__()
        self.length = 32
        self.type = 'bulk'
        self.stack_type = 'single'
        self.variants = [['box_20_foot_1CC', 'box_20_foot_red', 'box_20_foot_1CC'],
                         ['box_20_foot_red', 'box_20_foot_red', 'box_20_foot_red'],
                         ['box_20_foot_2CC', 'box_20_foot_2CC', 'box_20_foot_2CC'],
                         ['box_20_foot_1CC', 'box_20_foot_1CC', 'box_20_foot_1CC'],
                         ['box_20_foot_1CC', 'box_40_foot_1CC'],
                         ['box_20_foot_2CC', 'box_40_foot_1CC'],
                         ['box_20_foot_red', 'box_40_foot_red'],
                         ['box_40_foot_1CC', 'box_20_foot_1CC'],
                         ['box_40_foot_2CC', 'box_20_foot_2CC'],
                         ['box_40_foot_2CC', 'box_20_foot_1CC']]


class IntermodalEdiblesTank16px(IntermodalContainerGestalt):
    def __init__(self):
        super().__init__()
        self.length = 16
        self.type = 'edibles_tank'
        self.stack_type = 'single'
        self.variants = [['box_30_foot_1CC'],
                         ['box_30_foot_2CC']]


class IntermodalEdiblesTank24px(IntermodalContainerGestalt):
    def __init__(self):
        super().__init__()
        self.length = 24
        self.type = 'edibles_tank'
        self.stack_type = 'single'
        self.variants = [['box_20_foot_1CC', 'box_20_foot_red'],
                         ['box_20_foot_red', 'box_20_foot_1CC'],
                         ['box_40_foot_1CC'],
                         ['box_40_foot_2CC'],
                         ['box_40_foot_red']]


class IntermodalEdiblesTank32px(IntermodalContainerGestalt):
    def __init__(self):
        super().__init__()
        self.length = 32
        self.type = 'edibles_tank'
        self.stack_type = 'single'
        self.variants = [['box_20_foot_1CC', 'box_20_foot_red', 'box_20_foot_1CC'],
                         ['box_20_foot_red', 'box_20_foot_red', 'box_20_foot_red'],
                         ['box_20_foot_2CC', 'box_20_foot_2CC', 'box_20_foot_2CC'],
                         ['box_20_foot_1CC', 'box_20_foot_1CC', 'box_20_foot_1CC'],
                         ['box_20_foot_1CC', 'box_40_foot_1CC'],
                         ['box_20_foot_2CC', 'box_40_foot_1CC'],
                         ['box_20_foot_red', 'box_40_foot_red'],
                         ['box_40_foot_1CC', 'box_20_foot_1CC'],
                         ['box_40_foot_2CC', 'box_20_foot_2CC'],
                         ['box_40_foot_2CC', 'box_20_foot_1CC']]


class IntermodalFlat16px(IntermodalContainerGestalt):
    def __init__(self):
        super().__init__()
        self.length = 16
        self.type = 'flat'
        self.stack_type = 'single'
        self.variants = [['box_30_foot_1CC'],
                         ['box_30_foot_2CC']]


class IntermodalFlat24px(IntermodalContainerGestalt):
    def __init__(self):
        super().__init__()
        self.length = 24
        self.type = 'flat'
        self.stack_type = 'single'
        self.variants = [['box_20_foot_red', 'empty_20_foot',]]


class IntermodalFlat32px(IntermodalContainerGestalt):
    def __init__(self):
        super().__init__()
        self.length = 32
        self.type = 'flat'
        self.stack_type = 'single'
        self.variants = [['box_20_foot_red', 'empty_20_foot', 'empty_20_foot']]


class IntermodalLivestock16px(IntermodalContainerGestalt):
    def __init__(self):
        super().__init__()
        self.length = 16
        self.type = 'livestock'
        self.stack_type = 'single'
        self.variants = [['box_30_foot_1CC'],
                         ['box_30_foot_2CC']]


class IntermodalLivestock24px(IntermodalContainerGestalt):
    def __init__(self):
        super().__init__()
        self.length = 24
        self.type = 'livestock'
        self.stack_type = 'single'
        self.variants = [['box_20_foot_red', 'empty_20_foot',]]


class IntermodalLivestock32px(IntermodalContainerGestalt):
    def __init__(self):
        super().__init__()
        self.length = 32
        self.type = 'livestock'
        self.stack_type = 'single'
        self.variants = [['box_20_foot_red', 'empty_20_foot', 'empty_20_foot']]


class IntermodalReefer16px(IntermodalContainerGestalt):
    def __init__(self):
        super().__init__()
        self.length = 16
        self.type = 'reefer'
        self.stack_type = 'single'
        self.variants = [['box_30_foot_1CC'],
                         ['box_30_foot_2CC']]


class IntermodalReefer24px(IntermodalContainerGestalt):
    def __init__(self):
        super().__init__()
        self.length = 24
        self.type = 'reefer'
        self.stack_type = 'single'
        self.variants = [['box_20_foot_red', 'empty_20_foot',]]


class IntermodalReefer32px(IntermodalContainerGestalt):
    def __init__(self):
        super().__init__()
        self.length = 32
        self.type = 'reefer'
        self.stack_type = 'single'
        self.variants = [['box_20_foot_red', 'empty_20_foot', 'empty_20_foot']]


class IntermodalTank16px(IntermodalContainerGestalt):
    def __init__(self):
        super().__init__()
        self.length = 16
        self.type = 'tank'
        self.stack_type = 'single'
        self.variants = [['box_30_foot_1CC'],
                         ['box_30_foot_2CC']]


class IntermodalTank24px(IntermodalContainerGestalt):
    def __init__(self):
        super().__init__()
        self.length = 24
        self.type = 'tank'
        self.stack_type = 'single'
        self.variants = [['box_20_foot_red', 'empty_20_foot',]]


class IntermodalTank32px(IntermodalContainerGestalt):
    def __init__(self):
        super().__init__()
        self.length = 32
        self.type = 'tank'
        self.stack_type = 'single'
        self.variants = [['tank_20_foot_1CC', 'tank_20_foot_1CC', 'tank_20_foot_1CC'],
                         ['tank_30_foot_1CC', 'tank_30_foot_1CC'],
                         ['tank_40_foot_1CC', 'tank_20_foot_1CC']]


# containers with visible cargo
# -----------------------------

class IntermodalOpenBulkBase(IntermodalContainerGestalt):
    def __init__(self, cargo_label):
        super().__init__()
        self.type = cargo_label


class IntermodalOpenBulk16px(IntermodalOpenBulkBase):
    def __init__(self, cargo_label):
        super().__init__(cargo_label)
        self.length = 16
        self.stack_type = 'single'
        # !!!!!!!!!!!!!!!!! unfinished variants
        # by design, bulk containers are single-colour, no random variants
        self.variants = [['box_30_foot_1CC']]


class IntermodalOpenBulk24px(IntermodalOpenBulkBase):
    def __init__(self, cargo_label):
        super().__init__(cargo_label)
        self.length = 24
        self.stack_type = 'single'
        # by design, bulk containers are single-colour, no random variants
        bulk_20_foot = cargo_label + '_20_foot'
        self.variants = [[bulk_20_foot, bulk_20_foot]]


class IntermodalOpenBulk32px(IntermodalOpenBulkBase):
    def __init__(self, cargo_label):
        super().__init__(cargo_label)
        self.length = 32
        self.stack_type = 'single'
        # by design, bulk containers are single-colour, no random variants
        bulk_20_foot = cargo_label + '_20_foot'
        self.variants = [[bulk_20_foot, bulk_20_foot, bulk_20_foot]]


def get_container_gestalts_by_length(vehicle_length):
    result = []
    for container_gestalt in registered_container_gestalts:
        if container_gestalt.length == 4 * vehicle_length:
            result.append(container_gestalt)
    return result

registered_container_gestalts = []

def main():
    registered_container_gestalts.extend([IntermodalBox16px(),
                                          IntermodalBox24px(),
                                          IntermodalBox32px(),
                                          IntermodalBulk16px(),
                                          IntermodalBulk24px(),
                                          IntermodalBulk32px(),
                                          IntermodalEdiblesTank16px(),
                                          IntermodalEdiblesTank24px(),
                                          IntermodalEdiblesTank32px(),
                                          IntermodalFlat16px(),
                                          IntermodalFlat24px(),
                                          IntermodalFlat32px(),
                                          IntermodalLivestock16px(),
                                          IntermodalLivestock24px(),
                                          IntermodalLivestock32px(),
                                          IntermodalReefer16px(),
                                          IntermodalReefer24px(),
                                          IntermodalReefer32px(),
                                          IntermodalTank16px(),
                                          IntermodalTank24px(),
                                          IntermodalTank32px()])

    for cargo_label, body_recolour_name, cargo_recolour_map in polar_fox.constants.bulk_cargo_recolour_maps:
        registered_container_gestalts.append(IntermodalOpenBulk16px(cargo_label))
        registered_container_gestalts.append(IntermodalOpenBulk24px(cargo_label))
        registered_container_gestalts.append(IntermodalOpenBulk32px(cargo_label))
