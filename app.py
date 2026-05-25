import tkinter as tk
from tkinter import filedialog
import threading

from transcriber import transcribe_audio


# 创建窗口
window = tk.Tk()

window.title("课后反馈助手")

window.geometry("800x600")


# 文本框
text_box = tk.Text(
    window,
    font=("微软雅黑", 12)
)

text_box.pack(
    fill="both",
    expand=True,
    padx=10,
    pady=10
)

def run_transcribe(file_path):

    result = transcribe_audio(file_path)

    text_box.delete("1.0", tk.END)

    text_box.insert(
        tk.END,
        result
    )


# 选择文件
def choose_file():

    file_path = filedialog.askopenfilename(
        filetypes=[
            ("Audio Files", "*.m4a *.mp3 *.wav")
        ]
    )

    if not file_path:
        return

    text_box.delete("1.0", tk.END)

    text_box.insert(
        tk.END,
        "正在转录，请等待...\n"
    )

    # 开线程
    threading.Thread(
        target=run_transcribe,
        args=(file_path,)
    ).start()


# 按钮
button = tk.Button(
    window,
    text="选择录音并转文字",
    command=choose_file,
    height=2,
    font=("微软雅黑", 12)
)

button.pack(pady=10)


# 主循环
window.mainloop()