from typing import Literal, NamedTuple

from panda3d.core import VBase3F


class ExtraProp(NamedTuple):
    node: str
    target: Literal["toon", "righthand", "lefthand"] = "toon"
    pos: VBase3F = (0, 0, 0)
    hpr: VBase3F = (0, 0, 0)
    scale: float = 1


KnownAnimations = {
    "neutral": ("neutral", 0),
    "wave": ("wave", 18),
    "run": ("run", 9),
    "seltzer": ("hold-bottle", 28),
    "magic": ("cast", 33),
    "button": ("pushbutton", 53.55),
    "cupcake": ("throw", 61.4),
}

pistolPos = VBase3F(0.28, 0.10, 0.08)
pistolHpr = VBase3F(85.60, -4.44, 94.43)
ExtraProps = {
    "seltzer": ExtraProp("phase_3.5/models/props/bottle", "righthand"),
    "button": ExtraProp("phase_3.5/models/props/button", "lefthand"),
    "cupcake": ExtraProp("phase_3.5/models/props/tart", "righthand"),
}


def getParentNode(toon, target):
    if target == "righthand":
        return toon.rightHands[0]
    elif target == "lefthand":
        return toon.leftHands[0]
    else:
        return toon
