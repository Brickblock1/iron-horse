from roster import Roster

from vehicles import americano
from vehicles import anaconda
from vehicles import argentina
from vehicles import astarsa
from vehicles import breda
from vehicles import burro
from vehicles import cooke
from vehicles import electrico
from vehicles import estados
from vehicles import evolucao
from vehicles import justicialista
from vehicles import krauss
from vehicles import pacifico
from vehicles import pala
from vehicles import peacock
from vehicles import potosi
from vehicles import roca
from vehicles import super_mountain
from vehicles import thing_ng
from vehicles import universal
from vehicles import ut440
from vehicles import v8

# speed for wagons in mph (some generations may optionally have no speed set)
# format is [standard, speedy]
speeds = dict(gen_1_wagon_speeds = [50, 65],
              gen_2_wagon_speeds = [65, 85],
              gen_3_wagon_speeds = [85, None],
              ng_wagon_speeds = [40, 70])

roster = Roster(id = 'soam',
                speeds = speeds,
                engines = [thing_ng,
                           burro,
                           americano,
                           peacock,
                           cooke,
                           pacifico,
                           argentina,
                           potosi,
                           super_mountain,
                           electrico,
                           estados,
                           breda,
                           v8,
                           ut440,
                           justicialista,
                           krauss,
                           pala,
                           astarsa,
                           universal,
                           evolucao,
                           roca,
                           anaconda])
