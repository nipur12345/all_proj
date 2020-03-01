import tkinter.filedialog
import tkinter
import threading
import time
def btn_s_Click():
    res=tkinter.filedialog.askopenfilename()
    var_s.set(res)
def btn_d_Click():
    res = tkinter.filedialog.asksaveasfilename()
    var_d.set(res)
def copyData(s,d):
    global t_byte,t_byte_copied
    s_s=open(s,'rb')
    s_d=open(d,'wb')
    s_s.seek(0,2)
    t_byte=s_s.tell()
    s_s.seek(0,0)
    while(True):
        data=s_s.read(100)
        if data==b'':
            break
        s_d.write(data)
        s_d.flush()
        t_byte_copied=s_d.tell()
        time.sleep(.001)
    s_d.close()
def check_progress():
    while(True):
        global t_byte,t_byte_copied
        t_p=(t_byte_copied/t_byte)*100
        btn_progress['text']=str(t_p)+"%... Copied"
        if t_p>=100:
            btn_progress['text'] = "Task Completed"
            break
        time.sleep(1)
def btn_copy_Click():
    th_copy=threading.Thread(target=copyData,args=(var_s.get(),var_d.get()))
    th_copy.start()
    time.sleep(.01)
    th_progress=threading.Thread(target=check_progress)
    th_progress.start()
def btn_progress_Click():
    pass
root=tkinter.Tk()
root.minsize(400,400)
lbl_s=tkinter.Label(root,text='Source File:')
lbl_s.grid(row=0,column=0)
var_s=tkinter.StringVar()
txt_s=tkinter.Entry(root,textvariable=var_s,width=50)
txt_s.grid(row=0,column=1)
btn_s=tkinter.Button(root,text="Browse Source",command=btn_s_Click)
btn_s.grid(row=0,column=2)


lbl_d=tkinter.Label(root,text='Dest File:')
lbl_d.grid(row=1,column=0)
var_d=tkinter.StringVar()
txt_d=tkinter.Entry(root,textvariable=var_d,width=50)
txt_d.grid(row=1,column=1)
btn_d=tkinter.Button(root,text="Browse Dest",command=btn_d_Click)
btn_d.grid(row=1,column=2)

btn_copy=tkinter.Button(root,text="Start Copy",command=btn_copy_Click)
btn_copy.grid(row=2,column=0,columnspan=3)
btn_progress=tkinter.Button(root,text="0%",command=btn_progress_Click)
btn_progress.grid(row=3,column=0,columnspan=3)
root.mainloop()