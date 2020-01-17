[title=MERLIN - constants - enemy]
[Back to index](#s=MERLIN/doc/index)  

## Enemy type constants
[requireEclmap=17]
Constants to be used with the [ins=303,17] and [ins=306,17] instructions. The `Type` column determines which instruction should be used: [ins=306,17] for `main` and [ins=303,17] for `sprite`.
[/requireEclmap]

[requireAnm=enemy]
### `enemy.anm`
| Constant                  | Type      | Sprite                | Notes                                    |
|:-------------------------:|:---------:|:---------------------:|:-----------------------------------------|
| `ENM_GIRL_S_BLUE`         | `main`    |[anm=enemy.anm,17,0]  | -                                         |
| `ENM_GIRL_S_RED`          | `main`    |[anm=enemy.anm,17,5]  | -                                         |
| `ENM_GIRL_S_GREEN`        | `main`    |[anm=enemy.anm,17,10] | -                                         |
| `ENM_GIRL_S_YELLOW`       | `main`    |[anm=enemy.anm,17,15] | -                                         |
| `ENM_GIRL_S_BLUE_ALT`     | `main`    |[anm=enemy.anm,17,20] | -                                         |
| `ENM_GIRL_S_RED_ALT`      | `main`    |[anm=enemy.anm,17,25] | -                                         |
| `ENM_GIRL_M_BLUE`         | `main`    |[anm=enemy.anm,17,35] | -                                         |
| `ENM_GIRL_M_RED`          | `main`    |[anm=enemy.anm,17,30] | -                                         |
| `ENM_GIRL_L`              | `main`    |[anm=enemy.anm,17,40] | -                                         |
| `ENM_GIRL_S_DARK_BLUE`    | `main`    |[anm=enemy.anm,17,147]| -                                         |
| `ENM_GIRL_S_DARK_RED`     | `main`    |[anm=enemy.anm,17,152]| -                                         |
| `ENM_GIRL_S_DARK_YELLOW`  | `main`    |[anm=enemy.anm,17,157]| -                                         |
| `ENM_GIRL_S_PURPLE`       | `main`    |[anm=enemy.anm,17,162]| -                                         |
| `ENM_GIRL_L_DARK`         | `main`    |[anm=enemy.anm,17,167]| -                                         |
| `ENM_CIR_RED`             | `sprite`  |[anm=enemy.anm,17,53] | -                                         |
| `ENM_CIR_GREEN`           | `sprite`  |[anm=enemy.anm,17,56] | -                                         |
| `ENM_CIR_BLUE`            | `sprite`  |[anm=enemy.anm,17,59] | -                                         |
| `ENM_CIR_PURPLE`          | `sprite`  |[anm=enemy.anm,17,62] | -                                         |
| `ENM_CIR_RED_FADE`        | `sprite`  |[anm=enemy.anm,17,65] | Has a fade-in animation when spawning.    |
| `ENM_CIR_GREEN_FADE`      | `sprite`  |[anm=enemy.anm,17,68] | Has a fade-in animation when spawning.    |
| `ENM_CIR_BLUE_FADE`       | `sprite`  |[anm=enemy.anm,17,71] | Has a fade-in animation when spawning.    |
| `ENM_CIR_PURPLE_FADE`     | `sprite`  |[anm=enemy.anm,17,74] | Has a fade-in animation when spawning.    |
| `ENM_PHANTOM_RED`         | `sprite`  |[anm=enemy.anm,17,79] | Spawns particles going up.                |
| `ENM_PHANTOM_GREEN`       | `sprite`  |[anm=enemy.anm,17,83] | Spawns particles going up.                |
| `ENM_PHANTOM_BLUE`        | `sprite`  |[anm=enemy.anm,17,87] | Spawns particles going up.                |
| `ENM_PHANTOM_YELLOW`      | `sprite`  |[anm=enemy.anm,17,91] | Spawns particles going up.                |
| `ENM_PHANTOM_RED_FLIP`    | `sprite`  |[anm=enemy.anm,17,80] | Spawns particles going down.              |
| `ENM_PHANTOM_GREEN_FLIP`  | `sprite`  |[anm=enemy.anm,17,84] | Spawns particles going down.              |
| `ENM_PHANTOM_BLUE_FLIP`   | `sprite`  |[anm=enemy.anm,17,88] | Spawns particles going down.              |
| `ENM_PHANTOM_YELLOW_FLIP` | `sprite`  |[anm=enemy.anm,17,92] | Spawns particles going down.              |
| `ENM_GIRL_S_BLUE_GLOW`    | `main`    |[anm=enemy.anm,17,172]|Not available before [game=17]WBaWC[/game].|
| `ENM_GIRL_S_RED_GLOW`     | `main`    |[anm=enemy.anm,17,177]|Not available before [game=17]WBaWC[/game].|
| `ENM_GIRL_S_GREEN_GLOW`   | `main`    |[anm=enemy.anm,17,182]|Not available before [game=17]WBaWC[/game].|
| `ENM_GIRL_S_YELLOW_GLOW`  | `main`    |[anm=enemy.anm,17,187]|Not available before [game=17]WBaWC[/game].|
| `ENM_GIRL_S_BLUE_ALT_GLOW`| `main`    |[anm=enemy.anm,17,192]|Not available before [game=17]WBaWC[/game].|
| `ENM_GIRL_S_RED_ALT_GLOW` | `main`    |[anm=enemy.anm,17,197]|Not available before [game=17]WBaWC[/game].|
| `ENM_GIRL_M_BLUE_GLOW`    | `main`    |[anm=enemy.anm,17,202]|Not available before [game=17]WBaWC[/game].|
| `ENM_GIRL_M_RED_GLOW`     | `main`    |[anm=enemy.anm,17,207]|Not available before [game=17]WBaWC[/game].|
| `ENM_GIRL_L_GLOW`         | `main`    |[anm=enemy.anm,17,212]|Not available before [game=17]WBaWC[/game].|

### `enemyb.anm` ([game=17]WBaWC[/game])
`enemyb.anm` is basically the same as `enemy.anm` - in fact, all constants are the same. The only difference is that some sprites are slightly different.
| Constant                  | Type      | Sprite                | Notes                                    |
|:-------------------------:|:---------:|:---------------------:|:-----------------------------------------|
| `ENM_GIRL_S_BLUE`         | `main`    |[anm=enemyb.anm,17,0]  | -                                         |
| `ENM_GIRL_S_RED`          | `main`    |[anm=enemyb.anm,17,5]  | -                                         |
| `ENM_GIRL_S_GREEN`        | `main`    |[anm=enemyb.anm,17,10] | -                                         |
| `ENM_GIRL_S_YELLOW`       | `main`    |[anm=enemyb.anm,17,15] | -                                         |
| `ENM_GIRL_S_BLUE_ALT`     | `main`    |[anm=enemyb.anm,17,20] | -                                         |
| `ENM_GIRL_S_RED_ALT`      | `main`    |[anm=enemyb.anm,17,25] | -                                         |
| `ENM_GIRL_M_BLUE`         | `main`    |[anm=enemyb.anm,17,35] | -                                         |
| `ENM_GIRL_M_RED`          | `main`    |[anm=enemyb.anm,17,30] | -                                         |
| `ENM_GIRL_L`              | `main`    |[anm=enemyb.anm,17,40] | -                                         |

All other scripts from `enemy.anm` are present as well, but they are unchanged so I decided to not include them in this table.

### Enemy auras from `enemy.anm`
MERLIN also features a whole bunch of enemy aura constants, which are not listed in a table as it would be way too large (and mostly redundant). The auras generally look like this, but with a color effect applied: [anm=enemy.anm,17,93]  
They also come in different sizes. The general naming is `ENM_AURA_<SIZE>_<COLOR>`:
- `<SIZE>` is `S`, `M` or `L`. In general, `S` is meant for `ENM_GIRL_S*`, `M` for `ENM_GIRL_M*` and `L` for `ENM_GIRL_L*`.
- `<COLOR>` is `RED`, `PURPLE`, `BLUE`, `GREEN`, `YELLOW`, `CYAN` and their variations  (normal, light and dark versions exist - for example, there is `RED`, `LIGHTRED` and `DARKRED`).

[/requireAnm]


[Back to index](#s=MERLIN/doc/index)  