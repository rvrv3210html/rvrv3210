import math
import tkinter as tk
from tkinter import messagebox

# 測試版警告視窗
try:
  messagebox.showwarning("警告", "目前版本為測試版!")
except Exception:
  pass


class RVRV3210ToolApp:

  def __init__(self, root):
    self.root = root
    self.root.title("rvrv3210小工具")

    try:
      window_width = root.winfo_screenwidth()  # 取得螢幕寬度
      window_height = root.winfo_screenheight()  # 取得螢幕高度
      width = window_width
      height = window_height - 200
      left = int((window_width - width) / 2)
      top = int((window_height - height) / 2)
      self.root.geometry(f"{width}x{height}+{left}+{top}")
      root.iconbitmap("rvrv3210小工具.ico")
    except Exception:
      self.root.geometry("800x600")

    self.root.configure(bg="#1abed4")

    # 建立主容器框架
    self.container = tk.Frame(root, bg="#1abed4")
    self.container.pack(fill=tk.BOTH, expand=True)

    # 計時器相關變數
    self.timer_seconds = 0
    self.timer_running = False
    self.timer_job = None

    # 初始化各個頁面
    self.create_index_page()
    self.create_notes_page()
    self.create_computer_page()
    self.create_timer_page()
    self.create_nav_bar()

    # 預設顯示首頁
    self.show_index()

  def show_page(self, page):
    """安全切換頁面，避免崩潰"""
    try:
      for p in [
          self.index_frame,
          self.notes_frame,
          self.computer_frame,
          self.timer_frame,
      ]:
        p.pack_forget()
      page.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
    except Exception as e:
      messagebox.showerror("錯誤", f"切換頁面時發生錯誤: {e}")

  # -------------------- 首頁 (v2) --------------------
  def create_index_page(self):
    try:
      self.index_frame = tk.Frame(self.container, bg="#1abed4")

      title_frame = tk.Frame(self.index_frame, bg="#1abed4")
      title_frame.pack(pady=20)

      tk.Label(
          title_frame,
          text="首頁",
          font=("Arial", 24, "bold"),
          bg="#1abed4",
          fg="#fff",
      ).pack(side=tk.LEFT)
      tk.Label(
          title_frame,
          text="(v2)",
          font=("Arial", 24, "bold"),
          bg="#1abed4",
          fg="yellow",
      ).pack(side=tk.LEFT)

      tk.Frame(self.index_frame, height=2, bg="#fff").pack(fill=tk.X, pady=5)
      tk.Label(
          self.index_frame,
          text="歡迎使用 rvrv3210 小工具 (v2)！\n請透過下方按鈕切換功能。",
          font=("Arial", 14),
          bg="#1abed4",
          fg="#fff",
      ).pack(pady=40)
    except Exception as e:
      pass

  def show_index(self):
    try:
      self.show_page(self.index_frame)
      self.nav_bar.pack(side=tk.BOTTOM, fill=tk.X)
    except Exception:
      pass

  # -------------------- 筆記頁面 --------------------
  def create_notes_page(self):
    try:
      self.notes_frame = tk.Frame(self.container, bg="#1abed4")
      tk.Label(
          self.notes_frame,
          text="筆記",
          font=("Arial", 24, "bold"),
          bg="#1abed4",
          fg="#fff",
      ).pack(pady=10)
      tk.Frame(self.notes_frame, height=2, bg="#fff").pack(fill=tk.X, pady=5)

      self.text_notes = tk.Text(
          self.notes_frame, wrap=tk.WORD, width=40, height=12, bg="#fff"
      )
      self.text_notes.pack(pady=10)

      btn_frame = tk.Frame(self.notes_frame, bg="#1abed4")
      btn_frame.pack(pady=5)

      tk.Button(
          btn_frame,
          text="下載筆記",
          command=self.download_notes,
          bg="#2795ae",
          fg="#fff",
          font=("Arial", 12),
      ).pack(side=tk.LEFT, padx=5)
      tk.Button(
          btn_frame,
          text="返回首頁",
          command=self.show_index,
          bg="#ae2727",
          fg="#fff",
          font=("Arial", 12),
      ).pack(side=tk.LEFT, padx=5)
    except Exception:
      pass

  def show_notes(self):
    try:
      self.show_page(self.notes_frame)
      self.nav_bar.pack(side=tk.BOTTOM, fill=tk.X)
    except Exception:
      pass

  def download_notes(self):
    """下載/儲存筆記功能，加入防崩潰保護"""
    try:
      content = self.text_notes.get("1.0", tk.END).strip()
      if not content:
        messagebox.showwarning("提示", "筆記無文字喔！")
        return
      with open("rvrv3210小工具-筆記.txt", "w", encoding="utf-8") as f:
        f.write(content)
      messagebox.showinfo("成功", "筆記已成功儲存為 'rvrv3210小工具-筆記.txt'")
    except Exception as e:
      messagebox.showerror("錯誤", f"儲存筆記時發生錯誤: {e}")

  # -------------------- 計算機頁面 --------------------
  def create_computer_page(self):
    try:
      self.computer_frame = tk.Frame(self.container, bg="#1abed4")

      tk.Label(
          self.computer_frame,
          text="計算機",
          font=("Arial", 20, "bold"),
          bg="#1abed4",
          fg="#fff",
      ).pack(pady=5)
      tk.Frame(self.computer_frame, height=2, bg="#fff").pack(fill=tk.X, pady=2)

      comp_body = tk.Frame(self.computer_frame, bg="#2c3e50", padx=10, pady=10)
      comp_body.pack(pady=5)

      # 顯示框
      self.calc_display = tk.Entry(
          comp_body,
          font=("Arial", 20),
          bg="#1e1e1e",
          fg="#00ffcc",
          insertbackground="#00ffcc",
          justify="right",
      )
      self.calc_display.grid(
          row=0, column=0, columnspan=6, sticky="ew", pady=(0, 10)
      )

      # 按鈕配置
      buttons = [
          ("1", 1, 0),
          ("2", 1, 1),
          ("3", 1, 2),
          ("+", 1, 3),
          ("ⁿ√x", 1, 4),
          ("e", 1, 5),
          ("4", 2, 0),
          ("5", 2, 1),
          ("6", 2, 2),
          ("-", 2, 3),
          ("xʸ", 2, 4),
          ("±", 2, 5),
          ("7", 3, 0),
          ("8", 3, 1),
          ("9", 3, 2),
          ("×", 3, 3),
          (".", 3, 4),
          ("0", 3, 5),
          ("⌫", 4, 0),
          ("÷", 4, 1),
          ("(", 4, 2),
          (")", 4, 3),
          ("C", 4, 4),
          ("%", 4, 5),
      ]

      for (text, r, c) in buttons:
        btn = tk.Button(
            comp_body,
            text=text,
            font=("Arial", 12, "bold"),
            bg="#34495e",
            fg="#fff",
            activebackground="#1abc9c",
            command=lambda t=text: self.press_calc(t),
        )
        btn.grid(row=r, column=c, padx=3, pady=3, sticky="nsew")

      # 底部特殊功能按鈕
      tk.Button(
          comp_body,
          text="=",
          font=("Arial", 14, "bold"),
          bg="#27ae60",
          fg="#fff",
          command=self.calculate_result,
      ).grid(row=5, column=0, columnspan=3, sticky="nsew", padx=3, pady=3)
      tk.Button(
          comp_body,
          text="教學",
          font=("Arial", 14, "bold"),
          bg="#2980b9",
          fg="#fff",
          command=self.teaching,
      ).grid(row=5, column=3, columnspan=3, sticky="nsew", padx=3, pady=3)

      tk.Button(
          comp_body,
          text="返回首頁",
          font=("Arial", 12),
          bg="#ae2727",
          fg="#fff",
          command=self.show_index,
      ).grid(row=6, column=0, columnspan=6, sticky="nsew", padx=3, pady=3)
      tk.Button(
          comp_body,
          text="其他小工具",
          font=("Arial", 12),
          bg="#2730ae",
          fg="#fff",
          state=tk.DISABLED,
      ).grid(row=7, column=0, columnspan=6, sticky="nsew", padx=3, pady=3)

      tk.Button(
          comp_body,
          text="筆記",
          font=("Arial", 12),
          bg="#2795ae",
          fg="#fff",
          command=self.show_notes,
      ).grid(row=8, column=0, columnspan=3, sticky="nsew", padx=3, pady=3)
      tk.Button(
          comp_body,
          text="計時器",
          font=("Arial", 12),
          bg="#2795ae",
          fg="#fff",
          command=self.show_timer,
      ).grid(row=8, column=3, columnspan=3, sticky="nsew", padx=3, pady=3)
    except Exception:
      pass

  def show_computer(self):
    try:
      self.show_page(self.computer_frame)
      self.nav_bar.pack_forget()
    except Exception:
      pass

  def press_calc(self, value):
    """計算機按鈕點擊處理（帶防崩潰保護）"""
    try:
      current_pos = self.calc_display.index(tk.INSERT)
      if value == "⌫":
        if current_pos > 0:
          self.calc_display.delete(current_pos - 1, current_pos)
      elif value == "C":
        self.calc_display.delete(0, tk.END)
      elif value == "ⁿ√x":
        self.calc_display.insert(current_pos, "√(")
      elif value == "xʸ":
        self.calc_display.insert(current_pos, "**")
      elif value == "±":
        self.toggle_sign()
      elif value == "×":
        self.calc_display.insert(current_pos, "*")
      elif value == "÷":
        self.calc_display.insert(current_pos, "/")
      else:
        self.calc_display.insert(current_pos, value)
    except Exception:
      pass

  def toggle_sign(self):
    """± 符號切換"""
    try:
      val = self.calc_display.get()
      pos = self.calc_display.index(tk.INSERT)
      left = val[:pos]
      right = val[pos:]
      if left.endswith("(-"):
        self.calc_display.delete(pos - 2, pos)
      else:
        self.calc_display.insert(pos, "(-")
        if not right.endswith(")"):
          self.calc_display.insert(pos + 2, ")")
    except Exception:
      pass

  def calculate_result(self):
    """計算結果（使用安全的 eval，並徹底防止崩潰）"""
    try:
      expr = self.calc_display.get()
      import re

      parsed = re.sub(
          r"(\d+)?√\(([^)]+)\)",
          lambda m: f"(({m.group(2)})**(1/{m.group(1) if m.group(1) else 2}))",
          expr,
      )

      allowed_names = {
          "__builtins__": {},
          "math": math,
          "e": math.e,
          "pi": math.pi,
      }
      result = eval(parsed, allowed_names)

      if result is None or not (
          isinstance(result, (int, float)) and math.isfinite(result)
      ):
        self.calc_display.delete(0, tk.END)
        self.calc_display.insert(0, "Error")
      else:
        self.calc_display.delete(0, tk.END)
        self.calc_display.insert(0, str(result))
    except Exception:
      self.calc_display.delete(0, tk.END)
      self.calc_display.insert(0, "Error")

  def teaching(self):
    try:
      messagebox.showinfo(
          "教學模式",
          "進入教學模式囉\n"
          "1. 因為是Python寫的，運算邏輯與JS雷同。\n"
          "2. 按了 xʸ 會出現 ** (代表次方)。\n"
          "3. e 的用法代表數學常數。\n"
          "4. 任何錯誤都會顯示 Error，不會導致程式崩潰！",
      )
    except Exception:
      pass

  # -------------------- 計時器 (碼表) 頁面 --------------------
  def create_timer_page(self):
    try:
      self.timer_frame = tk.Frame(self.container, bg="#1abed4")
      tk.Label(
          self.timer_frame,
          text="計時器",
          font=("Arial", 24, "bold"),
          bg="#1abed4",
          fg="#fff",
      ).pack(pady=10)
      tk.Frame(self.timer_frame, height=2, bg="#fff").pack(fill=tk.X, pady=5)

      # 碼表顯示框
      self.timer_display_lbl = tk.Label(
          self.timer_frame,
          text="00:00:00",
          font=("Courier", 32, "bold"),
          bg="#222",
          fg="#fff",
          padx=20,
          pady=15,
      )
      self.timer_display_lbl.pack(pady=20)

      # 計時器控制按鈕群組
      btn_box = tk.Frame(self.timer_frame, bg="#1abed4")
      btn_box.pack(pady=10)

      tk.Button(
          btn_box,
          text="開始",
          command=self.start_timer,
          bg="#27ae60",
          fg="white",
          font=("Arial", 14),
          padx=10,
          pady=5,
      ).pack(side=tk.LEFT, padx=5)
      tk.Button(
          btn_box,
          text="暫停",
          command=self.pause_timer,
          bg="#f39c12",
          fg="white",
          font=("Arial", 14),
          padx=10,
          pady=5,
      ).pack(side=tk.LEFT, padx=5)
      tk.Button(
          btn_box,
          text="歸零",
          command=self.reset_timer,
          bg="#c0392b",
          fg="white",
          font=("Arial", 14),
          padx=10,
          pady=5,
      ).pack(side=tk.LEFT, padx=5)

      tk.Button(
          self.timer_frame,
          text="返回首頁",
          command=self.show_index,
          bg="#ae2727",
          fg="white",
          font=("Arial", 14),
          padx=10,
          pady=5,
      ).pack(pady=15)
    except Exception:
      pass

  def format_time(self, seconds):
    try:
      hrs = str(seconds // 3600).zfill(2)
      mins = str((seconds % 3600) // 60).zfill(2)
      secs = str(seconds % 60).zfill(2)
      return f"{hrs}:{mins}:{secs}"
    except Exception:
      return "00:00:00"

  def start_timer(self):
    try:
      if not self.timer_running:
        self.timer_running = True
        self.run_timer_tick()
    except Exception:
      pass

  def run_timer_tick(self):
    try:
      if self.timer_running:
        self.timer_seconds += 1
        self.timer_display_lbl.config(
            text=self.format_time(self.timer_seconds)
        )
        self.timer_job = self.root.after(1000, self.run_timer_tick)
    except Exception:
      pass

  def pause_timer(self):
    try:
      self.timer_running = False
      if self.timer_job:
        self.root.after_cancel(self.timer_job)
        self.timer_job = None
    except Exception:
      pass

  def reset_timer(self):
    try:
      self.pause_timer()
      self.timer_seconds = 0
      self.timer_display_lbl.config(text=self.format_time(self.timer_seconds))
    except Exception:
      pass

  def show_timer(self):
    try:
      self.show_page(self.timer_frame)
      self.nav_bar.pack_forget()
    except Exception:
      pass

  # -------------------- 底部切換導覽列 --------------------
  def create_nav_bar(self):
    try:
      self.nav_bar = tk.Frame(self.root, bg="#1abed4")
      tk.Button(
          self.nav_bar,
          text="筆記",
          command=self.show_notes,
          bg="#2795ae",
          fg="#fff",
          font=("Arial", 12),
      ).pack(side=tk.LEFT, expand=True, fill=tk.X, padx=2, pady=5)
      tk.Button(
          self.nav_bar,
          text="計算機",
          command=self.show_computer,
          bg="#2795ae",
          fg="#fff",
          font=("Arial", 12),
      ).pack(side=tk.LEFT, expand=True, fill=tk.X, padx=2, pady=5)
      tk.Button(
          self.nav_bar,
          text="計時器(碼表)",
          command=self.show_timer,
          bg="#2795ae",
          fg="#fff",
          font=("Arial", 12),
      ).pack(side=tk.LEFT, expand=True, fill=tk.X, padx=2, pady=5)
    except Exception:
      pass


if __name__ == "__main__":
  try:
    root = tk.Tk()
    app = RVRV3210ToolApp(root)
    root.mainloop()
  except Exception as e:
    print(f"程式發生嚴重例外: {e}")