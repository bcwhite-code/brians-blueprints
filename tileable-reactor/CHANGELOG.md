# Tileable Reactor Blueprint Changelog

Don't update to a new version that is different in the first or second digit while in the process of building the reactor, including extending an existing one with more rows. Though very similar, they are **not** compatible!

## v4.3.2

- Fixed lamps in "+5 rows" blueprint.

## v4.3.1

- Changed water tile to basic "waterfill" instead of "deep waterfill".

## v4.3.0

- First real changes to the design.
- Added a 15th heat-exchanger per reactor. Now 600MW per row.
- Fewer connections between parallel storage tanks.
- Use four tanks in a row (instead of just one) to see if it's over-producing.
- Tested against a 5GW sink including startup, continuous, and "shock" loading.

## v4.2.0

- Compressed each side by one tile near reactors. Heat-pipe is very sensitive to distance so every tile helps.

## v4.1.0

- Some minor cleanup.

## v4.0.0

- Conversion of the original v4 design, with changes.

**Note:** _If the [Waterfill](https://mods.factorio.com/mod/Noxys_Waterfill) mod is not installed, there may be an error displayed when importing the blueprint. It's still possible to use the landfill method even in this situation._

## 1.3.1

- Fixed grid reference point so it'll be consistent between all the layers.

## v1.3.0

- Many small fixes. Thanks.

## v1.2.0

- Manage resources for bot construction.
- Fixed some power lines.
- Added simple steam-power blueprints
