import os.path
currentdir = os.curdir

import sys
sys.path.append(os.path.join('src')) # add to the module search path

import iron_horse
import global_constants
from PIL import Image

consists = iron_horse.get_consists_in_buy_menu_order()
input_graphics_dir = os.path.join('src', 'graphics')
base_template_spritesheet = Image.open(os.path.join('src','base_10_8_spritesheet.png'))
spriterow_height = 30
DOS_PALETTE = Image.open('palette_key.png').palette

def get_legacy_bounding_boxes(y=0):
    return ([60,  y, 8, 27], [76,  y, 26, 24], [107, y, 40, 16], [156, y, 26, 24],
            [188, y, 8, 27], [200, y, 26, 24], [235, y, 40, 16], [284, y, 26, 24],
            [316, y, 64, 16])

def recomp_legacy_spriterows(count, spriterow, migrated_spritesheet):
    migrated_spriterow = base_template_spritesheet.crop((0, 10, 400, 40))
    for vertexes in get_legacy_bounding_boxes():
        crop_box = (vertexes[0], vertexes[1], vertexes[0] + vertexes[2], vertexes[1] + vertexes[3])
        sprite = spriterow.crop(crop_box)
        migrated_spriterow.paste(sprite, (vertexes[0], vertexes[1]))
    insert_loc = (0, 10 + count * spriterow_height)
    migrated_spritesheet.paste(migrated_spriterow, insert_loc)
    return migrated_spritesheet

def migrate_spritesheet(rows_with_valid_content):
    new_height = 10 + spriterow_height * len(rows_with_valid_content)
    migrated_spritesheet = Image.new("P", (400, new_height), 255)
    migrated_spritesheet.putpalette(DOS_PALETTE)
    for count, spriterow in enumerate(rows_with_valid_content):
        migrated_spritesheet = recomp_legacy_spriterows(count, spriterow, migrated_spritesheet)
    #migrated_spritesheet.show()
    return migrated_spritesheet

def detect_spriterows_with_content(filename):
    legacy_spritesheet = Image.open(os.path.join(input_graphics_dir, filename))
    base_y = 10
    rows_with_valid_content = []
    while base_y + spriterow_height < legacy_spritesheet.size[1]:
        crop_box = (0,
                    base_y,
                    legacy_spritesheet.size[0],
                    base_y + spriterow_height)
        test_row = legacy_spritesheet.crop(crop_box)
        base_y += spriterow_height
        if min(list(test_row.getdata())) < 255:
            # row contains some colours other than white, now check if it contains any blue, or if it's just leftover parts from drawing
            if min(list(test_row.getdata())) > 0:
                # this is just leftover parts, so show this image so it can be cleaned up manually
                test_row.show()
                print(filename, "contains some orphaned / leftover / junk pixels")
            else:
                rows_with_valid_content.append(test_row)
    return rows_with_valid_content

def main():
    legacy_filenames = []
    for consist in consists:
        if consist.use_legacy_spritesheet:
            # assumes spritesheets are suffixed _0 or _1, which is probably true
            for i in range(2):
                # non-template case
                filename = os.path.join(consist.id + '_' + str(i) + '.png')
                if os.path.isfile(os.path.join(input_graphics_dir, filename)):
                    legacy_filenames.append(filename)
                # template case
                filename = os.path.join(consist.id + '_template_' + str(i) + '.png')
                if os.path.isfile(os.path.join(input_graphics_dir, filename)):
                    legacy_filenames.append(filename)
    legacy_filenames.sort()

    for filename in legacy_filenames:
        output_path = os.path.join(currentdir, 'src', 'graphics_migrated', filename)
        rows_with_valid_content = detect_spriterows_with_content(filename)
        migrated_spritesheet = migrate_spritesheet(rows_with_valid_content)
        migrated_spritesheet.save(output_path)

    print('Count', len(legacy_filenames))

if __name__ == '__main__':
    main()

