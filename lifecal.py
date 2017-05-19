import datetime
import math
import numpy as np
import matplotlib.pyplot as plt

class LifeCal(object):
    """ This is LifeCal, documentation pending """
    def __init__(self, birth=datetime.datetime(1980, 1, 1), life_expectancy=80):
        self.birth = birth
        self.life_expectancy = life_expectancy
        self.weeks_alive = self.get_weeks_alive()
        self.expected_weeks_alive = self.get_expected_weeks_alive()
        self.cells = self.spawn_cells()

    def get_birth(self):
        """ Returns birth """
        return self.birth

    def get_life_expectancy(self):
        """ Returns life expectancy """
        return self.life_expectancy

    def get_weeks_alive(self):
        """ Returns number of entire weeks since birth """
        birth = self.get_birth()
        date = datetime.datetime.today()
        return math.floor((date-birth).days / 7)

    def get_expected_weeks_alive(self):
        """ Returns expected amount of weeks a person is alive """
        birth = self.get_birth()
        life_expectancy = self.get_life_expectancy()
        death = birth.replace(birth.year+life_expectancy)
        return math.floor((death-birth).days / 7)

    def spawn_cells(self):
        """ Write some documentation here """
        expectancy = self.get_life_expectancy()
        weeks_alive = self.get_weeks_alive()
        cells = np.zeros((expectancy, 52))
        yrs, w = 0, 0
        for i in range(weeks_alive):
            cells[yrs][w] = 1
            if w == 51:
                w = 0
                yrs += 1
            else:
                w += 1
        return cells

    def get_cells(self):
        """ Returns cells """
        return self.cells

    def show(self):
        """ Plots life calendar """
        plt.matshow(self.get_cells(), origin='lower')
        plt.show()
        return None

    def bokeh_show(self):
        """ !WIP! Plots life calendar with Bokeh """
        from bokeh.charts import HeatMap, show
        p = HeatMap(self.get_cells(), title="Life Calendar")
        show(p)

    def update(self):
        """ Updates cell states and redraws plot """
        pass

if __name__ == "__main__":
    lif = LifeCal()
    lif.show()
