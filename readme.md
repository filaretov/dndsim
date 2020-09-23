# dndsim

Simulating the conflicts of a city in a D&D 5e game.

## Goal
We are playing a campaign in a huge city based on the premise that we are a guild offering services.
The campaign is more social/political rather than combat-focused. Our DM would like to have many
factions battling for power in a certain part of the map. During our session 0, we discussed
simulating the behaviour of the factions and letting our DM interpret the results into a story,
rather than making him plan the actions of 13 factions across 40 districts every single week (is
there a DM appreciation day? I feel like there should be an international DM appreciation day).

## Overview
- Factions
  - want: districts
  - have: resources
  - exhibit: behaviour (aggressive expansion, castling, neutralizing), preferences (allies and enemies)
- Districts
  - contain: poi (temples, courthouse, businesses, infrastructure)
  - have: crime rates, population density, etc (these might be abstracted away)
  - generate: resources
- Resources
  - law
  - money
  - clergy
  - knowledge
- Behaviour
  - actions: scout, invest
  - randomness

## Concept
The simulation will essentially be an agent-based model. The environment is an undirected graph of
districts. The actual proximity of districts will not be taken into account to begin with. The
agents are factions and their behaviour is based on their preferences and resources. Usually, they
will want to control districts, neutralize enemies and maximize their preferred resource type (or a
combination of types).

One tick duration will probably equal 1 to 3 in-game days. After every tick, a summary of what has
happened should be presented to the user (our DM). In order to keep the summary managable, the
number of events should be kept low. The way I imagine it is that only _some_ of the factions
will act every turn, depending on some criteria --- their resources, behaviour, etc.

Scouting means increasing the amount of influence that can be spent in one tick in a district.

Alright, so, there's no point in having a grid if there's nothing going on in it.

I'm not ever sure we need `mesa` for this. The complexity comes in later.

### Step
There'll probably be three steps:

1. Choose targets --- each faction chooses whether to make a move on a district
2. Make moves --- the moves are executed, conflicts resolved
3. Generate rewards --- each faction gets the rewards from their districts

## Our campaign
In our campaign, there are currently 13 factions and 40 districts.

### Specific notes to keep in mind
- At least one faction doesn't want additional districts, but wants to limit the growth of their enemy faction.

## Example step
- 3 factions are making moves this tick.
- 2 factions are scouting territories (increasing how much influence they can spend at once there)
- 1 faction is spending influence in a district to gain control
- one of the scouting factions and the investing faction have targeted the same district, but that
  doesn't trigger a conflict, because scouting is not an aggressive move
- the investing faction does trigger a conflict

## Changelog

### 2020-09-23
I'm going to abandon `mesa` in favour of my own ABM framework. Mesa has a weird circular dependency in the agents and models --- models hold the information about schedules and agents, but agents also have a reference to the model holding them. That seems a bit weird to me.