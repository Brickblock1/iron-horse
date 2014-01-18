#!/usr/bin/env python

"""
  This file is part of Iron Horse Newgrf for OpenTTD.
  Iron Horse is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, version 2.
  Iron Horse is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
  See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with Iron Horse. If not, see <http://www.gnu.org/licenses/>.
"""
print "[RENDER GRAPHICS] render_graphics.py"

import codecs # used for writing files - more unicode friendly than standard open() module

import shutil
import sys
import os
currentdir = os.curdir

import time
from multiprocessing import Process, active_children

import iron_horse
import utils
import global_constants

graphics_input = os.path.join(currentdir, 'src', 'graphics')
graphics_output_path = os.path.join(iron_horse.generated_files_path, 'graphics')
if os.path.exists(graphics_output_path):
    shutil.rmtree(graphics_output_path)
os.mkdir(graphics_output_path)

hint_file = codecs.open(os.path.join(graphics_output_path, '_graphics_files_here_are_generated.txt'), 'w','utf8')
hint_file.write("Don't edit the graphics files here.  They're generated by the build script. \n Edit sources in graphics_sources and export spritesheets to graphics_input.")
hint_file.close()

def run_pipeline(variant, consist):
    src_spritesheet = consist.id + '_' + str(variant.spritesheet_suffix) + '.png'
    if variant.graphics_processor is not None:
        variant.graphics_processor.pipeline.render(variant, consist)
        shutil.copy(os.path.join(graphics_input, src_spritesheet), graphics_output_path)
    else:
        shutil.copy(os.path.join(graphics_input, src_spritesheet), graphics_output_path)

# wrapped in a main() function so this can be called explicitly, because unexpected multiprocessing fork bombs are bad     
def main():
    consists = iron_horse.get_consists_in_buy_menu_order(show_warnings=True)
    variants = {}
    for consist in consists:
        spritesheet_suffixes_seen = []
        for variant in consist.model_variants:
            # raise if spritesheet_suffix number is a duplicate
            if variant.spritesheet_suffix in spritesheet_suffixes_seen:
                raise AssertionError("Duplicate spritesheet suffix in consist " + consist.id + ": " + str(variant.spritesheet_suffix))
            else:
                spritesheet_suffixes_seen.append(variant.spritesheet_suffix)
            variants[variant] = consist
        
    for variant, consist in variants.iteritems():
        Process(target=run_pipeline, args=(variant, consist,)).start()
        
    # dirty way to wait until all processes are complete before moving on
    while True:
        time.sleep(0.027) # 0.027 because it's a reference to TTD ticks :P (blame Rubidium)
        if len(active_children()) == 0:
            print "done"
            break
            
    # handle special case spritesheets
    shutil.copy(os.path.join(graphics_input, 'null_trailing_part.png'), graphics_output_path)

    """
    """     

if __name__ == '__main__': 
    main()
