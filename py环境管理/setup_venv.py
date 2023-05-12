import os


def menu_show():
    print('###-work mode-### ')
    print('0 -- Creating a virtual environment')
    print('1 -- Update all modules')
    print('2 -- Delete all modules')
    mode = int(input('please choose work mode (0-3): '))
    return mode


def main(mode):
    sys_type = os.name
    # creat_venv
    if mode == 0:
        venv_name = input('Name of venv: ')
        inherit = int(input('Select whether to inherit (0 & 1): '))
        if inherit:
            print('inherit base env')
            os.system(f'python -m venv --system-site-packages --copies {venv_name}')
        else:
            print('clear env')
            os.system(f'python -m venv {venv_name}')
        print('over')
    # upgrade_all
    elif mode == 1:
        confirm = int(input('Press 1 to continue: '))
        if confirm == 1:
            os.system('python -m pip install --upgrade pip')
            os.system('pip3 list --outdated')
            os.system('pip-review --local --interactive')
            print('over')
        else:
            print('abandon execution')
    # delete_all
    elif mode == 2:
        confirm = int(input('Press 1 to continue: '))
        if confirm == 1:
            os.system('pip3 freeze>all_pyModules.txt')
            os.system('pip3 uninstall -r all_pyModules.txt -y')
            if sys_type == 'posix':  # linux
                os.system('rm -r all_pyModules.txt')
            elif sys_type == 'nt':  # windows
                os.system('del all_pyModules.txt')
            os.system('pip3 list')
            print('over')
        else:
            print('abandon execution')
    # default
    else:
        mode = int(input('Unspecified mode, please enter again'))
        main(mode)


if __name__ == '__main__':
    # 切换到当前目录
    os.chdir(os.path.split(os.path.realpath(__file__))[0])
    # 选择模式并执行
    use_mode = menu_show()
    main(use_mode)
