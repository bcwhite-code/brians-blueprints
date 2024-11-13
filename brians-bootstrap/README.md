# Brian's Bootstrap

**Now updated for Factorio 2.0!** At the time of this writing, there is no Auto-Research Mod so you have to queue the research manually. It can make Cliff Explosives only if the [I'd like cliff explosives on Nauvis please](https://mods.factorio.com/mod/id-like-cliff-explosives-on-nauvis-please) mod is installed. Note: I've only played through this once (making necessary changes as I went) so there may be errors.

The goal of the "bootstrap" base is to produce all the materials required for [Brian's Trains](https://factorioprints.com/view/-LaIPNgh8f16V8EwXXpW) with mines and smelters in remote locations. The assemblers for creating a personal roboport and construction bots are also present as they make building the train network much easier.

This starter base is built in phases with the items needed earliest being the ones that are constructed first. Some items will need to be crafted manually but, for the most part, any items needed in bulk are being produced by the time they are needed. Those that have already used this once may elect to just lay down the final "Phase #4" blueprint as they already know how it goes together. First-time users should build the phases in order, dropping each new one directly over the last one to expand upon it.

Once the train network is running with the potential to bring huge amounts of various materials into a concentrated area, a more full-featured mall can be built with the output being directly fed into the logistics network. The production capacity created here is intended only to get the larger base going, not to provide for a full expansion.

- Download from [Factorio Prints](https://factorioprints.com/user/RNRy11ePrQRDlqu6AwY4QDQi26l2)
- Download from [GitHub](https://github.com/bcwhite-code/brians-blueprints/releases)
- See [Changelog](./CHANGELOG.md)
- See my other [blueprints](https://github.com/bcwhite-code/brians-blueprints)
- Join the [discussion on Discord](https://discord.gg/hQnsXwpZ8A)

## Construction Order

Here's how to build everything.

### Phase 1

- Place blueprint "B1"
- Add coal to burner-inserters and central chest.
- Add iron and copper ore to the left and right chests, respectively.
- Take iron and copper plates directly from ovens.
- Craft pump, boiler, and steam engine.
- Create power plant and run power to the base.

### Phase 2

- Place blueprint "B2"
- Craft lab.
- Craft 10 red science, put them in the lab, research automation.
- Craft 3 assembly machines and drop them.
- Craft inserters and drop them. Replace burner-inserters.
- Craft the second, auxiliary oven for some extra iron capacity. This one needs to be manually fed with coal when it runs out.
- With iron and copper plates available, craft electric miners.
- Create small mines of coal, iron, and copper.
- With provided yellow belts, bring ore to base and power plant.
- When ore chests are empty, replace them with belted inputs.

### Phase 3

- Place blueprint "B3"
- Split incoming ore belts and run them to new ovens. Stone is optional for now unless walls are needed.
- Drop one oven per lane and fill in belting to feed them. Add power poles.
- Research Logistics. This will slow down belt production so don't rush it.
- Run belts to the start of gear and green circuit factories.
- Manually craft assembly machines and drop them in singles to start gear and green circuit production. Add necessary power poles and inserters to get production flowing.
- Run belts to the next stage where inserters will be built. Some splitters and underground belts will appear unnecessary but allow the fourth phase to be added later.
- Craft assembly machines for basic and long-reach inserter production.
- Add inserters to get things going and wooden chests to store the output.
- Add stone ovens as necessary to increase production of plates; iron is most used here. A larger power plant and increased mining capacity will probably also be needed.
- If you're tired of manually crafting assembly machines, run the belting around to where they are assembled and get that going, too.
- The assembler for repair packs can also build turrets once researched: Just change the recipe and make room in the chest for the new item type.
- Re-place the blueprint to update assembler recipes now that Logistics is available. It's necessary to do this frequently as technologies are researched.
- Craft factories for fast inserters and all yellow-belt parts.
- Increase gear and green circuit production.
- Add the iron & copper plate storage chests so there is no longer a dependency on the phase-2 base for building materials.
- Start researching desired red-science technologies. This can now run continuously since all the other output (plates and yellow belts) is created by the extended factory. Research is not particularly fast.
- Build out the remainder of phase-3 in whatever order is most important: walls, turrets, assembly machines, ovens, etc. Phase-4 can be started once Steel Oven and AM2 production are running.

### Phase 4

- Place blueprint "B4"
- In the early phase-2 base, upgrade the assembly machines to AM2 and install the new Green Science parts. It will use the Yellow Belt production that already exists there but has a chest into which Inserters must be manually moved from where they are produced. Upgrade the main iron oven. Build the Chemical Science factory when you can. Will run about 3.5 science labs. Keep the research going; the [Auto-Research Mod](https://mods.factorio.com/mods/canidae/auto-research) is useful here; just enter them all and select the ingredients being produced:
- Automation 2
- Advanced Material Processing
- Electric Energy Distribution
- Logistics 2
- Advanced Oil Processing
- Logistics Train Network
- Landfill
- Cliff Explosives
- Stack inserter
- Personal Roboport
- Personal Battery (MK2 optional)
- Rail Signals
- Accumulator
- Fluid Wagon
- Advanced Electronics 2 (Processor)
- Change the recipe of the refinery near the Science Labs to be "basic" until Advanced Oil Processing is known, then change it back. Re-placing the blueprint will always set it to "advanced", which is good once you have it so you don't go back to "basic" without noticing.
- Don't place the storage tanks until after the switch to the "advanced" oil processing recipe.
- Place new belting in the middle area that was omitted from the phase-3 blueprint. From there, fill in the base in a clockwise direction following the general flow of material.
- Upgrade original ovens and assembly machines where necessary as production proves to be insufficient.
- Assemblers for red belt parts can be placed but are not generally necessary except for a few long-reach underground belts.
- Ensure that the power plant continues to have sufficient capacity.
- Ensure that the local mines produce enough ore.
- If the storage tanks fill up and cause the refinery to stop, click on them and "delete" all the contents.

If build-out is forced to pause while waiting for some technology to be researched, build the train blueprint and start filling the cars with materials. When it comes time to build the rail network, you'll need all of this.

(It seems that blueprints don't include locked car contents unless built by bots which is not the case here. See the contents [HERE](https://drive.google.com/open?id=1DZEQcGXLN4N6sFbb4xJ1uPskAXNpK2Bf).)

Each car has items for specific uses:

1. Rail Network: These are the I's, U's, and H's of [Brian's Trains](https://factorioprints.com/view/-LaIPNgh8f16V8EwXXpW) and form the main rail network, plus some landfill and cliff explosives to clean the path. Just load these items into personal inventory and let the bots lay it down while you slowly drive the train down the tracks that were just laid.
2. Loop & Stations: Rail, chests, inserters, and belts enough make up the loop and up to four 4-car provider or requester stations (or two 8-car stations). Fluid parts and additional belts are in car #3.
3. Mine: These are the miners, pumps, electrical, and belting necessary to create a remote ore mine or oil field.
4. Whatever: The slots in this car are open making it easy to carry whatever supplies are needed to build a specialized layout such as an iron smelter or a circuit factory. Or weapons for clearing biter nests.

Once the train network starts to provide significant quantities of plates and circuits, grab some more construction bots, craft a few roboports, and lay down a real mall to get through the rest of the game. It should then be possible to destruct this entire thing and really get things going.
