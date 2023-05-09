import os
import time
from multiprocessing import Process


def txt2cache(filename):
    with open(filename, 'r', encoding='utf-8') as cache_data_txt:
        cache_data = cache_data_txt.read()
        cache_data = eval(cache_data)  # exec(command) 同样适用
    return cache_data


def exec_os(cmd_str):
    os.system(cmd_str)


class Process_pro:
    def __init__(self, func_list, args_list):
        self.process_list = []
        for i, args in enumerate(args_list):
            # daemon=True, 父线程结束, 子线程皆强制退出
            if args is None:
                work_p = Process(target=func_list[i], daemon=False)
            else:
                work_p = Process(target=func_list[i], args=args, daemon=False)
            self.process_list.append(work_p)

    def start_all(self):
        for i, work_unit in enumerate(self.process_list):
            print(f'info: Process-{i} is running...')
            work_unit.start()

    def join_all(self):
        for work_unit in self.process_list:
            work_unit.join()


def main():
    cmd_cache = txt2cache('func_list.txt')
    func_list = []
    args_list = []
    for i, cmd in enumerate(cmd_cache):
        print(f'command: {cmd}')
        func_list.append(exec_os)
        args_list.append((cmd, ))
    works = Process_pro(func_list, args_list)
    works.start_all()
    # works.join_all()  # 进程阻塞


if __name__ == '__main__':
    # 等待系统初始化完毕
    time.sleep(60)
    # 切换到当前目录
    os.chdir(os.path.split(os.path.realpath(__file__))[0])
    # 执行
    main()
