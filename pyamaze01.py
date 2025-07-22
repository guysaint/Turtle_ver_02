from pyamaze import maze, COLOR, agent
#미로 크기 설정
MAZE_ROWS = 10
MAZE_COLS = 10
m = maze(MAZE_ROWS,MAZE_COLS)
m.CreateMaze(theme=COLOR.light) # 미로 테마 설정
#m.CreateMaze(loadMaze="maze--2025-07-22--14-52-02.csv")
a=agent(m, filled=True, footprints=True)
m.tracePath({a:m.path})
m.run()
#벽 따라가기 알고리즘



#메인 함수

def main():
    m.run()
    print(m.maze_map)

#프로그램 실행
if __name__ =="__main__":
    main()
    




