# Self-Building Space-Exploration

These blueprints are for Space Exploration games using the "self building factory" (SBF) system from my [self-building-factory](https://factorioprints.com/view/-MNZWdWosuqr3vtaC2hD).

These cover a lot of the planetside work but the "space" aspect will generally be omitted because:
 - I don't want to spoil it.
 - I don't use automated construction trains in space.

Join the discussion [on Discord](https://discord.gg/eSt3Qd8D2e).

You'll need the following mods:
* [Space Exploration](https://mods.factorio.com/mod/space-exploration) (required)
* [Merging Chests](https://mods.factorio.com/mod/WideChests) and [Unlimited](https://mods.factorio.com/mod/WideChestsUnlimited) (required)
* [Loader Redux](https://mods.factorio.com/mod/LoaderRedux) (required)
* [Logistic Train Network](https://mods.factorio.com/mod/LogisticTrainNetwork) (required)
* [Ghost Scanner](https://mods.factorio.com/mod/GhostScanner) (required)
* [Stack Combinator](https://mods.factorio.com/mod/stack-combinator) (required)
* [Nanobots](https://mods.factorio.com/mod/Nanobots) (recommended)
* [Noxy's Waterfill](https://mods.factorio.com/mod/Noxys_Waterfill) (recommended)
* [Moar Radar](https://mods.factorio.com/mod/Moar-Radar) (suggested)

Intall these using the in-game installer so that all the dependencies are also installed.

You'll need the following blueprint books:

**Import blueprint books only AFTER all mods are installed!** (Or things will be missing.)

* [Space Exploration](https://github.com/bcwhite-code/brians-blueprints/releases/tag/self-building-spacex)
* [Self-Building Factory](https://factorioprints.com/view/-MNZWdWosuqr3vtaC2hD)
* [Brian's Trains](https://factorioprints.com/view/-LaIPNgh8f16V8EwXXpW)
* [Brian's Trains (auxilliary)](https://factorioprints.com/view/-M5PZvxZVXEZnmg4V7Hy)

## Configuration

During the creation of the initial ("Nauvis") world:

* Increase the size and richness of all ore/oil patches to maximum.
* Change the frequency of  copper and iron to 200%
* Reduce the amount of water, set it to the minimum, or turn it off completely (uncheck).
* Turn off all enemies.  Unless you want to manage that manually.
* Turn off pollution (less calculation == more UPS)
* Cliffs and trees are optional.  I tend to reduce the former and keep the latter.

In the Mod Settings for Startup:

* Merging Chests: Set "Mergable chest" [sic] to "Iron Chest".
* Set "Maximum chest width", "Maximum chest height", and "Maximum chest area" all to 150.
* Set "Inventory size limit" to 1000.
* Set "Whitelist of merged chests" to "1xN Nx1" (reduces memory consumption).
* Waterfill: Set "Waterfillable" to "Everything".

In the Mod Settings for the Map:

* LTN: Enable "Schedule circuit conditions".  The designs still work without this but will sometimes have to wait for the 2-minute timeout.
* Ghost Scanner: Set "Update frequency" to 3600.  Set "Scan Result limit" to 0 (zero).

In the Mod Settings for the Player:

* Uncheck "Factorio Alerts".  Otherwise you'll get a lot of annoying warnings about trains with "missing cargo" and the like.  (It's intentional but the disable-warnings signal is not respected.)

## How to Build

See the [main SBF document for "The Build"](https://docs.google.com/document/d/1b7OT1-h5GWfey4rIVNbMCXX-dMkoWLmcURutqrliLYE/edit#heading=h.qqx59ll9md1) but note the following differences:

* Every rail station is an "[aux](https://factorioprints.com/view/-M5PZvxZVXEZnmg4V7Hy)" station with merged chests.  Merging **must** be done **after** all chests and medium power poles are placed.  For full blocks, this is possible once phase#1 is complete (i.e. when construction is in phase#2).  For quarter-blocks, wait until a delivery for LTN stations happens.  From map view, run the merge tool over the _entire block_ and not just obvious rail stations.  If merging is forgotten, stations will not function but won't "fail" either.  It's safe to merge chests even after deliveries begin.
* Quarter-block blueprints don't use the standard "Construction Site".  They use the "General Construction" version from the "Construction" sub-book of the SBF.  Just place that on the side to line up with the roboports there and turn it on as usual.  Removing it after construction is likely to remove the rail signal there, too, but there's an unconnected one just off from the track to show where it was.  Add it back and remove the unconnected one.

## Build Order

"Booting up" isn't covered but there are some blueprints in the book to help
out.  I find it easiest to lay a rail grid ghost early and fit the Mall into
one of them (leaving space for incoming rail "stub" track placed off a siding
of the main rail).  Then I just feed the Mall and slowly build it out by hand.
The only things I automate outside the mall are Red Science and Yellow Belts.

Mines aren't included.  Build them by hand using track from the SBF and stations from BT/aux.

* Mall: Use upgrade planner to change yellow chests to wooden.  Place them.  Then reverse the upgrade and leave it pending.  Do the same with red chests.  Later, bots will put everything back in order.  Set refinecy recipe to basic processing (output only methane) until "advanced oil processing" is researched (requires blue science).  Note: The Mall doesn't produce _everything_.  Some things will have to be hand-crafted and dumped into the logistics network via "trash slots" and others will have to be produced in space.
* Home: Build beside Mall.
* Basic Science: Build beside mall.  Prioritize coal, stone, iron, & copper.  Beyond red and green sciences, only research what you need!  Research Waterfill when some black (military) science appears and add pump to produce some plastic.  Manually move some sulfur (and later: lubricant, sulfuric acid) from the Mall.
* Iron Smelter: Fill in only 1/2 for now.  Fill the rest when waiting for other things.
* Copper Smelter: Same.
* Starter Circuits: This needs blue belts to be functional but that should be coming along by the time you get here.  Add the blue belts sparingly as created to start green circuit production.  Red circuits have to wait for Plastic and processors will come later once researched and assembler-3s are available.
* Belts: This is the first "quarter block" blueprint.  Downgrade the assemblers to #2 for now.  Just remember when restoring them to _remove_ the gear assemblers and re-place the blueprint so that the module configuration will be restored (even if not populated until later).  Blue-belt production won't start until the Refinery is built.

By this time, science should be approaching construction and logistic bots.
Once they're being produced, connect the Mall to Home and Basic Science and fit
a "Construction Supply" (from the SBF "Construction" sub-book) beside the Mall.
You'll need to research "logistic system" which needs some yellow science and
that needs LDS so will take some time.  Use barrels to shuttle some lubricant
to the Basic Science input.

* Refinery: This can be build with automated construction but be patient as there aren't many bots.  You can manually move the necessary parts from red chests to blue chests (_not_ the steel buffer chests) so the bots don't have to.  First product will be Lubricant; if it stops producing, manually place sulfur to station belts then flush the methane and light oil tanks.
* Steel (electric)
