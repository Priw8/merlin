[title=MERLIN - constants - bullet types]
[Back to index](#s=merlin/doc/index)  

## Bullet type constants

MERLIN defines constants for all bullet types and colors. The table below shows all bullet type constants, and the type of color constant the bullet needs to use. There are a few categories of color constants:
- `COLOR16` - for small bullets, for example: `COLOR16_RED`. Available options are: `BLACK`, `DARKRED`, `RED`, `PURPLE`, `PINK`, `DARKBLUE`, `BLUE`, `DARKCYAN`, `CYAN`, `DARKGREEN`, `GREEN`, `LIME`, `DARKYELLOW`, `YELLOW`, `ORANGE`, `WHITE`.
- `COLOR8` - for large bullets, for example: `COLOR8_RED`. Available options are: `BLACK`, `RED`, `PINK`, `BLUE`, `CYAN`, `GREEN`, `YELLOW`, `WHITE`.
- `COLOR4` - for bubbles only. Available options: `RED`, `BLUE`, `GREEN`, `YELLOW`.
- `COLOR_COIN` - special type for the coin bullets. There is `COLOR_COIN_GOLD`, `SILVER` and `BRONZE`.
- `COLOR_NEG` - for bullet types that only have 1 color. You can also simply use `0` instead of this constant.


| Constant    | Color type    | Sprite      | Notes                        |
|:-----------:|:-------------:|:-----------:|:-----------------------------|
|`ET_PELLET`  |`COLOR16`      | [et=0,1,15] | -                            |
|`ET_PELLET2` |`COLOR16`      | [et=1,1,15] | Uses a different blend mode. |
|`ET_POPCORN` |`COLOR16`      | [et=2,1,15] | -                            |
|`ET_PELLET3` |`COLOR16`      | [et=3,1,15] | -                            |
|`ET_BALL`    |`COLOR16`      | [et=4,1,15] | -                            |
|`ET_BALL2`   |`COLOR16`      | [et=5,1,15] | Uses a different blend mode. |
|`ET_OUTLINE` |`COLOR16`      | [et=6,1,15] | -                            |
|`ET_OUTLINE2`|`COLOR16`      | [et=7,1,15] | Uses a different blend mode. |
|`ET_RICE`    |`COLOR16`      | [et=8,1,15] | -                            |
|`ET_RICE_SPIN`|`COLOR16`     | [et=35,1,15] | Spins.                      |
|`ET_KUNAI`   |`COLOR16`      | [et=9,1,15] | `COLOR16_WHITE` is this instead of white: [et=9,15,15]. You can also use the `COLOR16_SPECIAL` constant to get this weird-looking kunai. |
|`ET_SHARD`   |`COLOR16`      | [et=10,1,15]| -                            |
|`ET_SHARD_SPIN`|`COLOR16`    | [et=36,1,15]| Spins.                       |
|`ET_AMULET`  |`COLOR16`      | [et=11,1,15]| -                            |
|`ET_ARROWHEAD`|`COLOR16`     | [et=12,1,15]| -                            |
|`ET_BULLET`  |`COLOR16`      | [et=13,1,15]| -                            |
|`ET_LASERHEAD`|`COLOR16`     | [et=14,1,15]| -                            |
|`ET_BACTERIA`|`COLOR16`      | [et=15,1,15]| -                            |
|`ET_STAR`    |`COLOR16`      | [et=16,1,15]| Spins clockwise.             |
|`ET_STAR2`   |`COLOR16`      | [et=37,1,15]| Spins counterclockwise.      |
|`ET_COIN`    |`COLOR_COIN`   | [et=17,0,15][et=17,1,15][et=17,2,15]| Use `COLOR_COIN_GOLD`, `SILVER` and `BRONZE` for colors. |
|`ET_DROPLET` |`COLOR16`      | [et=34,1,15]| -                            |
|`ET_LASER`   |`COLOR16`      | [et=38,1,15]| Use for lasers.              |
|`ET_MENTOS`  |`COLOR8`       | [et=18,1,15]| -                            |
|`ET_MENTOS2` |`COLOR8`       | [et=19,1,15]| Uses a different blend mode. |
|`ET_PULSE`   |`COLOR8`       | [et=30,1,15]| Pulses.                      |
|`ET_JELLYBEAN`|`COLOR8`      | [et=20,1,15]| -                            |
|`ET_KNIFE`   |`COLOR8`       | [et=21,1,15]| -                            |
|`ET_BUTTERFLY`|`COLOR8`      | [et=22,1,15]| -                            |
|`ET_BIGSTAR` |`COLOR8`       | [et=23,1,15]| Spins clockwise.             |
|`ET_BIGSTAR2`|`COLOR8`       | [et=24,1,15]| Spins counterclockwise.      |
|`ET_HEART`   |`COLOR8`       | [et=29,1,15]| -                            |
|`ET_ARROW`   |`COLOR8`       | [et=31,1,15]| -                            |
|`ET_REST`    |`COLOR8`       | [et=43,1,15]| -                            |
|`ET_ORB`     |`COLOR8`       | [et=33,1,15]| -                            |
|`ET_BUBBLE`  |`COLOR4`       | [et=32,1,15]| -                            |
|`ET_FIREBALL_RED`    |`COLOR_NEG`    | [et=25,0,15]| Color must be 0.             |
|`ET_FIREBALL_PURPLE` |`COLOR_NEG`    | [et=26,0,15]| Color must be 0.             |
|`ET_FIREBALL_BLUE`   |`COLOR_NEG`    | [et=27,0,15]| Color must be 0.             |
|`ET_FIREBALL_YELLOW` |`COLOR_NEG`    | [et=28,0,15]| Color must be 0.             |
|`ET_NOTE_RED`        |`COLOR_NEG`    | [et=39,0,15]| Color must be 0.             |
|`ET_NOTE_BLUE`       |`COLOR_NEG`    | [et=40,0,15]| Color must be 0.             |
|`ET_NOTE_GREEN`      |`COLOR_NEG`    | [et=41,0,15]| Color must be 0.             |
|`ET_NOTE_PURPLE`     |`COLOR_NEG`    | [et=42,0,15]| Color must be 0.             |


[Back to index](#s=merlin/doc/index)  