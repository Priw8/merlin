import os
import re

retIndex = "[Back to index](#s=MERLIN/doc/index)  "

lines = [
    "<!-- This file is autogenerated with sfx-gen.py -->",
    "[title=MERLIN - sound effect constants]",
    retIndex,
    "## MERLIN - sound effect constants",
    "Constants to be used with sound-related instructions.  ",
    "Note: Previews may differ than the actual ingame sounds in terms of volume. In fact, the game has multiple copies of the some sounds on different IDs, with varying volume.  ",
    "Note2: \"Since game\" refers to MERLIN versions, not in which game the sound actually appeared first.  ",

    "| ID | Preview | Name | Name (alt) | Notes |",
    "|:--:|:-------:|:----:|:----------:|:-----:|"
]

class globalMap:
    def __init__(self, txt, ver, vername):
        self.ver = ver
        self.vername = vername
        self.parse(txt)
        
    def parse(self, txt):
        self.globals = []
        lines = txt.split("\n")
        for line in lines:
            m = re.match(r"global (.*?) = (.*?);", line)
            if (m != None):
                self.globals.append([m.group(1), m.group(2)])

    def get(self, globalName):
        for pair in self.globals:
            if (pair[0] == globalName):
                return pair[1]

    def find(self, globalVal):
        for pair in self.globals:
            if (pair[1] == globalVal):
                return pair[0]

    def findReverse(self, globalVal):
        for pair in reversed(self.globals):
            if (pair[1] == globalVal):
                return pair[0]

    def findAlt(self, globalName):
        val = self.get(globalName)
        alt = self.findReverse(val)
        if (alt != self.find(val)):
            return alt
        else:
            return "-"





globals16 = open("../../merlin/th16/globals/sfx.tecl")
globals17 = open("../../merlin/th17/globals/sfx.tecl")

maps = [globalMap(globals16.read(), 16, "HSiFS"), globalMap(globals17.read(), 17, "WBaWC")]

globals16.close()
globals17.close()

sfxDir = "sfx"

for gmap in maps:
    handledAlts = []
    for pair in gmap.globals:
        name = pair[0]
        if (name in handledAlts):
            continue

        val = pair[1]
        alt = gmap.findAlt(name)
        if (alt != "-"):
            handledAlts.append(alt)
        
        handledAlts.append(name)

        filename = name.lower().rstrip("_") + ".wav"
        player = ""
        if (not os.path.exists(sfxDir + "/" + filename)):
            print("{}: file not found".format(filename))
            player = "Error"
        else:
            player = "<audio controls preload='none'><source src='content/MERLIN/doc/globals/{}/{}' type='audio/wav'></audio>".format(sfxDir, filename)

        lines.append(
            "|{}|{}|`{}`|`{}`|{}".format(val, player, name, alt, "Since [game={}]{}[/game]".format(gmap.ver, gmap.vername))
        )
    

lines.append("  ")
lines.append(retIndex)
out = open("sfx.md", "w")
out.write("\n".join(lines))

out.close()