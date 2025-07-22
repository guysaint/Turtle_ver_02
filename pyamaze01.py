from pyamaze import maze, COLOR, agent
m = maze(10,10)
#m.CreateMaze(theme=COLOR.light)
m.CreateMaze(loadMaze="maze--2025-07-22--14-52-02.csv")
a=agent(m, filled=True, footprints=True)
m.tracePath({a:m.path})
m.run()
print(m.maze_map)