# MERLIN
**M**inimal  
**E**CL  
**R**esource  
**L**ibrary  
**I** have  
**N**o clue what the last 2 letters could stand for lmao  

### What is this?  
It's an ECL library that aims to make writing custom ECL code easier and more friendly. It needs a `thecl` version from commit `c63c782c0d4ac80b6562c6b679d81ca8e17ddede` or later. Feel free to join the [ZUNcode discord](https://discord.gg/fvPJvHJ) if you need help or want to ask any questions.

### Usage
There are 2 ways to use MERLIN:
- use `#include "merlin/thxx.tecl"`, with `xx` being the game number, for example `th17.tecl` for WBaWC.
- if you'd rather keep MERLIN functions in a separate file, use `#include "merlin/thxxglobals.tecl"` to include only global constant definitions, inline sub definitions, and forward declarations of subs from the compiled `merlin/thxx/merlin.ecl`. Then, simply include the compiled MERLIN with `ecli`.

In both cases, an [ECLMAP](https://github.com/Priw8/eclmap) is loaded automatically.


### Supported games
- th16
- th17
  
most values from 16/17 should work with 13-15 as well.

### Features
Lots of global constants:
- bullet types (like `ET_BUBBLE`)
- bullet colors (`COLOR16_BLUE` for bullets with 16 colors, `COLOR8_BLUE` for 8 colors etc)
- enemy sprites from enemy.anm (`ENM_GIRL_S_BLUE`, `ENM_CIR_RED` etc)
- aura sprites from enemy.anm (`ENM_AURA_S_RED`, `ENM_AURA_L_BLUE` etc)
- things from effect.anm (like `EFF_EXPLODE_LARGE` for boss explosions, but also some particles)
- sound effects, both as file names (`SE_PLST00`) and custom names (`SE_PLAYER_SHOOT`)
- flags for `flagSet` and `flagClear` instructions, like `FLAG_NO_HITBOX`
- items (`ITEM_POWER`, `ITEM_F`...)
- movement modes for instructions such as Move_posTime (`MODE_ACCEL`, `MODE_LINEAR`...)
- math constants like `PI`, `TAU` and also ZUN's magic numbers (`NEG = -999999`, `NEGF = -999999.0f`)
- bullet transformation types (`EX_WAIT`, `EX_ACCEL`...)
- some constants for the transforms, like `BOUNCE_UDL = 7` for defining on which walls the bullet is allowed to bounce
- aim modes for ins_607 (`etAim`)
  
Some subroutines, many of which are inline:
- `@setupNon()`, `@setupCard()` subs to be called before every nonspell/spellcard (the same thing that ZUN copypastes everywhere, reset boss parameters, clear bullets, reset vars etc)
- `@stop()` - waits forever
- `@etOnAuto(int etId, int interval, int n)` - makes the bullet manager `etId` shoot bullets every `interval` frames, and repeat it `n` times. Made with stage design in mind, for boss patterns you should make more complex stuff obviously.
- separate subs for every bullet transform type, so you can do `@etExWait(etId, channel, time)` instead of `etEx(etId, channel, EX_WAIT time, NEG, NEGF, NEGF)`
- `@effCharge(int pnt, int speed)` that allows easily creating more customizable boss appear effects than the ones in default.ecl. There are versions for different colors, like `effChargeGreen`.
- and some other small things, check the library code for details (documentation will be created at some point).

For documentation and examples, visit the website: [documentation](https://priw8.github.io/#s=MERLIN/doc/index).
