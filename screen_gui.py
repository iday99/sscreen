import tkinter as tk
import subprocess

# 切换显示模式的函数
def set_display_mode(mode):
    cmd_map = {
        'extend': ('DisplaySwitch.exe /extend', '已切换为扩展模式'),
        'clone': ('DisplaySwitch.exe /clone', '已切换为复制模式'),
        'internal': ('DisplaySwitch.exe /internal', '已切换为仅主屏'),
        'external': ('DisplaySwitch.exe /external', '已切换为仅外接'),
    }
    if mode in cmd_map:
        cmd, msg = cmd_map[mode]
        try:
            subprocess.run(cmd, shell=True, check=True)
            status_var.set(msg)
        except subprocess.CalledProcessError:
            status_var.set('切换失败，请以管理员身份运行')
    else:
        status_var.set('未知模式')

# 创建主窗口
root = tk.Tk()
root.title('多显示器模式切换工具')
root.geometry('300x200')

status_var = tk.StringVar()
status_var.set('请选择显示模式')

# 按钮
btn_extend = tk.Button(root, text='扩展模式', width=15, command=lambda: set_display_mode('extend'))
btn_clone = tk.Button(root, text='复制模式', width=15, command=lambda: set_display_mode('clone'))
btn_internal = tk.Button(root, text='仅主屏', width=15, command=lambda: set_display_mode('internal'))
btn_external = tk.Button(root, text='仅外接', width=15, command=lambda: set_display_mode('external'))

# 布局
btn_extend.pack(pady=5)
btn_clone.pack(pady=5)
btn_internal.pack(pady=5)
btn_external.pack(pady=5)

status_label = tk.Label(root, textvariable=status_var, fg='blue')
status_label.pack(pady=10)

root.mainloop() 