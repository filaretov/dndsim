from mesa import Agent, Model
from mesa.time import RandomActivation
from mesa.space import SingleGrid


class FactionAgent(Agent):
    """A faction spends resources to control districts according to their preferences."""

    def __init__(self, uid, model, debug=False) -> None:
        super().__init__(uid, model)
        self.money = 1
        self.debug = debug

    def step(self):
        if self.money == 0:
            return
        other_agent = self.random.choice(self.model.schedule.agents)
        other_agent.money += 1
        self.money -= 1
        if self.debug:
            print(f"Agent {self.unique_id}, {self.money=}")


class QuarterModel(Model):
    """A quarter contains factions battling over districts."""

    def __init__(self, N):
        self.n_factions = N
        self.schedule = RandomActivation(self)
        for i in range(self.n_factions):
            faction = FactionAgent(i, self)
            self.schedule.add(faction)

    def step(self):
        """Advance the model by one step."""
        self.schedule.step()


class Districts:
    def __init__(self, N):
        self.n_districts = N


# legends say that the infamous Thugs 4 Less secretly rule all districts in the Harbour Quarter
