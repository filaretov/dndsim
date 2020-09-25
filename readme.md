# dndsim

Simulating the conflicts of a city in a D&D 5e game.


## Changelog

### 2020-09-23
I'm going to abandon `mesa` in favour of my own ABM framework. Mesa has a weird circular dependency in the agents and models --- models hold the information about schedules and agents, but agents also have a reference to the model holding them. That seems a bit weird to me.
