from pyamaze import maze, COLOR, agent
m = maze(10,10)
m.CreateMaze(theme=COLOR,white)
m.CreateMaze(saveMaze=True)
m.run()