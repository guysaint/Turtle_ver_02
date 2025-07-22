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

def wall_following_algorithm(maze_obj):
    
    #특정 방향으로 이동 할 수 있는지 판단
    def can_move_to(from_pos, direction):
    
    
    #현재 위치에서 특정 방향으로 이동했을 때 다음 위치를 반환
    def get_next_position(pos, direction):    
    
    #현재 위치에서 목표지점까지 직진이 가능한지 확인
    def can_go_to_goal_directly():
    
    #오른손 법칙에 따라 이동 방향 결정
    def get_wall_following_direction():

    #목표지점을 향해 직진
    def move_toward_goal():    


#메인 함수

def main():
    m.run()
    print(m.maze_map)

#프로그램 실행
if __name__ =="__main__":
    main()
    




