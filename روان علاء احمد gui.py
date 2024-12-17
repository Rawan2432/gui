import tkinter as tk
from gtts import gTTS
import os

# إنشاء نافذة الـ GUI
root = tk.Tk()
root.title("Text-to-Speech App")
root.geometry("400x300")

# وظيفة زر "Play" لتحويل النص إلى كلام وتشغيله باستخدام os
def play_text():
    text = entry.get()
    if text:
        tts = gTTS(text=text, lang='ar')  # تحويل النص إلى صوت باللغة العربية
        tts.save("output.mp3")  # حفظ الملف الصوتي
        os.system("start output.mp3")  # تشغيل الصوت باستخدام المشغل الافتراضي (على Windows)

# وظيفة زر "Exit" لإغلاق التطبيق
def exit_app():
    root.quit()

# وظيفة زر "Set" لمسح النص في الـ Entry
def clear_text():
    entry.delete(0, tk.END)

# إضافة واجهة المستخدم
entry = tk.Entry(root, width=40)
entry.pack(pady=20)

# زر "Play" لتشغيل النص كصوت
play_button = tk.Button(root, text="Play", command=play_text)
play_button.pack(pady=10)

# زر "Exit" لإغلاق التطبيق (اللون الأحمر)
exit_button = tk.Button(root, text="Exit", command=exit_app, fg="white", bg="red")
exit_button.pack(pady=10)

# زر "Set" لمسح النص من الـ Entry
set_button = tk.Button(root, text="Set", command=clear_text)
set_button.pack(pady=10)

# بدء التطبيق
root.mainloop()
