from direct.directnotify.DirectNotifyGlobal import *

from toontown.toon import ToonDNA
from toontown.toon.ToonHead import *

LegsAnimDict = {}
TorsoAnimDict = {}
HeadAnimDict = {}

AnimList = (
    ("neutral", "neutral"),
    ("run", "run"),
    ("pushbutton", "press-button"),
    ("throw", "pie-throw"),
    ("wave", "wave"),
    ("cast", "cast"),
    ("hold-bottle", "hold-bottle"),
)
LegDict = {
    "s": "tt_a_chr_dgs_shorts_legs_",
    "m": "tt_a_chr_dgm_shorts_legs_",
    "l": "tt_a_chr_dgl_shorts_legs_",
}
TorsoDict = {
    "ss": "tt_a_chr_dgs_shorts_torso_",
    "ms": "tt_a_chr_dgm_shorts_torso_",
    "ls": "tt_a_chr_dgl_shorts_torso_",
    "sd": "tt_a_chr_dgs_skirt_torso_",
    "md": "tt_a_chr_dgm_skirt_torso_",
    "ld": "tt_a_chr_dgl_skirt_torso_",
}


def compileGlobalAnimList():
    for anim, filename in AnimList:
        for key in LegDict:
            LegsAnimDict.setdefault(key, {})
            file = f"phase_3/models/char/animations/{LegDict[key]}{filename}"
            LegsAnimDict[key][anim] = file
        for key in TorsoDict:
            TorsoAnimDict.setdefault(key, {})
            file = f"phase_3/models/char/animations/{TorsoDict[key]}{filename}"
            TorsoAnimDict[key][anim] = file
        for key in ["dss", "dsl", "dls", "dll"]:
            HeadAnimDict.setdefault(key, {})
            file = f"phase_3/models/char/animations/{HeadDict[key]}{filename}"
            HeadAnimDict[key][anim] = file


class Toon(ToonHead):
    notify = directNotify.newCategory("Toon")
    afkTimeout = ConfigVariableInt("afk-timeout", 600).value
    standWalkRunReverse = None
    isStunned = 0
    style = None

    def __init__(self):
        ToonHead.__init__(self)
        self.rightHands = []
        self.rightHand = None
        self.leftHands = []
        self.leftHand = None
        self.headParts = []
        self.torsoParts = []
        self.hipsParts = []
        self.legsParts = []

    def delete(self):
        self.stop()
        self.rightHands = None
        self.rightHand = None
        self.leftHands = None
        self.leftHand = None
        self.headParts = None
        self.torsoParts = None
        self.hipsParts = None
        self.legsParts = None
        ToonHead.delete(self)

    def updateToonDNA(self, newDNA, fForce=0):
        self.style.gender = newDNA.getGender()
        oldDNA = self.style
        if fForce or newDNA.head != oldDNA.head:
            self.swapToonHead(newDNA.head)
        if fForce or newDNA.torso != oldDNA.torso:
            self.swapToonTorso(newDNA.torso, genClothes=0)
            self.loop("neutral")
        if fForce or newDNA.legs != oldDNA.legs:
            self.swapToonLegs(newDNA.legs)
        self.swapToonColor(newDNA)
        self.__swapToonClothes(newDNA)

    def setDNAString(self, dnaString):
        newDNA = ToonDNA.ToonDNA()
        newDNA.makeFromNetString(dnaString)
        if len(newDNA.torso) < 2:
            newDNA.torso = newDNA.torso + "s"
        self.setDNA(newDNA)

    def setDNA(self, dna):
        if self.style:
            self.updateToonDNA(dna)
        else:
            self.style = dna
            self.generateToon()

    def parentToonParts(self):
        if self.hasLOD():
            for lodName in self.getLODNames():
                if not self.getPart("torso", lodName).find("**/def_head").isEmpty():
                    self.attach("head", "torso", "def_head", lodName)
                else:
                    self.attach("head", "torso", "joint_head", lodName)
                self.attach("torso", "legs", "joint_hips", lodName)
        else:
            self.attach("head", "torso", "joint_head")
            self.attach("torso", "legs", "joint_hips")

    def unparentToonParts(self):
        if self.hasLOD():
            for lodName in self.getLODNames():
                self.getPart("head", lodName).reparentTo(self.getLOD(lodName))
                self.getPart("torso", lodName).reparentTo(self.getLOD(lodName))
                self.getPart("legs", lodName).reparentTo(self.getLOD(lodName))

        else:
            self.getPart("head").reparentTo(self.getGeomNode())
            self.getPart("torso").reparentTo(self.getGeomNode())
            self.getPart("legs").reparentTo(self.getGeomNode())

    def setLODs(self):
        self.setLODNode()
        levelOneIn = ConfigVariableInt("lod1-in", 20).value
        levelOneOut = ConfigVariableInt("lod1-out", 0).value
        levelTwoIn = ConfigVariableInt("lod2-in", 80).value
        levelTwoOut = ConfigVariableInt("lod2-out", 20).value
        levelThreeIn = ConfigVariableInt("lod3-in", 280).value
        levelThreeOut = ConfigVariableInt("lod3-out", 80).value
        self.addLOD(1000, levelOneIn, levelOneOut)
        self.addLOD(500, levelTwoIn, levelTwoOut)
        self.addLOD(250, levelThreeIn, levelThreeOut)

    def generateToon(self):
        self.setLODs()
        self.generateToonLegs()
        self.generateToonHead()
        self.generateToonTorso()
        self.generateToonColor()
        self.parentToonParts()
        self.rescaleToon()
        self.setupToonNodes()

    def setupToonNodes(self):
        rightHand = NodePath("rightHand")
        self.rightHand = None
        self.rightHands = []
        leftHand = NodePath("leftHand")
        self.leftHands = []
        self.leftHand = None
        for lodName in self.getLODNames():
            hand = self.getPart("torso", lodName).find("**/joint_Rhold")
            if not self.getPart("torso", lodName).find("**/def_joint_right_hold").isEmpty():
                hand = self.getPart("torso", lodName).find("**/def_joint_right_hold")
            self.rightHands.append(hand)
            rightHand = rightHand.instanceTo(hand)
            if not self.getPart("torso", lodName).find("**/def_joint_left_hold").isEmpty():
                hand = self.getPart("torso", lodName).find("**/def_joint_left_hold")
            self.leftHands.append(hand)
            leftHand = leftHand.instanceTo(hand)
            if self.rightHand is None:
                self.rightHand = rightHand
            if self.leftHand is None:
                self.leftHand = leftHand

        self.headParts = self.findAllMatches("**/__Actor_head")
        self.legsParts = self.findAllMatches("**/__Actor_legs")
        self.hipsParts = self.legsParts.findAllMatches("**/joint_hips")
        self.torsoParts = self.hipsParts.findAllMatches("**/__Actor_torso")

    def rescaleToon(self):
        animalStyle = self.style.getAnimal()
        bodyScale = ToonBodyScales[animalStyle]
        self.getGeomNode().setScale(bodyScale)

    def getBodyScale(self):
        animalStyle = self.style.getAnimal()
        return ToonBodyScales[animalStyle]

    def generateToonLegs(self, copy=1):
        legStyle = self.style.legs
        filePrefix = LegDict.get(legStyle)
        if filePrefix is None:
            self.notify.error("unknown leg style: %s" % legStyle)
        self.loadModel("phase_3/models/char/" + filePrefix + "1000", "legs", "1000", copy)
        self.loadModel("phase_3/models/char/" + filePrefix + "500", "legs", "500", copy)
        self.loadModel("phase_3/models/char/" + filePrefix + "250", "legs", "250", copy)
        if not copy:
            self.showPart("legs", "1000")
            self.showPart("legs", "500")
            self.showPart("legs", "250")
        self.loadAnims(LegsAnimDict[legStyle], "legs", "1000")
        self.loadAnims(LegsAnimDict[legStyle], "legs", "500")
        self.loadAnims(LegsAnimDict[legStyle], "legs", "250")
        self.findAllMatches("**/boots_short").stash()
        self.findAllMatches("**/boots_long").stash()
        self.findAllMatches("**/shoes").stash()

    def swapToonLegs(self, legStyle, copy=1):
        self.unparentToonParts()
        self.removePart("legs", "1000")
        self.removePart("legs", "500")
        self.removePart("legs", "250")
        self.style.legs = legStyle
        self.generateToonLegs(copy)
        self.generateToonColor()
        self.parentToonParts()
        self.rescaleToon()

    def generateToonTorso(self, copy=1, genClothes=1):
        torsoStyle = self.style.torso
        filePrefix = TorsoDict.get(torsoStyle)
        if filePrefix is None:
            self.notify.error("unknown torso style: %s" % torsoStyle)
        self.loadModel("phase_3/models/char/" + filePrefix + "1000", "torso", "1000", copy)
        self.loadModel("phase_3/models/char/" + filePrefix + "500", "torso", "500", copy)
        self.loadModel("phase_3/models/char/" + filePrefix + "250", "torso", "250", copy)
        if not copy:
            self.showPart("torso", "1000")
            self.showPart("torso", "500")
            self.showPart("torso", "250")
        self.loadAnims(TorsoAnimDict[torsoStyle], "torso", "1000")
        self.loadAnims(TorsoAnimDict[torsoStyle], "torso", "500")
        self.loadAnims(TorsoAnimDict[torsoStyle], "torso", "250")
        if genClothes == 1:
            self.generateToonClothes()

    def swapToonTorso(self, torsoStyle, copy=1, genClothes=1):
        self.unparentToonParts()
        self.removePart("torso", "1000")
        self.removePart("torso", "500")
        self.removePart("torso", "250")
        self.style.torso = torsoStyle
        self.generateToonTorso(copy, genClothes)
        self.generateToonColor()
        self.parentToonParts()
        self.rescaleToon()
        self.setupToonNodes()
        self.generateBackpack()

    def generateToonHead(self, copy=1):
        ToonHead.generateToonHead(self, copy, self.style, ("1000", "500", "250"))
        if self.style.getAnimal() == "dog":
            self.loadAnims(HeadAnimDict[self.style.head], "head", "1000")
            self.loadAnims(HeadAnimDict[self.style.head], "head", "500")
            self.loadAnims(HeadAnimDict[self.style.head], "head", "250")

    def swapToonHead(self, headStyle, copy=1):
        self.stopLookAroundNow()
        self.eyelids.request("open")
        self.unparentToonParts()
        self.removePart("head", "1000")
        self.removePart("head", "500")
        self.removePart("head", "250")
        self.style.head = headStyle
        self.generateToonHead(copy)
        self.generateToonColor()
        self.parentToonParts()
        self.rescaleToon()
        self.eyelids.request("open")
        self.startLookAround()

    def generateToonColor(self):
        ToonHead.generateToonColor(self, self.style)
        armColor = self.style.getArmColor()
        gloveColor = self.style.getGloveColor()
        legColor = self.style.getLegColor()
        for lodName in self.getLODNames():
            torso = self.getPart("torso", lodName)
            for pieceName in ("arms", "neck"):
                piece = torso.find("**/" + pieceName)
                piece.setColor(armColor)

            hands = torso.find("**/hands")
            hands.setColor(gloveColor)
            legs = self.getPart("legs", lodName)
            for pieceName in ("legs", "feet"):
                piece = legs.find("**/%s;+s" % pieceName)
                piece.setColor(legColor)

    def swapToonColor(self, dna):
        self.setStyle(dna)
        self.generateToonColor()

    def __swapToonClothes(self, dna):
        self.setStyle(dna)
        self.generateToonClothes(fromNet=1)

    def generateToonClothes(self, fromNet=0):
        swappedTorso = 0
        if self.hasLOD():
            if self.style.getGender() == "f" and fromNet == 0:
                try:
                    bottomPair = ToonDNA.GirlBottoms[self.style.botTex]
                except IndexError:
                    bottomPair = ToonDNA.GirlBottoms[0]

                if len(self.style.torso) < 2:
                    self.notify.warning(f"Invalid torso: {self.style.torso}")
                    return 0
                if self.style.torso[1] == "s" and bottomPair[1] == ToonDNA.SKIRT:
                    self.swapToonTorso(self.style.torso[0] + "d", genClothes=0)
                    swappedTorso = 1
                elif self.style.torso[1] == "d" and bottomPair[1] == ToonDNA.SHORTS:
                    self.swapToonTorso(self.style.torso[0] + "s", genClothes=0)
                    swappedTorso = 1
            try:
                texName = ToonDNA.Shirts[self.style.topTex]
            except IndexError:
                texName = ToonDNA.Shirts[0]

            shirtTex = loader.loadTexture(texName, okMissing=True)
            if shirtTex is None:
                shirtTex = loader.loadTexture(ToonDNA.Shirts[0])
            shirtTex.setMinfilter(Texture.FTLinearMipmapLinear)
            shirtTex.setMagfilter(Texture.FTLinear)
            try:
                shirtColor = ToonDNA.ClothesColors[self.style.topTexColor]
            except IndexError:
                shirtColor = ToonDNA.ClothesColors[0]

            try:
                texName = ToonDNA.Sleeves[self.style.sleeveTex]
            except IndexError:
                texName = ToonDNA.Sleeves[0]

            sleeveTex = loader.loadTexture(texName, okMissing=True)
            if sleeveTex is None:
                sleeveTex = loader.loadTexture(ToonDNA.Sleeves[0])
            sleeveTex.setMinfilter(Texture.FTLinearMipmapLinear)
            sleeveTex.setMagfilter(Texture.FTLinear)
            try:
                sleeveColor = ToonDNA.ClothesColors[self.style.sleeveTexColor]
            except IndexError:
                sleeveColor = ToonDNA.ClothesColors[0]

            if self.style.getGender() == "m":
                try:
                    texName = ToonDNA.BoyShorts[self.style.botTex]
                except IndexError:
                    texName = ToonDNA.BoyShorts[0]

            else:
                try:
                    texName = ToonDNA.GirlBottoms[self.style.botTex][0]
                except IndexError:
                    texName = ToonDNA.GirlBottoms[0][0]

            bottomTex = loader.loadTexture(texName, okMissing=True)
            if bottomTex is None:
                if self.style.getGender() == "m":
                    bottomTex = loader.loadTexture(ToonDNA.BoyShorts[0])
                else:
                    bottomTex = loader.loadTexture(ToonDNA.GirlBottoms[0][0])
            bottomTex.setMinfilter(Texture.FTLinearMipmapLinear)
            bottomTex.setMagfilter(Texture.FTLinear)
            try:
                bottomColor = ToonDNA.ClothesColors[self.style.botTexColor]
            except IndexError:
                bottomColor = ToonDNA.ClothesColors[0]

            darkBottomColor = bottomColor * 0.5
            darkBottomColor.setW(1.0)
            for lodName in self.getLODNames():
                thisPart = self.getPart("torso", lodName)
                top = thisPart.find("**/torso-top")
                top.setTexture(shirtTex, 1)
                top.setColor(shirtColor)
                sleeves = thisPart.find("**/sleeves")
                sleeves.setTexture(sleeveTex, 1)
                sleeves.setColor(sleeveColor)
                bottoms = thisPart.findAllMatches("**/torso-bot")
                for bottomNum in range(0, bottoms.getNumPaths()):
                    bottom = bottoms.getPath(bottomNum)
                    bottom.setTexture(bottomTex, 1)
                    bottom.setColor(bottomColor)

                caps = thisPart.findAllMatches("**/torso-bot-cap")
                caps.setColor(darkBottomColor)

        return swappedTorso


compileGlobalAnimList()
