# Tileable Reactor, Self-Throttling & Belt-Fed

This was originally [Aeternus's V4 design](https://forums.factorio.com/viewtopic.php?t=60622) but I wanted something that I could _optionally_ use with the [Waterfill](https://mods.factorio.com/mod/Noxys_Waterfill) mod which doesn't allow placement with the same exactness as landfill and thus couldn't fit the pumps from the original design.

This version of his design has the following changes:

- Eight pumps per row (instead of six), set in areas that can be created using the Waterfill (or Pump Anywhere) mod.
- Merged the "steam turbine" blueprints into the "control" and "row" blueprints: Now only one thing to lay down per row (not including waterfill/landfill).
- Increased capacity from additional heat exchangers (now 600MW instead of 560MW per row).
- Changed belting to yellow since it's cheaper and all that is necessary.
- Send fuel up only a single lane on each side to reduce idle resources. Can still feed 750 rows (450TW).
- Added roboports to make it self-building.
- Added logic to reset latches when everything powers on together.
- "Disable" switch is now a "Power On" switch, with red/green indicator lamp.
- Added a 5-row blueprint for faster layout and since a roboport is necessary only every 5 rows.
- Added grid parameters for accurate placement of multiple rows.
- Added pure waterfill and pure landfill blueprints that can be laid down and "filled" in advance.
- Added some solar panels and accumulators to the control section for failsafe recovery. Just disconnect the control section from the main grid and it should be possible to restart the reactor even during an outage.
- Fully compatible with Factorio 1.X.

To use:

1. Find a big area of dry land on which some waterfill can be placed or a big lake (tall and at least 120 tiles wide) on which landfill can be placed.
2. Lay down the waterfill print, or the "control" landfill print making sure there is water where the pumps will go. Fill it. There is only one "waterfill" print -- it's the same for both the control row and additional rows.
3. Lay down the control row.
4. Connect the control room to the main grid to provide power to roboports.
5. Lay down as many additional waterfill/landfill rows as desired. They have a defined grid so, to place a new row, lay it over the existing row, click-hold, and walk in the direction you want it to go. Fill the new tiles with water/land as appropriate.
6. Lay down additional "entities" rows on the waterfill/landfill using the same technique. Use the 5-row version to continue the roboport scaffolding and make the entire thing self-building.
7. (Optional) Lay down concrete underpad blueprint.
8. Build it by providing the necessary parts to the roboports in the control room.
9. Connect **both** turbine sides to the main power grid. They will be independent of the control grid.
10. Remove the large power poles that connect the sides to the center; they're in-line with the control-row roboports. As long as the roboports are left in place, it's best to keep the control room also wired to the main grid but it can be disconnected and run on its own in an emergency.
11. Send in fuel on one belt and collect spent fuel from the other belt. [Brian's Trains](https://factorioprints.com/view/-LaIPNgh8f16V8EwXXpW) are good for this but it's just as easily managed by logistics chests.
12. Turn on the power switch in the control room. The light will change from red to green.

The reactor will start only once fuel has reached all the way down and every row is ready. All reactors will load and run in synchronization.

The control row supplies about 480MW but each additional row will add 600MW of power capacity. (Though see "I Study Nuclear Science" for a nice surprise.)

Additional rows can be added at any time but may stall the reactor (no new fuel inserted) if not done carefully:

1. Lay down blueprint for the new row.
2. Build with either the control area (except the reactors themselves) or all of the power generation first, then the other. Selectively choose what parts to supply to the robots in order to accomplish this.
3. When the control area is finished except for the reactors, manually place the reactors.

The new row will activate with all the others come the next cycle. If the reactors are present before all the logic gets built, fuel cells may be inserted out-of-sync. It will re-synchronize eventually but probably waste fuel until then. To synchronize manually: Turn off the reactor via the main switch and wait for all remaining fuel to finish burning, then immediately turn it back on again. Power generation shouldn't be interrupted by this.

## I Study Nuclear Science

_I love my classes. I got a crazy teacher; he wears dark glasses._

Reactors have a "neighbor bonus". For every directly adjacent (not diagonal) peer, a reactor increases its heat output by another 40MW. Thus, each reactor in a 4-unit square puts out 120MW for a total of 480MW. As soon as the double-row of reactors is continued, each inside square of 4 units now produces 160x4=640MW of heat energy.

This is well documented. What is surprising, though, is that rather than the outside pairs of a double-row supplying less energy than the inside pairs, every reactor appears to produce approximately the average of the group! This is because the reactors sit on a bed of heat pipes that distribute their energy roughly equally among their peers.

Why is this interesting?

Because although the control row generates only 480MW of heat, it has the capability of turning up to 600MW of heat into electricity. When a second row is added providing a total of 480+640=1120MW of heat, every bit of it is converted to electricity because the two rows have a combined 1200MW of conversion capability. In fact, the first three additional rows all add 640MW of electrical capacity because of this idle ability in the control row being able to make use of the extra heat. Beyond three, however, only 600MW is added for every new row.

The end result is a big reactor that generates a sustained, easy-to-calculate 0.6GW per row.

## Origin

_See the original [forum post](https://forums.factorio.com/viewtopic.php?t=60622) for details, reproduced (without images) here:_

Short version:

- Tileable design expandable into infinity as long as terrain permits
- Requires landfilling. Works well with tall but narrow stretches of water.
- Throttled design, reactors will only be active when more steam production is needed.
- Production: 640MW per 4 reactors, 560MW drained by heat exchangers per full row.
- No bots (for logistics). Belts only.

It's been a while! The last reactor design I tried broke with the water barreling not working well anymore - and I wasn't happy with it anyway. So, back to the drawing board!
I've encountered several problems when making nuclear reactors:

- Heat exchangers now need to be close to the reactors. At a not-so-insignificant distance they just never activate anymore, even when the reactors are at 1000 degrees.
- Water supply is continuous and high volume. Steam output is continuous and high volume. Both of these facts limit the amount of piping you can do.

With these limitations the only logical way to make an infinite tileable design is to put the water pumps into the plant themselves. Which means shaping the terrain to fit the design. Yes, landfilling required, but I've tried to keep it manageable by having the water sections close together, near the reactors.

Overview
Image
This overview is of a ~25GW power plant, which is currently handling the bulk of my base's power demands. Fuel is brought in by rail, spent fuel is pushed out by rail. Around the edges there's still a "scaffold" of roboports that I forgot to clear - these were used to have bots build the incremental rows automatically. And place the concrete.

Reactor Controls:
Image
Reactor controls, rather spartan I suppose but they do what they need to.
On the left we have a simple latch that gets set when fuel is inserted, and gets cleared when the reactors eject their spent fuel cells. While the latch is set, the reactor controls get sent a Red signal. This state is signalled by a yellow light.
On the right we have a level based control that gauges steam in the first row's steam tank (which is generally the lowest as it's fed from the bottom row which has slightly less heat available due to the lower neighbour bonus at the edges). While there is sufficient steam, the reactor fuel inserters are blocked by the Red signal, and a Blue light signals this state.
In the middle there's a constant combinator that can be set to manually block the fuel inserters. A Red light signals that state.
Fuel input and Spent Fuel output is also delivered here by red belt. I used red belts since using blue is overkill here. You'd need to require upwards of 1 TW before you'd run into belt capacity issues.

Reactor row:
Image
Reactor design, rather straightforward. Long inserters for spent fuel ejection. These block the fuel inserters as long as any one of them is not able to get rid of that spent fuel cell. Since all of them are synchronized, there should never be a blockage if you have something pack up spent fuel at the end of the belt. The splitters break off a small portion of fuel, and the belts are measured to check if there's sufficient fuel to feed each generator. If not, the entire plant is held until fuel supply is restored. The thought behind this is to ensure that the entire reactor remains synchronized. Every reactor inserts and ejects fuel at the same time. The yellow inserters are set to a stack size of 1.
You can also see the placement of the water pumps here. The basic landfill pattern for this reactor design is: Land - 2 Water - 18 Land - 2 Water - Land. Any lake that's 22 water wide and any length can be used (in vanilla) to make this power plant work.

Heat exchangers:
Image
Just showing the left side, the right side is a mirror image of this. To get around flow limitations, the water pumps are practically glued onto the heat exchangers. The double row of heat pipes is not arbitrary - it's needed to ensure that the final 2 heat exchangers get sufficient heat once the reactors near 850 degrees. Water and heat from the right, as close to the reactor as I could manage it. Steam exits to the left into a large buffer. The buffer is split into 2 sections because flow between the tanks wasn't working when you've got 6 in a row. The first buffer takes steam from the heat exchangers, and should suffice to buffer an entire reactor cycle if the plant is drawing at least 20% of max capacity. The second buffer feeds the turbines and should frankly, never be empty. There are 3 paths from reactor to the steam buffer. This was needed because 2 will run you into flow capacity limits, even with pumps.

Turbines:
Image
Pretty straightforward a triple row of turbines with some interruptions for substations to pull the power. You may notice that the substations from the pumps and the ones touching the turbines do not interconnect. This is by design for players who want to have the reactor controls and steam feeding devices on a separate circuit with backup power in case of black outs, for easier recovery. I've never found it necessary... the only realistic way where the plant could fail, fuel starvation.
If you want to be able to consume slightly more steam then the heat exchangers produce, add one more turbine at the end. The strings posted generate 556MW of power for 560MW of heat exchanger steam production for 640MW reactor energy generation.

Failure modes:

- Overload: Plant produces maximum power, periodically still stalling since the reactors will generate more heat then the turbines can consume. It'll produce the maximum amount of energy the turbines can produce, and as long as the fuel inserters keep working, the plant should operate normally.
- Underload/no load: Plant shuts down once the steam buffer is above the treshold. If the turbines aren't producing power, reactors should stay at around 850 degrees when the fuel cycle ends.
- Fuel starvation: Plant will stop the reactors if there is insufficient fuel to fully fuel all rows. As soon as fuel is resupplied, it'll start working again.
- Spent fuel backup: Plant will stop the reactors if the spent fuel cannot be dropped from the inserter onto the belt. Once all inserters are able to dispose of the spent fuel, reactors will be ready again.
- Water shortage: Does not happen, since the pumps don't need power and are integrated in the design.

Hope this'll be of use to someone. This is a design meant for power-hungry megabases, for loads of more then 1.5GW, with no real upper limit. The tileable design also makes it expandable - power production becoming an issue? Add another row, and you've got 560MW more to play with. There is also some room between the steam tanks and the turbines to add a radar if you want to be able to remotely view your power plant.
One word of warning though: Nuclear power isn't UPS friendly compared to solar. Even idle a big nuclear facility can put a dent into your UPS.
