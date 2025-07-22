from pyamaze import maze, COLOR, agent
m = maze(10,10)
m.CreateMaze(theme=COLOR,white)
m.CreateMaze(loadMaze=maze--2025-07-22--14-52-02.csv)
a=agent(m, shape='arrow', footprints=True)
m.run()