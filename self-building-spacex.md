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
* [Noxy's Waterfill](https://mods.factorio.com/mod/Noxys_Waterfill) (required)
* [Stack Combinator](https://mods.factorio.com/mod/stack-combinator) (required)
* [Nanobots](https://mods.factorio.com/mod/Nanobots) (recommended)
* [Moar Radar](https://mods.factorio.com/mod/Moar-Radar) (suggested)

Intall these using the in-game installer so that all the dependencies are also installed.

You'll need the following blueprint books:

**Import blueprint books only AFTER all mods are installed!** (Or things will be missing.)

* [Space Exploration](https://github.com/bcwhite-code/brians-blueprints/releases/tag/self-building-spacex)
* [Self-Building Factory](https://factorioprints.com/view/-MNZWdWosuqr3vtaC2hD)
* [Brian's Trains](https://factorioprints.com/view/-LaIPNgh8f16V8EwXXpW)
* [Brian's Trains (auxilliary)](https://factorioprints.com/view/-M5PZvxZVXEZnmg4V7Hy)

## Configuration:

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

## Build Order:

"Booting up" isn't covered but there are some blueprints in the book to help
out.  I find it easiest to lay a rail grid ghost early and fit the Mall into
one of them (leaving space for incoming rail "stub" track placed off a siding
of the main rail).  Then I just feed the Mall and slowly build it out by hand.
The only things I automate outside the mall are Red Science and Yellow Belts.

Mines aren't included.  Build them by hand using track from the SBF and stations from BT/aux.

* Mall: Use upgrade planner to change yellow chests to wooden.  Place them.  Then reverse the upgrade and leave it pending.  Do the same with red chests.  Later, bots will put everything back in order.  Set refinecy recipe to basic processing (output only methane) until "advanced oil processing" is researched (requires blue science).  Note: The Mall doesn't produce _everything_.  Some things will have to be hand-crafted and dumped into the logistics network via "trash slots" and others will have to be produced in space.
* Home
* Basic Science: Prioritize coal, stone, iron, & copper.  Research Waterfill when some black (military) science appears and add pump to produce some plastic.  Manually move some sulfur (and later: lubricant, sulfuric acid) from the Mall.
* Iron Smelter: Fill in only 1/2 for now.  Fill the rest when waiting for other things.
* Copper Smelter: Same.
* Starter Circuits: This needs blue belts to be functional but that should be coming along by the time you get here.
