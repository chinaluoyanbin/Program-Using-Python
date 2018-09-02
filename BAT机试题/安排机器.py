"""
链接：https://www.nowcoder.com/questionTerminal/42e7ff5c5696445ab907caff17fc9e15?orderByHotValue=1&page=1&onlyReference=false
来源：牛客网

小Q的公司最近接到m个任务, 第i个任务需要xi的时间去完成, 难度等级为yi。
小Q拥有n台机器, 每台机器最长工作时间zi, 机器等级wi。
对于一个任务,它只能交由一台机器来完成, 如果安排给它的机器的最长工作时间小于任务需要的时间, 则不能完成,如果完成这个任务将获得200 * xi + 3 * yi收益。
对于一台机器,它一天只能完成一个任务, 如果它的机器等级小于安排给它的任务难度等级, 则不能完成。
小Q想在今天尽可能的去完成任务, 即完成的任务数量最大。如果有多种安排方案,小Q还想找到收益最大的那个方案。小Q需要你来帮助他计算一下。
"""


# 新建一个node类, 用来存放机器的时间和等级以及任务的时间和等级
class node():
    def __init__(self, time, level):
            self.time = time
            self.level = level

while True:
    try:
        # 读取第一行的机器数和任务数
        machineNum, jobNum = map(int, input().split())

        machines = []
        jobs = []
        # 读取每台机器的最大工作时间和机器等级
        for i in range(machineNum):
            time, level = map(int, input().split())
            machine = node(time, level)
            machines.append(machine)
        # 读取每个任务需要的完成时间和任务等级
        for i in range(jobNum):
            time, level = map(int, input().split())
            job = node(time, level)
            jobs.append(job)

        # 根据时间排序
        machines.sort(key=lambda x: (x.time, x.level), reverse=True)
        jobs.sort(key=lambda x: (x.time, x.level), reverse=True)

        profit = 0  # 收益
        count = 0  # 最大能完成的任务数量
        level = [0] * 105  # list的index代表了机器的难度等级，list的val代表了满足等级为index且满足工作时间大于任务时间的机器个数
        j = 0

        # 从时间最长及难度最大的任务开始
        for i in range(jobNum):
            # 统计满足任务条件的机器个数，存放到列表level中
            while j < machineNum and machines[j].time >= jobs[i].time:
                level[machines[j].level] += 1
                j += 1
            for k in range(jobs[i].level, 101):
                if level[k]:
                    count += 1
                    level[k] -= 1
                    profit += jobs[i].time * 200 + jobs[i].level * 3
                    break
        print('%s %s' % (count, profit))
    except:
        break
