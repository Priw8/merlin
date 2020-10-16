[title=MERLIN - constants - misc. bullet-related]
[Back to index](#s=MERLIN/doc/index)  

## Various other bullet constants

### Walls for `etExBounce` and `etExWrap` transformations
The constant can be combined by using the bitwise OR operator in order to allow bouncing on multiple walls (e.g. `BOUNCE_U | BOUNCE_L`). You can also use the combined constants (not listed in this table to keep it small) such as `BOUNCE_UL` for up and left. There is a constant for every possible combination of walls, but keep in mind that the letters must be given in the same order as the constant appear in the table (`UDLR`), for example `BOUNCE_UDR`.
| Constant        | Function                             |
|:---------------:|:-------------------------------------|
|`BOUNCE_U`       | Allow bouncing from the top wall.    |
|`BOUNCE_D`       | Allow bouncing from the bottom wall. |
|`BOUNCE_L`       | Allow bouncing from the left wall.   |
|`BOUNCE_R`       | Allow bouncing from the right wall.  |

### Aim modes
For more detailed explanations of aim modes, refer to the [ECL tutorial](#b=ecl-tutorial/&p=1).
| Constant        | Function                                                    |
|:---------------:|:------------------------------------------------------------|
|`AIM_AT`         | Fan aimed at the player. The default mode (0).              |
|`AIM_ST`         | Fan aimed statically. Aim mode 1.                           |
|`AIM_AT_RING`    | Ring aimed at the player. Aim mode 2.                       |
|`AIM_ST_RING`    | Ring aimed statically. Aim mode 3.                          |
|`AIM_AWAY_RING`  | Ring aimed away from the player. Aim mode 4.                |
|`AIM_ST_RING2`   | Ring aimed statically away. Aim mode 5.                     |
|`AIM_RAND`       | Fan with randomized angles. Aim mode 6.                     |
|`AIM_RAND_RING`  | Ring with randomized speeds. Aim mode 7.                    |
|`AIM_MEEK`       | Full randomization. Aim mode 8.                             |
|`AIM_AT_PYRAMID` | Pyramid aimed at the player. Aim mode 9.                    |
|`AIM_ST_PYRAMID` | Pyramid aimed statically. Aim mode 10.                      |
|`AIM_AT_PEANUT`  | Peanut aimed at the player. Aim mode 11.                    |
|`AIM_ST_PEANUT`  | Peanut aimed statically. Aim mode 12.                       |

[Back to index](#s=MERLIN/doc/index)  