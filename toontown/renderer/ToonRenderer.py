import sys

from direct.showbase.ShowBase import ShowBase
from panda3d.core import loadPrcFile

from toontown.renderer.RenderingSettings import ExtraProps, KnownAnimations, getParentNode
from toontown.toon.Toon import Toon


def prepareRenderer():
    base.cam.setPos(0, -10, 1.95)


def makeToonImage(dna: bytes, animation: str, rotation: int) -> tuple[bool, str]:
    """
    Returns a tuple (success, errMsg), and creates a file screenshot.png in the project root with the render
    Feel free to play around with rotation to figure out which values should be allowed
    """
    try:
        pose, frame = KnownAnimations[animation]
    except KeyError:
        return False, f"Unknown animation: {animation}"

    toon = Toon()
    try:
        toon.setDNAString(dna)
    except Exception:  # noqa
        toon.cleanup()
        return False, "Error while setting the Toon's DNA!"

    toon.reparentTo(render)
    prop = ExtraProps.get(animation)
    if prop:
        copy = loader.loadModel(prop.node)
        copy.reparentTo(getParentNode(toon, prop.target))
        copy.setPos(prop.pos)
        copy.setHpr(prop.hpr)

    toon.setHpr(rotation, 0, 0)
    toon.pose(pose, frame)
    base.graphicsEngine.renderFrame()
    base.graphicsEngine.renderFrame()

    filename = "screenshot.png"
    try:
        success = base.screenshot(filename, defaultFilename=0)
        if not success:
            return False, "Panda3D rendering error!"
        return True, ""
    finally:
        toon.detachNode()
        toon.cleanup()


def main():
    loadPrcFile("etc/Configrc.prc")
    ShowBase()
    prepareRenderer()
    success, err = makeToonImage(bytes.fromhex(sys.argv[1]), sys.argv[2], int(sys.argv[3]))
    if not success:
        print("Error while rendering:", err)


if __name__ == "__main__":
    main()
