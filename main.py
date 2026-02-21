import tkinter as tk
import random

message = [
    "保持好心情",
    "好好爱自己",
    "期待下一次见面",
    "你是我最想见的人",
    "愿你万事顺意金榜题名",
    "愿你被世界温柔以待",
    "未来的小警察要加油哦",
    "你值得所有的美好",
    "你值得被偏爱与肯定",
    "愿你永远笑得灿烂",
    "放心大胆往前走，我一直在",
    "遇见你是我最大的幸运"
]

bg_colors = ["#C3C7CE","#E2D8DB","#E5DCD2","#C2C9C0","#F0EEE9","#D6B9B3"]

POPUP_COUNT = 800 # 总共要弹出的窗口数量
GENERATE_INTERVAL = 80 # 每个弹窗生成的时间间隔(毫秒),数值越小出现越快
POPUP_DURATION_MIN = 5000 # 每个弹窗显示的最短时间(毫秒)
POPUP_DURATION_MAX = 10000 # 每个弹窗显示的最长时间(毫秒),随机消失

def create_popup(root):
    #随机选择一条祝福语
    msg = random.choice(message)
    #随机选择背景色
    bg = random.choice(bg_colors)
    #随机字体大小(12~16px),增加视觉层次感
    font_size = random.randint(12, 16)

# 创建独立弹窗(Toplevel 类似于窗口)
    popup = tk.Toplevel(root)
    popup.title("love python") #窗口标题
    popup.configure(bg=bg) #设置背景颜色

    # 随机设置弹窗大小
    width = random.randint(190,210)
    height = random.randint(45,55)

    # 获取屏幕尺寸,用于限制弹窗不超过边界
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # 随机生成位置,留出50像素边距,避免贴边
    x = random.randint(50, screen_width - width - 50)
    y = random.randint(50, screen_height - height - 50)

    # 设置窗口大小和位置
    popup.geometry(f"{width}x{height}+{x}+{y}")

    #创建文字标签,居中显示消息
    lable = tk.Label(
        popup,
        text=msg,
        bg=bg, # 背景色与窗口一致
        font=("SimHei",font_size) # 使用黑体,清晰易懂
    )
    lable.pack(expand=True, fill="both") # 自动填充整个窗口

    # 设置一个随机时间后自动关闭该弹窗
    # 使用 after()实现延时销毁
    popup.after(random.randint(POPUP_DURATION_MIN, POPUP_DURATION_MAX), popup.destroy)

if __name__ == "__main__":
    #创建主窗口(不显示,仅作为容器)
    root = tk.Tk()
    root.withdraw()

    # 批量调度弹窗:每隔GENERATE_INTERVAL毫秒创建一个
    for i in range(POPUP_COUNT):
        # 使用 root.after() 延迟执行 create_popup
        # 实现"持续弹出"的动画效果
        root.after(i * GENERATE_INTERVAL, create_popup,root)

    # 启动TK的事件循环,保持程序运行
    root.mainloop()




