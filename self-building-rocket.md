# Self-Building Rocket

Okay, maybe not quite.  It takes a surprising amount of time just to get to the point where something can build itself.  My goal was to have to manually lay only the absolute minimum amount of material and then just let it go.  My best time with it is launching a rocket in just under 5h30m... but then I'm always doing tests and validation on the designs.  If you launch, _comment with your time!_

The factory certainly isn't fully optimal in creating its components so there's some waste to be found.  Mostly I chose designs that were "good enough" and easy to lay down.  Many of those designs came from [Nefrum's 1:45 WR video](https://www.youtube.com/watch?v=6ZUckTrmDo8&ab_channel=Nefrums).

It takes a bit of work to get that first robot flying around but then you can just sit back and relax, right?  Not quite.  At that point, it takes a lot of continued effort just to keep this monster fed with power and raw materials.  How you accomplish that is up to you -- I'm not going to provide details.

Questions?  Join the [discussion on Discord](https://discord.gg/Uk42YKA2f2).

### Placing Blueprints

There is a sequence of seven blueprints with each placed _exactly_ over the previous.  Other than a few transitions that require manual changes before the next update, all described in detail, there **must** be no errors when applying the new one.  Any error message about some conflict means a mistake somewhere that will very likely cause problems.  Be careful laying down parts because it's difficult to see what is wrong from the "place blueprint" display.

To make sure everything is correct, always follow these steps:

1. Attempt to re-place the existing blueprint.  If there are conflicts, find them and fix them.  Don't continue until this step can be done without any error messages.  Finding conflicts can be difficult, especially on the larger blueprints as the red coloring indicating the problem can be difficult to see.  It's much more obvious in "map" mode.
1. Perform the upgrade instructions, if any.
1. Advance to the next blueprint and shift-left-click to lay it down over top of any trees or rocks that are in the way.
1. Do an additional (regular) left-click to place it again.  Any error message here means an incomplete upgrade process... or an error in the blueprints themselves (which would mean either the book didn't import properly or I've screwed up).

I've verified the upgrade sequence by laying the blueprints down one after another, only removing the few items that would have to be upgraded by hand in a real game.  You can try the same.

## Setup

Prepare the game:
* Install the [auto-research mod](https://mods.factorio.com/mod/some-autoresearch).  (Unless you know intimately the exact minimum sequence necessary to build a rocket.)

Create a world that has:
* no enemy
* no cliffs
* maximize frequency, size, and richness of all resources except uranium
* reduce water coverage to 25 or 33%

## Step 0: Starting Blocks

This is about getting those first resources from the ore patches and turning them into plates from which important things can be built.

* Put the burner-miner on the iron patch and feed it directly to the stone furnace.  Feed them both with some coal extracted manually from rocks or the coal patch.
* When there is enough iron (plates), make more miners and furnaces, making a line over the iron-ore patch.
* When making miners more quickly, put two on the coal patch and have each feed the other.  They'll each build up 50 coal that you can remove by ctrl-clicking on them.
* Put a miner on the stone patch and have it feed to a wooden chest.
* Put miners and furnaces on the copper-ore patch and have it start making copper.
* Keep everything fed with coal.
* Extend the chain of coal miners to six.

There are example blueprints of all four of these: 8 iron, 6 coal, 4 copper, and 2 stone.  Soon you'll have plenty of resources with which to craft.

* Create a power plant:  2 boilers and 4 steam engines will hold you through the first stage.  It's easiest to assume one electric miner per boiler, even feeding them directly if your coal patch is big enough.
* Craft some yellow belts and basic inserters when you can.
* Find a good place to build the factory.  To test, lay down blueprint #7 with shift-click (to ignore trees & rocks) then lay it a second time in exactly the same place with a regular click.  If there is any error message, that's not a good place to build.  Press ctrl-z to "undo" until the ghosts go away.

Create the research queue.  Under the auto-research menu (shift-T), check "only research queued" and un-select all science types except "red".  Then, set the research order to be:

* logistics
* fast inserters
* steel axe
* advanced material processing
* circuit network
* construction robotics
* electric energy distribution 1
* worker robot speed 2
* inserter capacity bonus 2
* lab research speed 4
* effect transmission
* rocket silo
* mining productivity

## Step 1: Red Science

You'll need 8 (electric) miners of iron-ore, 3 miners of copper-ore, and 2 miners of coal to feed this stage.  Constant-combinators beside the inputs indicates the raw material being taken in.  Note that coal arrives somewhat away from the others.

* Grab all the iron and copper from the furnaces, and refill them with coal from the miners on the coal patch.  Repeat as necessary throughout the build.
* Lay down blueprint #1 so that the arrow points away from your resources in the direction you're going to build.  There may appear to be a lot of empty space and some unnecessary parts but they'll be filled in and used later.  Remove the arrow.
* Craft belts, inserters, and red science (30).
* Run power to the factory.  Craft a science lab and put it next to a power pole.  Put red science into it.
* Fill out the blueprint, starting at the ore inputs.  Craft what is needed and some more red science to keep research going.
* When ready, move the science lab into the blueprint along with some friends.
* Research should now continue on its own.

Available production:
* yellow belts
* gears

Upgrade preparation:
* Bolster your power plant.  The next stage will need 5 boilers and 10 steam engines.

## Step 2: Green Science

You'll need 16 miners of iron-ore and 8 miners of copper-ore.  The 2 miners of coal may continue to be sufficient but keep an eye on it.

* As before, start with the furnaces to get all the materials going for the assemblers to come.
* Fill in everything else.
* When green science starts to flow, go to auto-research (shift-T) and click on the green-science bottle to enable researching those technologies.
* Some excess inserters may collect in the chests.  Feel free to take them.

Available production:
* green circuits

Upgrade preparation:
* The (regular) inserters feeding the science labs need to be upgraded to fast inserters, as does the one leading from the gear assembler to the yellow-belt assembler.
* More power.  The next stage will need a total of 10 boilers and 20 steam engines.

## Step 3: Assemblers and Furnaces.

Another belt of iron-ore fed by 16 miners will be required as well as a belt of stone fed by 1 miner.  Coal will need 4 more miners (now 6).

* Steel production begins here.  Get that going.  There is a place for a second coal feed here but that won't be necessary for a while.
* Get the furnace and assembler production started.
* Increase the number of science labs.

Available production:
* steel
* assembler 2
* steel furnaces
* inserters (limited)

Upgrade preparation:
* More power!  The next stage will need a total of 20 boilers and 40 steam engines (consuming all water from 1 offshore pump). 
* Double the incoming ore capacity everywhere (iron, copper, stone, and coal), up to a maximum of 30 miners for a full yellow belt of ore.  There is a blueprint for a simple 30-miner single belt.
* Upgrade all of the furnaces to steel versions (from the chest).
* Upgrade all of the assemblers to #2s.  Except...
* _Remove_ all the assemblers for red and green science plus the three green-circuit assemblers.  This is the only way for the upgrade to lay down assemblers that will eventually get modules added to them.

## Step 4: Blue Science

No new ore is needed but you will need a pipe of oil (as many pumps as the closest field will allow) and a pipe of water from a single offshore pump.

* Replace the removed green-circuit assemblers.  Everything is assembler-2 from here on.
* If red/green research was not complete, place the assemblers removed as part of the upgrade process.  Otherwise, it can wait.
* Craft three oil refineries and pipe oil to them.  Pipe the output to the tank.  Make sure it's powered.
* Build the mall (pipes, steam engines, and various inserters) and its satellite (belts, undergrounds, and splitters).
* Craft and lay down the chemical factories.  Bring in the coal and water.
* Build the red-circuit factory, starting with its feeds, then the belting down to the blue-science area on which they will collect until needed.
* Build the blue-science area (and anything that was missed) then belt that down to the science labs.
* Enable blue-science research in auto-research.
* If plastic can't be created because of insufficient methane, add the fourth refinery.

Available production:
* pipes (regular and underground)
* inserters (regular, fast, and long)
* belts (regular, underground, and splitter)
* red circuits

Upgrade preparation:
* You can't move on until research competes "construction robotics".  If you have to wait, prepare two more belts of iron (30 miners each).
* If you still have time, you can shift-click place the #5 blueprint and start on the new belting.
* Change all iron chests to red "passive provider" chests.  There should be 10.  You can use the "upgrade" planner to flag them with yellow circles.

## Step 5: Robots!

No new inputs are needed here though this blueprint may need to be dropped multiple times if not everything has been researched at the time of the first drop.

* Connect all the belts to the robot construction area.
* Place yellow and additional red chests (three of each).
* Craft and drop four roboports.
* Place some wood in the lower (assuming ore inputs are on the left) yellow chest.  It has a "wood" filter set.

The indicator of missing components should show only speed and productivity modules.

Available production:
* nothing new

Upgrade preparation:
* Just wait until robots start flying around. (There's always _something_ for them to do.)

## Step 6: Production Capacity

There's nothing more to build _inside the factory_.  There is plenty to build to feed it.

* Full belts of material on all existing inputs.  30 miners each.  Plus...
* 2 belts of iron-ore
* 1 belt of copper-ore
* 1 belt of coal.
* There should be a wooden chest full of steam engines.  Grab them.  Remove the chest when you won't be needing any more.

Then, while waiting for the robots to build everything, it's time to really beef up that power plant.  The full factory peaks at over 230MW of electricity use so you'll need a total of **260** steam engines powered by 130 boilers (hand-crafted) fed by 130 miners to fully power the thing.  Divide them approximately equally among 8 offshore pumps (32 or 33 per pump).  Go to town and build that out while waiting for the robots to finish.

Available production (relevant to the jobs at hand):
* small power poles
* medium power poles
* electric miners
* steam engines
* pumps
* roboports (very slow)

Upgrade preparation:
* Wait until the robots have completed building everything and all furnaces are operational.  You can give the robots a hand if you have time and are feeling generous.  Otherwise, take a well-deserved break.

## Step 7: Rocket Launch!

This blueprint is so much larger than the others, it can actually be difficult to align.  Once it is, bring in:

* 5 full belts of iron-ore
* 9 full belts of copper-ore
* 3 full belts of coal (starting with the one that doesn't feed the furnaces but goes underground to the plastics factory.
* More oil.  More pumpjacks is less important than some fluid pumps along the pipe leading from the oil field to the factory.  After 50 pipe segments, throughput slows down so it's important to have "booster" pumps along the way.

Then enable yellow and purple science research.  There are only a few things to research at that level and you'll have to re-place blueprint #7 after each one to take advantage of that new technology.

Once you've finished supplying all the raw ores, you can (if you feel so inclined) help the robots along by getting those raw ores through the furnaces and then into the factories.  Or just sit back and watch.

Note that even after the Rocket Silo gets placed, it won't start to be filled until robots have delivered the four prod-3 modules to it.  Those extra resources are important.

## Go Fishing

A rocket really shouldn't launch without cargo.  Building a satellite requires parts (and associated research) that aren't available.  Instead, go catch a fish and say "thank you" by sending it into space.

# Blueprint Changelog

Don't update to a new version that is different in the first or second digit while in the process of building the factory. Though very similar, they are **not** compatible!

## V1.1.5
* Restored yet another missing red wire.
* Fixed some logic that stops wasting processors.
* Fixed problem where prod-1 production could be stopped too soon.

## V1.1.4
* Restored missing red wire to rocket silo.

## V1.1.3
* Fixed more missing power wires (only in Step#7).

## V1.1.2
* Fixed missing power wires due to Factorio 1.0->1.1 upgrade of my ghost templates.
  (It's possible I missed some -- please report via Discord if something isn't connected.)

## V1.1.1
* Better iron-stick delivery to purple science.
* Prioritize red circuits to blue-science when purple-science is ahead.
* Removed some underground pipe ghosts in step#3 blueprint.
* _Don't re-apply Stage#7 over Stage#7 of a previous version.  It's fine to apply it over Stage#6, though._

## V1.1.0
* Improved steel availability to blue science.
* Improved performance and reduced waste from beacon assembler.

## V1.0.5
* Added red-circuit cache for purple science.  Filled during build-out and used later.

## V1.0.4
* Added speed modules to sulfur plant.
* Added speed modules to Beacon assembler.
* Closer shutoff of LDS and Processors to reduce waste.
* Added a comment to the silo circuity.
* Added a manually-placed power-pole so Stage#6 can better build small power poles.
* Fixed Stage#4 coal belt that is supposed to be single-lane.

## V 1.0.3
* Fixed bad green wire from yellow science to blue-circuit control.

## V 1.0.2
* Fixed "rocket silo building" signal to not be from the LTN mod.

## V 1.0.1
* Added speed modules to late-game productivity module creation.

## V 1.0.0
* First public release.

## V 0.X
* Design and testing.
