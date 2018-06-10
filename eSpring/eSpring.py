#python
# Easy Spring for MODO
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
    "L":  InParam(1,         0,    32, False),  # Length of spring(m) (approx.)
    "N":  InParam(20,        1,   512, False),  # Number of turns(approx.)
    "R":  InParam(0.1,    0.01,    32, False),  # Radius of basic coil(m) (approx.)
    "RN": InParam(8,         6,    16, False),  # RoundNess(vertex num per 1 coil.)
    "SP": InParam(0.0,     0.0,     8, False),  # SPreading rate of radius(currently linier only.)
    "DR": InParam(0,         0,     1, True),   # DiRection invert (1 | 0)
    "RC": InParam(0,         0,     1, True),   # Render Curve or not(1 | 0)
}

MESH_NAME_SPRING = "New Spring"
MESH_NAME_SPIRAL = "New Spiral"

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
COIL_NUM = int(params["N"].value)
RADIUS = float(params["R"].value)
VERT_PER_COIL = int(params["RN"].value)
RADIUS_SPREAD = float(params["SP"].value)
DIRECTION_INVERT = int(params["DR"].value)
RENDER_CURVE = int(params["RC"].value)


# Vertex Position
class VertexPos:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


# --------------------------------------------------------------
# get vertex position
# --------------------------------------------------------------
def get_vertex_pos(rad, theta, pitch, step):
    return VertexPos(round(rad * cos(theta), 3),
                     pitch * step,
                     round(rad * sin(theta), 3))


# --------------------------------------------------------------
#  Main
# --------------------------------------------------------------
meshName = MESH_NAME_SPRING
if(LENGTH == 0):
    meshName = MESH_NAME_SPIRAL
lx.eval("item.create mesh \"%s\"" % meshName)


# derived parameters
vert_num = COIL_NUM * VERT_PER_COIL
pitch = (LENGTH / COIL_NUM) / VERT_PER_COIL
frequency = ((2 * pi) / VERT_PER_COIL)

# generate vtex
if DIRECTION_INVERT:
    frequency = -frequency

for step in range(0, vert_num):
    theta = frequency * step
    radiusStep = RADIUS * (1 + (RADIUS_SPREAD * step))
    vert = get_vertex_pos(radiusStep, theta, pitch, step)
    lx.eval("vert.new %s %s %s" % (vert.x, vert.y, vert.z))

# select all vtex
lx.eval("select.vertex add edge all 0")

# make curve
lx.eval("poly.makeCurveOpen")

if RENDER_CURVE:
    lx.eval("item.channel mesh$curves true")
