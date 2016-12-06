# !C:\Python27\python.exe
# -*- coding:UTF-8 -*-

import tkinter
# http://wiki.python.org/moin/TkInter
# windows下python3.2版本之后是自动安装tkinter的，python3.3的引入方式为

# 直接测试模块是否可用
# tkinter._test()


def center_window(w=300, h=200):
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)
    root.geometry("%dx%d+%d+%d" % (w, h, x, y))

# 显示一个窗体
root = tkinter.Tk(className='python gui')
center_window(844, 588)
root.mainloop()
