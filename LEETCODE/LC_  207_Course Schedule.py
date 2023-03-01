# medium level
# 23.02.05
# Course Schedule


class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        # 위에 조건이 대문자든 소문자든 상관이 있는 건가? 잘 모르겠군...


        # 아이디어 1 : prerequisites을 건드려서 먼저 순서대로 나열하고 원형으로 도는 게 있느지, 최대 몇 개 할 수 있는지 재보는 걸로...
        # 대충 dfs인데... 왜 아직 dfs를 못하니....

        return


    # test case
    canFinish(2, [[0, 1], [1, 0]])
    canFinish(3, [[2, 3], [1, 2], [0, 1]])
