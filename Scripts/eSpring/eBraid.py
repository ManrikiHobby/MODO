#python
# Easy Braid for MODO
# version: 1.0
#
# Author: Manriki
#
# coded under PEP8 Guideline.(as much as possible)
#
# Confirmed on:
#   MODO801 SP3
#   MODO701 SP5
#     windows7 64bit

from math import pi, sin, cos
import lx


# parameter class with check func.
class InParam:
    def __init__(self, default, min, max, clip):
        self.value = default
        self._default = default
        self._min = min
        self._max = max
        self._clip = clip

    def set(self, value):
        self.value = self.check(value)

    def check(self, value):
        checkedValue = value
        raiseException = False
        if(float(value) > float(self._max)):
            if(self._clip):
                checkedValue = self._max
            else:
                raiseException = True
        elif(float(value) < float(self._min)):
            if(self._clip):
                checkedValue = self._min
            else:
                raiseException = True

        if raiseException:
            raise ValueError("Out of range (" + str(value) + "). Please input again(" + str(self._min) + " - " + str(self._max) + ").")
        return checkedValue


# --------------------------------------------------------------
# Parameters (If you need, please customize these values.)
# --------------------------------------------------------------
params = {
#   Prefix        Default   Min   Max  Clip(clip or error when out of range)
    "L":  InParam(1,       0.1,    32, False),  # Length of braid(m) (approx.)
    "NW": InParam(8,         1,   128, False),  # total Number of Waves (approx.)
    "TH": InParam(0.05,  0.001,    16, False),  # THickness of braid(m) (approx.)
    "W":  InParam(0.1,   0.001,    16, False),  # Width of braid(m) (approx.)
    "NT": InParam(3,         2,     3, False),  # Number of Tassels(2 or 3 in current ver.)
    "PR": InParam(16,        8,    32, False),  # PRecision level(vertex num per 1 wave period)
    "DR": InParam(0,         0,     1, True),   # DiRection invert (1 | 0)
    "O":  InParam(1,         0,     1, True),   # One Mesh or multiple meshes(grouped) (1 | 0)
    "RC": InParam(0,         0,     1, True),   # Render Curve or not(1 | 0)
}

MESH_NAME_TASSEL = "New Tassel"
MESH_NAME_BRAID = "New Braid"


# --------------------------------------------------------------
# assemble arguments
# --------------------------------------------------------------
arguments = lx.args()
for arg in arguments:
    argParts = arg.split("=", 2)
    prefix = argParts[0].upper()
    inValue = argParts[1]
    if(prefix in params):
        params[prefix].set(inValue)

LENGTH = float(params["L"].value)
WAVE_DENSITY = int(float(params["NW"].value) / LENGTH)
THICKNESS = float(params["TH"].value)
WIDTH = float(params["W"].value)
TASSEL_NUM = int(params["NT"].value)
VERTEX_NUM_PER_PERIOD = int(params["PR"].value)
DIRECTION_INVERT = int(params["DR"].value)
ONE_MESH = int(params["O"].value)
RENDER_CURVE = int(params["RC"].value)

# derived parameters
TOTAL_VERTEX_NUM = int(LENGTH * WAVE_DENSITY * VERTEX_NUM_PER_PERIOD)  # total vertex num per tassel
PITCH = (float(LENGTH) / TOTAL_VERTEX_NUM)                             # interval of vertexes
Z_FREQ = (TASSEL_NUM - 1)                                              # frequency of sin curve of Z dir.


# Vertex Position
class VertexPos:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


# --------------------------------------------------------------
# generate new curve
# --------------------------------------------------------------
def generate_tassel_curve(tasselNo):

    # generate vertex
    ampX = WIDTH / 2
    ampZ = THICKNESS / 2

    phaseShift = (2 * pi) * tasselNo / TASSEL_NUM
    frequency = (pi * PITCH)

    if DIRECTION_INVERT:
        frequency = -frequency

    # judge whether twist tassel
    twist = False
    if(0 != (TASSEL_NUM % 2)):
        twist = True

    for step in range(0, TOTAL_VERTEX_NUM):
        theta = WAVE_DENSITY * (step * frequency) + phaseShift
        y = step * PITCH

        vert = get_vertex_pos(theta, y, ampX, ampZ, twist)
        lx.eval("vert.new %s %s %s" % (vert.x, vert.y, vert.z))

    # select all vtex
    lx.eval("select.vertex add edge all 0")

    # make curve
    lx.eval("poly.makeCurveOpen")


# --------------------------------------------------------------
# get vertex position
# --------------------------------------------------------------
def get_vertex_pos(theta, stepY, ampX, ampZ, twist=False):
    posX = ampX * round(sin(theta), 2)

    zStep = 0
    if twist:
        zStep = sin(theta * Z_FREQ)
    else:
        zStep = cos(theta * Z_FREQ)

    posZ = (ampZ * round(zStep, 2))

    return VertexPos(posX, stepY, posZ)


# --------------------------------------------------------------
# Main
# --------------------------------------------------------------
# generate new curve
items = []
for tasselNo in range(0, TASSEL_NUM):
    lx.eval("item.create mesh \"%s\"" % MESH_NAME_TASSEL)
    id = lx.eval('query sceneservice selection ? mesh')
    items.append(id)

    generate_tassel_curve(tasselNo)

# select new curves
for item in items:
    lx.eval("select.subItem %s" % item)

    if RENDER_CURVE:
        lx.eval("item.channel mesh$curves true")

# merge or group
if ONE_MESH:
    lx.eval("layer.mergeMeshes true")
    lx.eval("item.name \"%s\" mesh" % MESH_NAME_BRAID)
else:
    lx.eval("layer.groupSelected")
    lx.eval("item.name \"%s\" groupLocator" % MESH_NAME_BRAID)
