# MERLIN
**M**inimal  
**E**CL  
**R**esource  
**L**ibrary  
**I** have  
**N**o clue what the last 2 letters could stand for lmao  

### What is this?  
It's an ECL library that aims to make writing custom ECL code easier and more friendly. It is intended to be used with a thecl version that supports global definitions, \#map, \#include and calling subs directly by name (so basically [Nutzer's fork](https://github.com/Nutzer/thtk)).  

### Usage
To use MERLIN, put the folder of the right game version alongside your ECL scripts, and use `#include "merlin/main.ecld"`. If you wish to only use global constants and not pollute your script with other functions, use `#include "merlin/globals/main.ecld"` instead.

### Supported games
Only th16 so far, though I think most values should work in th15 and th17 too.

### Features
Lots of global constants:
- bullet types (like `[ET_BUBBLE]`)
- bullet colors (`[COLOR16_BLUE]` for bullets with 16 colors, `[COLOR8_BLUE]` for 8 colors etc)
- enemy sprites from enemy.anm (`[ENM_GIRL_S_BLUE]`, `[ENM_CIR_RED]` etc)
- aura sprites from enemy.anm (`[ENM_AURA_S_RED]`, `[ENM_AURA_L_BLUE]` etc)
- things from effect.anm (like `[EFF_EXPLODE_LARGE]` for boss explosions, but also some particles)
- sound effects, both as file names (`[SE_PLST00]`) and custom names (`[SE_PLAYER_SHOOT]`)
- flags for setFlag and clearFlag instructions, like `[FLAG_NO_HITBOX]`
- items (`[ITEM_POWER]`, `[ITEM_F]`...)
- movement modes for instructions such as Move_posTime (`[MODE_ACCEL]`, `[MODE_LINEAR]`...)
- math constants like `[PI]`, `[TAU]` and also ZUN's magic numbers (`[NEG] = -999999`, `[NEGF] = -999999.0f`)
- bullet transformation types (`[EX_WAIT]`, `[EX_ACCEL]`...)
- some constants for the transforms, like `[BOUNCE_UDL] = 7` for defining on which walls the bullet is allowed to bounce
- aim modes for ins_607 (Et_setAimMode)
  
Some subroutines:
- `setupNon()`, `setupCard()` subs to be called before every nonspell/spellcard (the same thing that ZUN copypastes everywhere, reset boss parameters, clear bullets, reset vars etc)
- `waitForever()` for well, waiting forever
- `Et_shootAtRate($etId, $interval, $n)` - makes the bullet manager `$etId` shoot bullets every `$interval` frames, and repeat it `$n` times. Made with stage design in mind, for boss patterns you should make more complex stuff obviously.
- separate subs for every bullet transform type, so you can do `Et_exWait($etId, $channel, $time)` instead of `Et_transformPush($etId, $channel, [EX_WAIT] $time, [NEG], [NEGF], [NEGF])`
- `Eff_charge($pnt, $speed)` that allows easily creating more customizable boss appear effects than the ones in default.ecl. There are versions for different colors, like `Eff_charge_green`.
- and some other small things, check `thxx/merlin/ecl/other.ecld` for details.

There are comments in the code, so you can refer to them.

Example ECL code created with MERLIN:  
```cpp
sub Boss() {
	var;
	setBoss(0);
	Move_pos(0.0f, 128.0f);
	setFlag([FLAG_INTANGIBLE]);
	Eff_charge_green(3, 1);
	wait(120);
	clearFlag([FLAG_INTANGIBLE]);
	Anm_select(3);
	Anm_setMain(0, 0);
	setHurtbox(56.0f, 56.0f);
	setHitbox(50.0f, 50.0f);
	call("BossNon1");
	waitForever();
	return();
}

sub BossNon1() {
	var;
	setLife(9400);
	setupNon();
	setNextSub(0, 1700, 2500, "BossCard1");
	setLifeMarker(0, 1700.0f, -24448);
	wait(90);
	call("BossNon1_at");
	waitForever();
	return();
}

sub BossNon1_at() {
	var et n;
	$et = 0;
	Et_create($et);
	Et_setAimMode($et, 3);
	Et_setSpeed($et, 3.1f, 2.7f);
	Et_exDist($et, 0);
	Et_setExSub($et, 2, "BossNon1_at2");
	$n = 0;
	while(1) {
		Et_setAngle($et, %RANDANGLE, 0.0f);
		Et_exSpecialSet($et, 0, 2);
		Et_setCount($et, 34, 2);
		if ($n == 0) {
			Et_setCount($et, 52, 2);
			Et_setSprite($et, [ET_BUTTERFLY], [COLOR8_GREEN]);
			Et_exBounceSet($et, 0, 1, 1, [BOUNCE_U], [NEGF]);
			Et_exAngleSet($et, 0, 2, 0, 1, 5, 0.12f, [NEGF]);
		} else if ($n == 1) {
			Et_setSprite($et, [ET_BUTTERFLY], [COLOR8_BLUE]);
			Et_exBounceSet($et, 0, 1, 1, [BOUNCE_L], [NEGF]);
		} else if ($n == 2) {
			Et_setSprite($et, [ET_BUTTERFLY], [COLOR8_PINK]);
			Et_exBounceSet($et, 0, 1, 1, [BOUNCE_R], [NEGF]);
		}
		$n = $n + 1;
		if ($n > 2) {
			$n = 0;
		}
		Et_shoot($et);
		wait(70);
	}
	return();
}

sub BossNon1_at2() {
	var et;
	$et = 0;
	setFlag([FLAG_INTANGIBLE]);
	Et_create($et);
	Et_setSprite($et, [ET_SHARD], [COLOR16_GREEN]);
	Et_setCount($et, 5, 1);
	Et_setAimMode($et, 1);
	Et_setSpeed($et, 3.0f, 0.0f);
	[MPI1_2] + (%RANDFS*0.17f);
	Et_setAngle($et, [-1.0f], 0.15f);
	Et_transformPush($et, 0, [EX_ACCEL], 120, [NEG], 0.06f, [PI1_2]);
	Et_shoot($et);
	delete();
} 
```
