import random

from direct.actor import Actor
from direct.fsm.ClassicFSM import ClassicFSM
from direct.fsm.State import State
from direct.interval.IntervalGlobal import *
from direct.task import Task
from panda3d.core import *
from direct.directnotify.DirectNotifyGlobal import *

from toontown.toon.TTGlobalsAvatars import ToonBodyScales

HeadDict = {
    "dls": "/models/char/tt_a_chr_dgm_shorts_head_",
    "dss": "/models/char/tt_a_chr_dgm_skirt_head_",
    "dsl": "/models/char/tt_a_chr_dgs_shorts_head_",
    "dll": "/models/char/tt_a_chr_dgl_shorts_head_",
    "c": "/models/char/cat-heads-",
    "h": "/models/char/horse-heads-",
    "m": "/models/char/mouse-heads-",
    "r": "/models/char/rabbit-heads-",
    "f": "/models/char/duck-heads-",
    "p": "/models/char/monkey-heads-",
    "b": "/models/char/bear-heads-",
    "s": "/models/char/pig-heads-",
}
EyelashDict = {
    "d": "/models/char/dog-lashes",
    "c": "/models/char/cat-lashes",
    "h": "/models/char/horse-lashes",
    "m": "/models/char/mouse-lashes",
    "r": "/models/char/rabbit-lashes",
    "f": "/models/char/duck-lashes",
    "p": "/models/char/monkey-lashes",
    "b": "/models/char/bear-lashes",
    "s": "/models/char/pig-lashes",
}
DogMuzzleDict = {
    "dls": "/models/char/dogMM_Shorts-headMuzzles-",
    "dss": "/models/char/dogMM_Skirt-headMuzzles-",
    "dsl": "/models/char/dogSS_Shorts-headMuzzles-",
    "dll": "/models/char/dogLL_Shorts-headMuzzles-",
}


class ToonHead(Actor.Actor):
    EyesOpen = None
    EyesClosed = None
    EyesSadOpen = None
    EyesSadClosed = None
    EyesAngryOpen = None
    EyesAngryClosed = None
    EyesSurprised = None
    Muzzle = None
    MuzzleSurprised = None

    notify = directNotify.newCategory("ToonHead")
    LeftA = Point3(0.06, 0.0, 0.14)
    LeftB = Point3(-0.13, 0.0, 0.1)
    LeftC = Point3(-0.05, 0.0, 0.0)
    LeftD = Point3(0.06, 0.0, 0.0)
    RightA = Point3(0.13, 0.0, 0.1)
    RightB = Point3(-0.06, 0.0, 0.14)
    RightC = Point3(-0.06, 0.0, 0.0)
    RightD = Point3(0.05, 0.0, 0.0)
    LeftAD = Point3(LeftA[0] - LeftA[2] * (LeftD[0] - LeftA[0]) / (LeftD[2] - LeftA[2]), 0.0, 0.0)
    LeftBC = Point3(LeftB[0] - LeftB[2] * (LeftC[0] - LeftB[0]) / (LeftC[2] - LeftB[2]), 0.0, 0.0)
    RightAD = Point3(RightA[0] - RightA[2] * (RightD[0] - RightA[0]) / (RightD[2] - RightA[2]), 0.0, 0.0)
    RightBC = Point3(RightB[0] - RightB[2] * (RightC[0] - RightB[0]) / (RightC[2] - RightB[2]), 0.0, 0.0)

    @staticmethod
    def loadEyeTextures():
        if ToonHead.EyesOpen is not None:
            return

        EyesOpen = ToonHead.EyesOpen = loader.loadTexture("phase_3/maps/eyes.png")
        EyesOpen.setMinfilter(Texture.FTLinear)
        EyesOpen.setMagfilter(Texture.FTLinear)
        EyesClosed = ToonHead.EyesClosed = loader.loadTexture("phase_3/maps/eyesClosed.png")
        EyesClosed.setMinfilter(Texture.FTLinear)
        EyesClosed.setMagfilter(Texture.FTLinear)
        EyesSadOpen = ToonHead.EyesSadOpen = loader.loadTexture("phase_3/maps/eyesSad.png")
        EyesSadOpen.setMinfilter(Texture.FTLinear)
        EyesSadOpen.setMagfilter(Texture.FTLinear)
        EyesSadClosed = ToonHead.EyesSadClosed = loader.loadTexture("phase_3/maps/eyesSadClosed.png")
        EyesSadClosed.setMinfilter(Texture.FTLinear)
        EyesSadClosed.setMagfilter(Texture.FTLinear)
        EyesAngryOpen = ToonHead.EyesAngryOpen = loader.loadTexture("phase_3/maps/eyesAngry.png")
        EyesAngryOpen.setMinfilter(Texture.FTLinear)
        EyesAngryOpen.setMagfilter(Texture.FTLinear)
        EyesAngryClosed = ToonHead.EyesAngryClosed = loader.loadTexture("phase_3/maps/eyesAngryClosed.png")
        EyesAngryClosed.setMinfilter(Texture.FTLinear)
        EyesAngryClosed.setMagfilter(Texture.FTLinear)
        EyesSurprised = ToonHead.EyesSurprised = loader.loadTexture("phase_3/maps/eyesSurprised.png")
        EyesSurprised.setMinfilter(Texture.FTLinear)
        EyesSurprised.setMagfilter(Texture.FTLinear)
        Muzzle = ToonHead.Muzzle = loader.loadTexture("phase_3/maps/muzzleShrtGeneric.png")
        Muzzle.setMinfilter(Texture.FTLinear)
        Muzzle.setMagfilter(Texture.FTLinear)
        MuzzleSurprised = ToonHead.MuzzleSurprised = loader.loadTexture("phase_3/maps/muzzleShortSurprised.png")
        MuzzleSurprised.setMinfilter(Texture.FTLinear)
        MuzzleSurprised.setMagfilter(Texture.FTLinear)

    def __init__(self):
        Actor.Actor.__init__(self)
        self.loadEyeTextures()
        self.toonName = "ToonHead-" + str(self.this)
        self.__blinkName = "blink-" + self.toonName
        self.__stareAtName = "stareAt-" + self.toonName
        self.__lookName = "look-" + self.toonName
        self.lookAtTrack = None
        self.__eyes = None
        self.__eyelashOpen = None
        self.__eyelashClosed = None
        self.__lod500Eyes = None
        self.__lod250Eyes = None
        self.__lpupil = None
        self.__lod500lPupil = None
        self.__lod250lPupil = None
        self.__rpupil = None
        self.__lod500rPupil = None
        self.__lod250rPupil = None
        self.__muzzle = None
        self.__eyesOpen = ToonHead.EyesOpen
        self.__eyesClosed = ToonHead.EyesClosed
        self.__height = 0.0
        self.__eyelashesHiddenByGlasses = False
        self.randGen = random.Random()
        self.randGen.seed(random.random())
        self.eyelids = ClassicFSM(
            "eyelids",
            [
                State("off", self.enterEyelidsOff, self.exitEyelidsOff, ["open", "closed", "surprised"]),
                State("open", self.enterEyelidsOpen, self.exitEyelidsOpen, ["closed", "surprised", "off"]),
                State("surprised", self.enterEyelidsSurprised, self.exitEyelidsSurprised, ["open", "closed", "off"]),
                State("closed", self.enterEyelidsClosed, self.exitEyelidsClosed, ["open", "surprised", "off"]),
            ],
            "off",
            "off",
        )
        self.eyelids.enterInitialState()
        self.emote = None
        self.__stareAtNode = NodePath()
        self.__defaultStarePoint = Point3(0, 0, 0)
        self.__stareAtPoint = self.__defaultStarePoint
        self.__stareAtTime = 0
        self.lookAtPositionCallbackArgs = None

    def delete(self):
        taskMgr.remove(self.__blinkName)
        taskMgr.remove(self.__lookName)
        taskMgr.remove(self.__stareAtName)
        if self.lookAtTrack:
            self.lookAtTrack.finish()
            self.lookAtTrack = None
        del self.eyelids
        del self.__stareAtNode
        del self.__stareAtPoint
        if self.__eyes:
            del self.__eyes
        if self.__lpupil:
            del self.__lpupil
        if self.__rpupil:
            del self.__rpupil
        if self.__eyelashOpen:
            del self.__eyelashOpen
        if self.__eyelashClosed:
            del self.__eyelashClosed
        self.lookAtPositionCallbackArgs = None
        Actor.Actor.delete(self)

    def setupHead(self, dna, forGui=0):
        self.__height = self.generateToonHead(1, dna, ("1000",), forGui)
        self.generateToonColor(dna)
        animalStyle = dna.getAnimal()
        bodyScale = ToonBodyScales[animalStyle]
        self.getGeomNode().setScale(bodyScale * 1.3)
        if forGui:
            self.getGeomNode().setDepthWrite(1)
            self.getGeomNode().setDepthTest(1)
        if dna.getAnimal() == "dog":
            self.loop("neutral")

    def fitAndCenterHead(self, maxDim, forGui=0):
        p1 = Point3()
        p2 = Point3()
        self.calcTightBounds(p1, p2)
        if forGui:
            h = 180
            t = p1[0]
            p1.setX(-p2[0])
            p2.setX(-t)
        else:
            h = 0
        d = p2 - p1
        biggest = max(d[0], d[2])
        s = maxDim / biggest
        mid = (p1 + d / 2.0) * s
        self.setPosHprScale(-mid[0], -mid[1] + 1, -mid[2], h, 0, 0, s, s, s)

    def setLookAtPositionCallbackArgs(self, argTuple):
        self.lookAtPositionCallbackArgs = argTuple

    def getHeight(self):
        return self.__height

    def getRandomForwardLookAtPoint(self):
        x = self.randGen.choice((-0.8, -0.5, 0, 0.5, 0.8))
        z = self.randGen.choice((-0.5, 0, 0.5, 0.8))
        return Point3(x, 1.5, z)

    def findSomethingToLookAt(self):
        if self.lookAtPositionCallbackArgs is not None:
            pnt = self.lookAtPositionCallbackArgs[0].getLookAtPosition(
                self.lookAtPositionCallbackArgs[1], self.lookAtPositionCallbackArgs[2]
            )
            self.startStareAt(self, pnt)
            return
        lookAtPnt = self.getRandomForwardLookAtPoint() if self.randGen.random() < 0.33 else self.__defaultStarePoint
        self.lerpLookAt(lookAtPnt, blink=1)
        return

    def generateToonHead(self, copy, style, lods, forGui=0):
        headStyle = style.head
        fix = None
        if headStyle == "dls":
            filePrefix = HeadDict["dls"]
            headHeight = 0.75
        elif headStyle == "dss":
            filePrefix = HeadDict["dss"]
            headHeight = 0.5
        elif headStyle == "dsl":
            filePrefix = HeadDict["dsl"]
            headHeight = 0.5
        elif headStyle == "dll":
            filePrefix = HeadDict["dll"]
            headHeight = 0.75
        elif headStyle == "cls":
            filePrefix = HeadDict["c"]
            fix = self.__fixHeadLongShort
            headHeight = 0.75
        elif headStyle == "css":
            filePrefix = HeadDict["c"]
            fix = self.__fixHeadShortShort
            headHeight = 0.5
        elif headStyle == "csl":
            filePrefix = HeadDict["c"]
            fix = self.__fixHeadShortLong
            headHeight = 0.5
        elif headStyle == "cll":
            filePrefix = HeadDict["c"]
            fix = self.__fixHeadLongLong
            headHeight = 0.75
        elif headStyle == "hls":
            filePrefix = HeadDict["h"]
            fix = self.__fixHeadLongShort
            headHeight = 0.75
        elif headStyle == "hss":
            filePrefix = HeadDict["h"]
            fix = self.__fixHeadShortShort
            headHeight = 0.5
        elif headStyle == "hsl":
            filePrefix = HeadDict["h"]
            fix = self.__fixHeadShortLong
            headHeight = 0.5
        elif headStyle == "hll":
            filePrefix = HeadDict["h"]
            fix = self.__fixHeadLongLong
            headHeight = 0.75
        elif headStyle == "mls":
            filePrefix = HeadDict["m"]
            fix = self.__fixHeadLongShort
            headHeight = 0.75
        elif headStyle == "mss":
            filePrefix = HeadDict["m"]
            fix = self.__fixHeadShortShort
            headHeight = 0.5
        elif headStyle == "rls":
            filePrefix = HeadDict["r"]
            fix = self.__fixHeadLongShort
            headHeight = 0.75
        elif headStyle == "rss":
            filePrefix = HeadDict["r"]
            fix = self.__fixHeadShortShort
            headHeight = 0.5
        elif headStyle == "rsl":
            filePrefix = HeadDict["r"]
            fix = self.__fixHeadShortLong
            headHeight = 0.5
        elif headStyle == "rll":
            filePrefix = HeadDict["r"]
            fix = self.__fixHeadLongLong
            headHeight = 0.75
        elif headStyle == "fls":
            filePrefix = HeadDict["f"]
            fix = self.__fixHeadLongShort
            headHeight = 0.75
        elif headStyle == "fss":
            filePrefix = HeadDict["f"]
            fix = self.__fixHeadShortShort
            headHeight = 0.5
        elif headStyle == "fsl":
            filePrefix = HeadDict["f"]
            fix = self.__fixHeadShortLong
            headHeight = 0.5
        elif headStyle == "fll":
            filePrefix = HeadDict["f"]
            fix = self.__fixHeadLongLong
            headHeight = 0.75
        elif headStyle == "pls":
            filePrefix = HeadDict["p"]
            fix = self.__fixHeadLongShort
            headHeight = 0.75
        elif headStyle == "pss":
            filePrefix = HeadDict["p"]
            fix = self.__fixHeadShortShort
            headHeight = 0.5
        elif headStyle == "psl":
            filePrefix = HeadDict["p"]
            fix = self.__fixHeadShortLong
            headHeight = 0.5
        elif headStyle == "pll":
            filePrefix = HeadDict["p"]
            fix = self.__fixHeadLongLong
            headHeight = 0.75
        elif headStyle == "bls":
            filePrefix = HeadDict["b"]
            fix = self.__fixHeadLongShort
            headHeight = 0.75
        elif headStyle == "bss":
            filePrefix = HeadDict["b"]
            fix = self.__fixHeadShortShort
            headHeight = 0.5
        elif headStyle == "bsl":
            filePrefix = HeadDict["b"]
            fix = self.__fixHeadShortLong
            headHeight = 0.5
        elif headStyle == "bll":
            filePrefix = HeadDict["b"]
            fix = self.__fixHeadLongLong
            headHeight = 0.75
        elif headStyle == "sls":
            filePrefix = HeadDict["s"]
            fix = self.__fixHeadLongShort
            headHeight = 0.75
        elif headStyle == "sss":
            filePrefix = HeadDict["s"]
            fix = self.__fixHeadShortShort
            headHeight = 0.5
        elif headStyle == "ssl":
            filePrefix = HeadDict["s"]
            fix = self.__fixHeadShortLong
            headHeight = 0.5
        elif headStyle == "sll":
            filePrefix = HeadDict["s"]
            fix = self.__fixHeadLongLong
            headHeight = 0.75
        else:
            raise ValueError("unknown head style: %s" % headStyle)
        if len(lods) == 1:
            self.loadModel("phase_3" + filePrefix + lods[0], "head", "lodRoot", copy)
            if not copy:
                self.showAllParts("head")
            if fix is not None:
                fix(style, None, copy)
            if not forGui:
                self.__lods = lods
                self.__style = style
                self.__headStyle = headStyle
                self.__copy = copy
        else:
            for lod in lods:
                self.loadModel("phase_3" + filePrefix + lod, "head", lod, copy)
                if not copy:
                    self.showAllParts("head", lod)
                if fix is not None:
                    fix(style, lod, copy)
                if not forGui:
                    self.__lods = lods
                    self.__style = style
                    self.__headStyle = headStyle
                    self.__copy = copy

        self.__fixEyes(style, forGui)
        self.setupEyelashes(style)
        self.eyelids.request("closed")
        self.eyelids.request("open")
        self.setupMuzzles(style)
        return headHeight

    def hideEars(self):
        self.findAllMatches("**/ears*;+s").stash()

    def showEars(self):
        self.findAllMatches("**/ears*;+s").unstash()

    def hideEyelashes(self):
        if self.__eyelashOpen:
            self.__eyelashOpen.stash()
        if self.__eyelashClosed:
            self.__eyelashClosed.stash()
        self.__eyelashesHiddenByGlasses = True

    def showEyelashes(self):
        if self.__eyelashOpen:
            self.__eyelashOpen.unstash()
        if self.__eyelashClosed:
            self.__eyelashClosed.unstash()
        self.__eyelashesHiddenByGlasses = False

    def generateToonColor(self, style):
        parts = self.findAllMatches("**/head*")
        parts.setColor(style.getHeadColor())
        animalType = style.getAnimal()
        if animalType in ("cat", "rabbit", "bear", "mouse", "pig"):
            parts = self.findAllMatches("**/ear?-*")
            parts.setColor(style.getHeadColor())

    def __fixEyes(self, style, forGui=0):
        mode = -3
        if forGui:
            mode = -2
        if self.hasLOD():
            for lodName in self.getLODNames():
                self.drawInFront("eyes*", "head-front*", mode, lodName=lodName)
                if not self.find("**/joint_pupil*").isEmpty():
                    self.drawInFront("joint_pupil*", "eyes*", -1, lodName=lodName)
                else:
                    self.drawInFront("def_*_pupil", "eyes*", -1, lodName=lodName)

            self.__eyes = self.getLOD(1000).find("**/eyes*")
            self.__lod500Eyes = self.getLOD(500).find("**/eyes*")
            self.__lod250Eyes = self.getLOD(250).find("**/eyes*")
            if self.__lod500Eyes.isEmpty():
                self.__lod500Eyes = None
            else:
                self.__lod500Eyes.setColorOff()
                if not self.find("**/joint_pupilL*").isEmpty():
                    self.__lod500lPupil = self.__lod500Eyes.find("**/joint_pupilL*")
                    self.__lod500rPupil = self.__lod500Eyes.find("**/joint_pupilR*")
                else:
                    self.__lod500lPupil = self.__lod500Eyes.find("**/def_left_pupil*")
                    self.__lod500rPupil = self.__lod500Eyes.find("**/def_right_pupil*")
            if self.__lod250Eyes.isEmpty():
                self.__lod250Eyes = None
            else:
                self.__lod250Eyes.setColorOff()
                if not self.find("**/joint_pupilL*").isEmpty():
                    self.__lod250lPupil = self.__lod250Eyes.find("**/joint_pupilL*")
                    self.__lod250rPupil = self.__lod250Eyes.find("**/joint_pupilR*")
                else:
                    self.__lod250lPupil = self.__lod250Eyes.find("**/def_left_pupil*")
                    self.__lod250rPupil = self.__lod250Eyes.find("**/def_right_pupil*")
        else:
            self.drawInFront("eyes*", "head-front*", mode)
            if not self.find("joint_pupil*").isEmpty():
                self.drawInFront("joint_pupil*", "eyes*", -1)
            else:
                self.drawInFront("def_*_pupil", "eyes*", -1)
            self.__eyes = self.find("**/eyes*")
        if not self.__eyes.isEmpty():
            self.__eyes.setColorOff()
            self.__lpupil = None
            self.__rpupil = None
            if not self.find("**/joint_pupilL*").isEmpty():
                if self.getLOD(1000):
                    lp = self.getLOD(1000).find("**/joint_pupilL*")
                    rp = self.getLOD(1000).find("**/joint_pupilR*")
                else:
                    lp = self.find("**/joint_pupilL*")
                    rp = self.find("**/joint_pupilR*")
            elif not self.getLOD(1000):
                lp = self.find("**/def_left_pupil*")
                rp = self.find("**/def_right_pupil*")
            else:
                lp = self.getLOD(1000).find("**/def_left_pupil*")
                rp = self.getLOD(1000).find("**/def_right_pupil*")
            if lp.isEmpty() or rp.isEmpty():
                self.notify.warning("Unable to locate pupils.")
            else:
                leye = self.__eyes.attachNewNode("leye")
                reye = self.__eyes.attachNewNode("reye")
                lmat = Mat4(
                    0.802174,
                    0.59709,
                    0,
                    0,
                    -0.586191,
                    0.787531,
                    0.190197,
                    0,
                    0.113565,
                    -0.152571,
                    0.981746,
                    0,
                    -0.233634,
                    0.418062,
                    0.0196875,
                    1,
                )
                leye.setMat(lmat)
                rmat = Mat4(
                    0.786788,
                    -0.617224,
                    0,
                    0,
                    0.602836,
                    0.768447,
                    0.214658,
                    0,
                    -0.132492,
                    -0.16889,
                    0.976689,
                    0,
                    0.233634,
                    0.418062,
                    0.0196875,
                    1,
                )
                reye.setMat(rmat)
                self.__lpupil = leye.attachNewNode("lpupil")
                self.__rpupil = reye.attachNewNode("rpupil")
                lpt = self.__eyes.attachNewNode("")
                rpt = self.__eyes.attachNewNode("")
                lpt.wrtReparentTo(self.__lpupil)
                rpt.wrtReparentTo(self.__rpupil)
                lp.reparentTo(lpt)
                rp.reparentTo(rpt)
                self.__lpupil.adjustAllPriorities(1)
                self.__rpupil.adjustAllPriorities(1)
                if self.__lod500Eyes:
                    self.__lod500lPupil.adjustAllPriorities(1)
                    self.__lod500rPupil.adjustAllPriorities(1)
                if self.__lod250Eyes:
                    self.__lod250lPupil.adjustAllPriorities(1)
                    self.__lod250rPupil.adjustAllPriorities(1)
                animalType = style.getAnimal()
                if animalType != "dog":
                    self.__lpupil.flattenStrong()
                    self.__rpupil.flattenStrong()

    def __setPupilDirection(self, x, y):
        if y < 0.0:
            y2 = -y
            left1 = self.LeftAD + (self.LeftD - self.LeftAD) * y2
            left2 = self.LeftBC + (self.LeftC - self.LeftBC) * y2
            right1 = self.RightAD + (self.RightD - self.RightAD) * y2
            right2 = self.RightBC + (self.RightC - self.RightBC) * y2
        else:
            y2 = y
            left1 = self.LeftAD + (self.LeftA - self.LeftAD) * y2
            left2 = self.LeftBC + (self.LeftB - self.LeftBC) * y2
            right1 = self.RightAD + (self.RightA - self.RightAD) * y2
            right2 = self.RightBC + (self.RightB - self.RightBC) * y2
        left0 = Point3(0.0, 0.0, left1[2] - left1[0] * (left2[2] - left1[2]) / (left2[0] - left1[0]))
        right0 = Point3(0.0, 0.0, right1[2] - right1[0] * (right2[2] - right1[2]) / (right2[0] - right1[0]))
        if x < 0.0:
            x2 = -x
            left = left0 + (left2 - left0) * x2
            right = right0 + (right2 - right0) * x2
        else:
            x2 = x
            left = left0 + (left1 - left0) * x2
            right = right0 + (right1 - right0) * x2
        self.__lpupil.setPos(left)
        self.__rpupil.setPos(right)

    def __lookPupilsAt(self, node, point):
        if node is not None:
            mat = node.getMat(self.__eyes)
            point = mat.xformPoint(point)
        distance = 1.0
        recip_z = 1.0 / max(0.1, point[1])
        x = distance * point[0] * recip_z
        y = distance * point[2] * recip_z
        x = min(max(x, -1), 1)
        y = min(max(y, -1), 1)
        self.__setPupilDirection(x, y)

    def __lookHeadAt(self, node, point, frac=1.0, lod=None):
        reachedTarget = 1
        head = self.getPart("head", self.getLODNames()[0]) if lod is None else self.getPart("head", lod)
        if node is not None:
            headParent = head.getParent()
            mat = node.getMat(headParent)
            point = mat.xformPoint(point)
        rot = Mat3(0, 0, 0, 0, 0, 0, 0, 0, 0)
        lookAt(rot, Vec3(point), Vec3(0, 0, 1), CSDefault)
        scale = VBase3(0, 0, 0)
        hpr = VBase3(0, 0, 0)
        if decomposeMatrix(rot, scale, hpr, CSDefault):
            hpr = VBase3(min(max(hpr[0], -60), 60), min(max(hpr[1], -20), 30), 0)
            if frac != 1:
                currentHpr = head.getHpr()
                reachedTarget = abs(hpr[0] - currentHpr[0]) < 1.0 and abs(hpr[1] - currentHpr[1]) < 1.0
                hpr = currentHpr + (hpr - currentHpr) * frac
            if lod is None:
                for lodName in self.getLODNames():
                    head = self.getPart("head", lodName)
                    head.setHpr(hpr)

            else:
                head.setHpr(hpr)
        return reachedTarget

    def setupEyelashes(self, style):
        if style.getGender() == "m":
            if self.__eyelashOpen:
                self.__eyelashOpen.removeNode()
                self.__eyelashOpen = None
            if self.__eyelashClosed:
                self.__eyelashClosed.removeNode()
                self.__eyelashClosed = None
        else:
            if self.__eyelashOpen:
                self.__eyelashOpen.removeNode()
            if self.__eyelashClosed:
                self.__eyelashClosed.removeNode()
            animal = style.head[0]
            model = loader.loadModel("phase_3" + EyelashDict[animal])
            head = self.getPart("head", "1000") if self.hasLOD() else self.getPart("head", "lodRoot")
            length = style.head[1]
            if length == "l":
                openString = "open-long"
                closedString = "closed-long"
            else:
                openString = "open-short"
                closedString = "closed-short"
            self.__eyelashOpen = model.find("**/" + openString).copyTo(head)
            self.__eyelashClosed = model.find("**/" + closedString).copyTo(head)
            model.removeNode()

    def __fixHeadLongLong(self, style, lodName=None, copy=1):
        searchRoot = self if lodName is None else self.find("**/" + str(lodName))
        otherParts = searchRoot.findAllMatches("**/*short*")
        for partNum in range(0, otherParts.getNumPaths()):
            if copy:
                otherParts.getPath(partNum).removeNode()
            else:
                otherParts.getPath(partNum).stash()

    def __fixHeadLongShort(self, style, lodName=None, copy=1):
        animalType = style.getAnimal()
        searchRoot = self if lodName is None else self.find("**/" + str(lodName))
        if animalType not in ("duck", "horse"):
            if animalType == "rabbit":
                if copy:
                    searchRoot.find("**/ears-long").removeNode()
                else:
                    searchRoot.find("**/ears-long").hide()
            elif copy:
                searchRoot.find("**/ears-short").removeNode()
            else:
                searchRoot.find("**/ears-short").hide()
        if animalType != "rabbit":
            if copy:
                searchRoot.find("**/eyes-short").removeNode()
            else:
                searchRoot.find("**/eyes-short").hide()
        if animalType != "dog":
            if copy:
                searchRoot.find("**/joint_pupilL_short").removeNode()
                searchRoot.find("**/joint_pupilR_short").removeNode()
            else:
                searchRoot.find("**/joint_pupilL_short").stash()
                searchRoot.find("**/joint_pupilR_short").stash()
        if copy:
            self.find("**/head-short").removeNode()
            self.find("**/head-front-short").removeNode()
        else:
            self.find("**/head-short").hide()
            self.find("**/head-front-short").hide()
        if animalType != "rabbit":
            muzzleParts = searchRoot.findAllMatches("**/muzzle-long*")
            for partNum in range(0, muzzleParts.getNumPaths()):
                if copy:
                    muzzleParts.getPath(partNum).removeNode()
                else:
                    muzzleParts.getPath(partNum).hide()

        else:
            muzzleParts = searchRoot.findAllMatches("**/muzzle-short*")
            for partNum in range(0, muzzleParts.getNumPaths()):
                if copy:
                    muzzleParts.getPath(partNum).removeNode()
                else:
                    muzzleParts.getPath(partNum).hide()

    def __fixHeadShortLong(self, style, lodName=None, copy=1):
        animalType = style.getAnimal()
        searchRoot = self if lodName is None else self.find("**/" + str(lodName))
        if animalType not in ("duck", "horse"):
            if animalType == "rabbit":
                if copy:
                    searchRoot.find("**/ears-short").removeNode()
                else:
                    searchRoot.find("**/ears-short").hide()
            elif copy:
                searchRoot.find("**/ears-long").removeNode()
            else:
                searchRoot.find("**/ears-long").hide()
        if animalType != "rabbit":
            if copy:
                searchRoot.find("**/eyes-long").removeNode()
            else:
                searchRoot.find("**/eyes-long").hide()
        if animalType != "dog":
            if copy:
                searchRoot.find("**/joint_pupilL_long").removeNode()
                searchRoot.find("**/joint_pupilR_long").removeNode()
            else:
                searchRoot.find("**/joint_pupilL_long").stash()
                searchRoot.find("**/joint_pupilR_long").stash()
        if copy:
            searchRoot.find("**/head-long").removeNode()
            searchRoot.find("**/head-front-long").removeNode()
        else:
            searchRoot.find("**/head-long").hide()
            searchRoot.find("**/head-front-long").hide()
        if animalType != "rabbit":
            muzzleParts = searchRoot.findAllMatches("**/muzzle-short*")
            for partNum in range(0, muzzleParts.getNumPaths()):
                if copy:
                    muzzleParts.getPath(partNum).removeNode()
                else:
                    muzzleParts.getPath(partNum).hide()

        else:
            muzzleParts = searchRoot.findAllMatches("**/muzzle-long*")
            for partNum in range(0, muzzleParts.getNumPaths()):
                if copy:
                    muzzleParts.getPath(partNum).removeNode()
                else:
                    muzzleParts.getPath(partNum).hide()

    def __fixHeadShortShort(self, style, lodName=None, copy=1):
        searchRoot = self if lodName is None else self.find("**/" + str(lodName))
        otherParts = searchRoot.findAllMatches("**/*long*")
        for partNum in range(0, otherParts.getNumPaths()):
            if copy:
                otherParts.getPath(partNum).removeNode()
            else:
                otherParts.getPath(partNum).stash()

    def __blinkOpenEyes(self, task):
        if self.eyelids.getCurrentState().getName() == "closed":
            self.eyelids.request("open")
        r = self.randGen.random()
        t = 0.2 if r < 0.1 else r * 4.0 + 1.0
        taskMgr.doMethodLater(t, self.__blinkCloseEyes, self.__blinkName)
        return Task.done

    def __blinkCloseEyes(self, task):
        if self.eyelids.getCurrentState().getName() != "open":
            taskMgr.doMethodLater(4.0, self.__blinkCloseEyes, self.__blinkName)
        else:
            self.eyelids.request("closed")
            taskMgr.doMethodLater(0.125, self.__blinkOpenEyes, self.__blinkName)
        return Task.done

    def startBlink(self):
        taskMgr.remove(self.__blinkName)
        if self.__eyes:
            self.openEyes()
        taskMgr.doMethodLater(self.randGen.random() * 4.0 + 1, self.__blinkCloseEyes, self.__blinkName)

    def stopBlink(self):
        taskMgr.remove(self.__blinkName)
        if self.__eyes:
            self.eyelids.request("open")

    def closeEyes(self):
        self.eyelids.request("closed")

    def openEyes(self):
        self.eyelids.request("open")

    def surpriseEyes(self):
        self.eyelids.request("surprised")

    def sadEyes(self):
        self.__eyesOpen = ToonHead.EyesSadOpen
        self.__eyesClosed = ToonHead.EyesSadClosed

    def angryEyes(self):
        self.__eyesOpen = ToonHead.EyesAngryOpen
        self.__eyesClosed = ToonHead.EyesAngryClosed

    def normalEyes(self):
        self.__eyesOpen = ToonHead.EyesOpen
        self.__eyesClosed = ToonHead.EyesClosed

    def blinkEyes(self):
        taskMgr.remove(self.__blinkName)
        self.eyelids.request("closed")
        taskMgr.doMethodLater(0.1, self.__blinkOpenEyes, self.__blinkName)

    def __stareAt(self, task):
        frac = 2 * globalClock.getDt()
        reachedTarget = self.__lookHeadAt(self.__stareAtNode, self.__stareAtPoint, frac)
        self.__lookPupilsAt(self.__stareAtNode, self.__stareAtPoint)
        if reachedTarget and self.__stareAtNode is None:
            return Task.done

        return Task.cont

    def doLookAroundToStareAt(self, node, point):
        self.startStareAt(node, point)
        self.startLookAround()

    def startStareAtHeadPoint(self, point):
        self.startStareAt(self, point)

    def startStareAt(self, node, point):
        taskMgr.remove(self.__stareAtName)
        if self.lookAtTrack:
            self.lookAtTrack.finish()
            self.lookAtTrack = None
        self.__stareAtNode = node
        if point is not None:
            self.__stareAtPoint = point
        else:
            self.__stareAtPoint = self.__defaultStarePoint
        self.__stareAtTime = globalClock.getFrameTime()
        taskMgr.add(self.__stareAt, self.__stareAtName)

    def lerpLookAt(self, point, time=1.0, blink=0):
        taskMgr.remove(self.__stareAtName)
        if self.lookAtTrack:
            self.lookAtTrack.finish()
            self.lookAtTrack = None
        lodNames = self.getLODNames()
        if lodNames:
            lodName = lodNames[0]
        else:
            return 0
        head = self.getPart("head", lodName)
        startHpr = head.getHpr()
        startLpupil = self.__lpupil.getPos()
        startRpupil = self.__rpupil.getPos()
        self.__lookHeadAt(None, point, lod=lodName)
        self.__lookPupilsAt(None, point)
        endHpr = head.getHpr()
        endLpupil = self.__lpupil.getPos() * 0.5
        endRpupil = self.__rpupil.getPos() * 0.5
        head.setHpr(startHpr)
        self.__lpupil.setPos(startLpupil)
        self.__rpupil.setPos(startRpupil)
        if startHpr.almostEqual(endHpr, 10):
            return 0
        if blink:
            self.blinkEyes()
        lookToTgt_TimeFraction = 0.2
        lookToTgtTime = time * lookToTgt_TimeFraction
        returnToEyeCenterTime = time - lookToTgtTime - 0.5
        origin = Point3(0, 0, 0)
        blendType = "easeOut"
        self.lookAtTrack = Parallel(
            Sequence(
                LerpPosInterval(self.__lpupil, lookToTgtTime, endLpupil, blendType=blendType),
                Wait(0.5),
                LerpPosInterval(self.__lpupil, returnToEyeCenterTime, origin, blendType=blendType),
            ),
            Sequence(
                LerpPosInterval(self.__rpupil, lookToTgtTime, endRpupil, blendType=blendType),
                Wait(0.5),
                LerpPosInterval(self.__rpupil, returnToEyeCenterTime, origin, blendType=blendType),
            ),
            name=self.__stareAtName,
        )
        for lodName in self.getLODNames():
            head = self.getPart("head", lodName)
            self.lookAtTrack.append(LerpHprInterval(head, time, endHpr, blendType="easeInOut"))

        self.lookAtTrack.start()
        return 1

    def stopStareAt(self):
        self.lerpLookAt(Vec3.forward())

    def stopStareAtNow(self):
        taskMgr.remove(self.__stareAtName)
        if self.lookAtTrack:
            self.lookAtTrack.finish()
            self.lookAtTrack = None
        if self.__lpupil and self.__rpupil:
            self.__setPupilDirection(0, 0)
        for lodName in self.getLODNames():
            head = self.getPart("head", lodName)
            head.setHpr(0, 0, 0)

    def __lookAround(self, task):
        self.findSomethingToLookAt()
        t = self.randGen.random() * 4.0 + 3.0
        taskMgr.doMethodLater(t, self.__lookAround, self.__lookName)
        return Task.done

    def startLookAround(self):
        taskMgr.remove(self.__lookName)
        t = self.randGen.random() * 5.0 + 2.0
        taskMgr.doMethodLater(t, self.__lookAround, self.__lookName)

    def stopLookAround(self):
        taskMgr.remove(self.__lookName)
        self.stopStareAt()

    def stopLookAroundNow(self):
        taskMgr.remove(self.__lookName)
        self.stopStareAtNow()

    def enterEyelidsOff(self):
        pass

    def exitEyelidsOff(self):
        pass

    def enterEyelidsOpen(self):
        if not self.__eyes.isEmpty():
            self.__eyes.setTexture(self.__eyesOpen, 1)
            if self.__eyelashOpen:
                self.__eyelashOpen.show()
            if self.__eyelashClosed:
                self.__eyelashClosed.hide()
            if self.__lod500Eyes:
                self.__lod500Eyes.setTexture(self.__eyesOpen, 1)
            if self.__lod250Eyes:
                self.__lod250Eyes.setTexture(self.__eyesOpen, 1)
            if self.__lpupil:
                self.__lpupil.show()
                self.__rpupil.show()
            if self.__lod500lPupil:
                self.__lod500lPupil.show()
                self.__lod500rPupil.show()
            if self.__lod250lPupil:
                self.__lod250lPupil.show()
                self.__lod250rPupil.show()

    def exitEyelidsOpen(self):
        pass

    def enterEyelidsClosed(self):
        if not self.__eyes.isEmpty() and self.__eyesClosed:
            self.__eyes.setTexture(self.__eyesClosed, 1)
            if self.__eyelashOpen:
                self.__eyelashOpen.hide()
            if self.__eyelashClosed:
                self.__eyelashClosed.show()
            if self.__lod500Eyes:
                self.__lod500Eyes.setTexture(self.__eyesClosed, 1)
            if self.__lod250Eyes:
                self.__lod250Eyes.setTexture(self.__eyesClosed, 1)
            if self.__lpupil:
                self.__lpupil.hide()
                self.__rpupil.hide()
            if self.__lod500lPupil:
                self.__lod500lPupil.hide()
                self.__lod500rPupil.hide()
            if self.__lod250lPupil:
                self.__lod250lPupil.hide()
                self.__lod250rPupil.hide()

    def exitEyelidsClosed(self):
        pass

    def enterEyelidsSurprised(self):
        if not self.__eyes.isEmpty() and ToonHead.EyesSurprised:
            self.__eyes.setTexture(ToonHead.EyesSurprised, 1)
            if self.__eyelashOpen:
                self.__eyelashOpen.hide()
            if self.__eyelashClosed:
                self.__eyelashClosed.hide()
            if self.__lod500Eyes:
                self.__lod500Eyes.setTexture(ToonHead.EyesSurprised, 1)
            if self.__lod250Eyes:
                self.__lod250Eyes.setTexture(ToonHead.EyesSurprised, 1)
            if self.__muzzle:
                self.__muzzle.setTexture(ToonHead.MuzzleSurprised, 1)
            if self.__lpupil:
                self.__lpupil.show()
                self.__rpupil.show()
            if self.__lod500lPupil:
                self.__lod500lPupil.show()
                self.__lod500rPupil.show()
            if self.__lod250lPupil:
                self.__lod250lPupil.show()
                self.__lod250rPupil.show()

    def exitEyelidsSurprised(self):
        if self.__muzzle:
            self.__muzzle.setTexture(ToonHead.Muzzle, 1)

    def setupMuzzles(self, style):
        self.__muzzles = []
        self.__surpriseMuzzles = []
        self.__angryMuzzles = []
        self.__sadMuzzles = []
        self.__smileMuzzles = []
        self.__laughMuzzles = []

        def hideAddNonEmptyItemToList(item, items):
            if not item.isEmpty():
                item.hide()
                items.append(item)

        def hideNonEmptyItem(item):
            if not item.isEmpty():
                item.hide()

        if self.hasLOD():
            for lodName in self.getLODNames():
                animal = style.getAnimal()
                if animal != "dog":
                    muzzle = self.find("**/" + lodName + "/**/muzzle*neutral")
                else:
                    muzzle = self.find("**/" + lodName + "/**/muzzle*")
                    if lodName in ("1000", "500"):
                        filePrefix = DogMuzzleDict[style.head]
                        muzzles = loader.loadModel("phase_3" + filePrefix + lodName)
                        if not self.find("**/" + lodName + "/**/__Actor_head/def_head").isEmpty():
                            muzzles.reparentTo(self.find("**/" + lodName + "/**/__Actor_head/def_head"))
                        else:
                            muzzles.reparentTo(self.find("**/" + lodName + "/**/joint_toHead"))
                surpriseMuzzle = self.find("**/" + lodName + "/**/muzzle*surprise")
                angryMuzzle = self.find("**/" + lodName + "/**/muzzle*angry")
                sadMuzzle = self.find("**/" + lodName + "/**/muzzle*sad")
                smileMuzzle = self.find("**/" + lodName + "/**/muzzle*smile")
                laughMuzzle = self.find("**/" + lodName + "/**/muzzle*laugh")
                self.__muzzles.append(muzzle)
                hideAddNonEmptyItemToList(surpriseMuzzle, self.__surpriseMuzzles)
                hideAddNonEmptyItemToList(angryMuzzle, self.__angryMuzzles)
                hideAddNonEmptyItemToList(sadMuzzle, self.__sadMuzzles)
                hideAddNonEmptyItemToList(smileMuzzle, self.__smileMuzzles)
                hideAddNonEmptyItemToList(laughMuzzle, self.__laughMuzzles)

        else:
            if style.getAnimal() != "dog":
                muzzle = self.find("**/muzzle*neutral")
            else:
                muzzle = self.find("**/muzzle*")
                filePrefix = DogMuzzleDict[style.head]
                muzzles = loader.loadModel("phase_3" + filePrefix + "1000")
                if not self.find("**/def_head").isEmpty():
                    muzzles.reparentTo(self.find("**/def_head"))
                else:
                    muzzles.reparentTo(self.find("**/joint_toHead"))
            surpriseMuzzle = self.find("**/muzzle*surprise")
            angryMuzzle = self.find("**/muzzle*angry")
            sadMuzzle = self.find("**/muzzle*sad")
            smileMuzzle = self.find("**/muzzle*smile")
            laughMuzzle = self.find("**/muzzle*laugh")
            self.__muzzles.append(muzzle)
            hideAddNonEmptyItemToList(surpriseMuzzle, self.__surpriseMuzzles)
            hideAddNonEmptyItemToList(angryMuzzle, self.__angryMuzzles)
            hideAddNonEmptyItemToList(sadMuzzle, self.__sadMuzzles)
            hideAddNonEmptyItemToList(smileMuzzle, self.__smileMuzzles)
            hideAddNonEmptyItemToList(laughMuzzle, self.__laughMuzzles)

    def getMuzzles(self):
        return self.__muzzles

    def getSurpriseMuzzles(self):
        return self.__surpriseMuzzles

    def getAngryMuzzles(self):
        return self.__angryMuzzles

    def getSadMuzzles(self):
        return self.__sadMuzzles

    def getSmileMuzzles(self):
        return self.__smileMuzzles

    def getLaughMuzzles(self):
        return self.__laughMuzzles

    def showNormalMuzzle(self):
        for muzzleNum in range(len(self.__muzzles)):
            self.__muzzles[muzzleNum].show()

    def hideNormalMuzzle(self):
        for muzzleNum in range(len(self.__muzzles)):
            self.__muzzles[muzzleNum].hide()

    def showAngryMuzzle(self):
        for muzzleNum in range(len(self.__angryMuzzles)):
            self.__angryMuzzles[muzzleNum].show()
            self.__muzzles[muzzleNum].hide()

    def hideAngryMuzzle(self):
        for muzzleNum in range(len(self.__angryMuzzles)):
            self.__angryMuzzles[muzzleNum].hide()
            self.__muzzles[muzzleNum].show()

    def showSadMuzzle(self):
        for muzzleNum in range(len(self.__sadMuzzles)):
            self.__sadMuzzles[muzzleNum].show()
            self.__muzzles[muzzleNum].hide()

    def hideSadMuzzle(self):
        for muzzleNum in range(len(self.__sadMuzzles)):
            self.__sadMuzzles[muzzleNum].hide()
            self.__muzzles[muzzleNum].show()

    def showSmileMuzzle(self):
        for muzzleNum in range(len(self.__smileMuzzles)):
            self.__smileMuzzles[muzzleNum].show()
            self.__muzzles[muzzleNum].hide()

    def hideSmileMuzzle(self):
        for muzzleNum in range(len(self.__smileMuzzles)):
            self.__smileMuzzles[muzzleNum].hide()
            self.__muzzles[muzzleNum].show()

    def showLaughMuzzle(self):
        for muzzleNum in range(len(self.__laughMuzzles)):
            self.__laughMuzzles[muzzleNum].show()
            self.__muzzles[muzzleNum].hide()

    def hideLaughMuzzle(self):
        for muzzleNum in range(len(self.__laughMuzzles)):
            self.__laughMuzzles[muzzleNum].hide()
            self.__muzzles[muzzleNum].show()

    def showSurpriseMuzzle(self):
        for muzzleNum in range(len(self.__surpriseMuzzles)):
            self.__surpriseMuzzles[muzzleNum].show()
            self.__muzzles[muzzleNum].hide()

    def hideSurpriseMuzzle(self):
        for muzzleNum in range(len(self.__surpriseMuzzles)):
            self.__surpriseMuzzles[muzzleNum].hide()
            self.__muzzles[muzzleNum].show()
