from tkinter import *
import random
import time



normal_mode=False
tk=Tk()
tk.title('')
tk.resizable(0,0)
tk.configure(bg='black')
wd=Frame(tk,bg='black')
window=Frame(wd,bg='black')
if normal_mode:
    window2=Frame(wd,bg='black')
window3=Frame(wd,bg='black')
place_label=Label(window3,bg='black',fg='peru',width=19,height=8)
photo_frame=Canvas(tk,bg='black',width=380,height=395,borderwidth=0,highlightthickness=0)
w1=Label(window,bg='black',fg='yellowgreen',text='O',width=2)
w2=Label(window,bg='black',fg='red',text='O',width=2)
w3=Label(window,bg='black',fg='red',text='O',width=2)
w4=Label(window,bg='black',fg='red',text='O',width=2)
w5=Label(window,bg='black',fg='red',text='O',width=2)
w6=Label(window,bg='black',fg='red',text='O',width=2)
w7=Label(window,bg='black',fg='red',text='O',width=2)
w8=Label(window,bg='black',fg='red',text='O',width=2)
w9=Label(window,bg='black',fg='red',text='O',width=2)
w10=Label(window,bg='black',fg='red',text='O',width=2)
w11=Label(window,bg='black',fg='red',text='O',width=2)
w12=Label(window,bg='black',fg='red',text='O',width=2)
w13=Label(window,bg='black',fg='red',text='O',width=2)
w14=Label(window,bg='black',fg='red',text='O',width=2)
w15=Label(window,bg='black',fg='red',text='O',width=2)
places_=[]
places_.append(w1)
places_.append(w2)
places_.append(w3)
places_.append(w4)
places_.append(w5)
places_.append(w6)
places_.append(w7)
places_.append(w8)
places_.append(w9)
places_.append(w10)
places_.append(w11)
places_.append(w12)
places_.append(w13)
places_.append(w14)
places_.append(w15)
places={}
file_stat=open('closed.txt','r')
num=''
blocked=[]
if file_stat != '':
    for line in file_stat:
        for char in line:
            if not char==' ':
                num+=char
            else:
                blocked.append(int(num))
                num=''
for window_place in range(15):
    places[window_place]=places_[window_place]
    for num in blocked:
        if window_place==num:
            places[window_place]['text']='X'
            places[window_place]['fg']='hotpink'
del places_
file_stat.close()
game_map=(
    ({},{},{},{}),
    ({},{},{},{}),
    ({},{},{},{}),
    ({},{},{},{}),
    ({},{},{},{})
    )
game_map[0][1]['place']={'title':'Start','status':'Outside'}#1
game_map[0][2]['place']={'title':'The old house','status':'Inside'}#2
game_map[0][3]['place']={'title':'First floor','status':'Inside'}#3
game_map[1][1]['place']={'title':'Field','status':'Outside'}#4
game_map[1][2]['place']={'title':'M. Street','status':'Outside'}#5
game_map[1][3]['place']={'title':'Shop','status':'Inside'}#6
game_map[2][0]['place']={'title':'Hidden room','status':'Inside'}#7
game_map[2][1]['place']={'title':'Cross P. Street and\nO. Street','status':'Outside'}#8
game_map[2][2]['place']={'title':'Cross M. Street and\nP. Street','status':'Outside'}#9
game_map[2][3]['place']={'title':'P. Street','status':'Outside'}#10
game_map[3][0]['place']={'title':'Hidden room shop','status':'Inside'}#11
game_map[3][1]['place']={'title':'O. Street','status':'Outside'}#12
game_map[3][2]['place']={'title':'Inside Castle','status':'Outside'}#13
game_map[3][3]['place']={'title':'Outside Castle','status':'Inside'}#14
game_map[4][1]['place']={'title':'Shop2','status':'Inside'}#15

game_map[0][1]['moves']=['b']
game_map[0][2]['moves']=['r','b']
game_map[0][3]['moves']=['l']
game_map[1][1]['moves']=['r','t']
game_map[1][2]['moves']=['t','b','l','r']
game_map[1][3]['moves']=['l']
game_map[2][0]['moves']=['b','r']
game_map[2][1]['moves']=['b','l','r']
game_map[2][2]['moves']=['t','l','r']
game_map[2][3]['moves']=['l','b']
game_map[3][0]['moves']=['t']
game_map[3][1]['moves']=['t','b']
game_map[3][2]['moves']=['r']
game_map[3][3]['moves']=['l','t']
game_map[4][1]['moves']=['t']

game_map[0][1]['id']=0
game_map[0][2]['id']=1
game_map[0][3]['id']=2
game_map[1][1]['id']=3
game_map[1][2]['id']=4
game_map[1][3]['id']=5
game_map[2][0]['id']=6
game_map[2][1]['id']=7
game_map[2][2]['id']=8
game_map[2][3]['id']=9
game_map[3][0]['id']=10
game_map[3][1]['id']=11
game_map[3][2]['id']=12
game_map[3][3]['id']=13
game_map[4][1]['id']=14

game_map[0][1]['blocked']=False
game_map[0][2]['blocked']=False
game_map[0][3]['blocked']=False
game_map[1][1]['blocked']=False
game_map[1][2]['blocked']=False
game_map[1][3]['blocked']=False
game_map[2][0]['blocked']=False
game_map[2][1]['blocked']=False
game_map[2][2]['blocked']=False
game_map[2][3]['blocked']=False
game_map[3][0]['blocked']=False
game_map[3][1]['blocked']=False
game_map[3][2]['blocked']=False
game_map[3][3]['blocked']=False
game_map[4][1]['blocked']=False
for y in (0,1,2,3,4):
    for x in {0:(1,2,3),1:(1,2,3),2:(0,1,2,3),3:(0,1,2,3),4:(None,1)}[y]:
        if not x==None:
            if places[game_map[y][x]['id']]['text']=='X':
                game_map[y][x]['blocked']=True

coords=[1,0]
moves=[]
blocking=0
out_mapping=0
file=open('select.txt','w')
file.write('Unselected')
file.close()
place_label['text']='Place:\n%s\n\nStatus:\n%s'%(game_map[coords[1]][coords[0]]['place']['title'],game_map[coords[1]][coords[0]]['place']['status'])


def btn_config(mode):
    for btn in buttons:
        if mode=='off':
            btn['state']=DISABLED
        else:
            btn['state']=NORMAL

def display_parameters(coords,text_display=None):
    place_label['text']=''
    for char in text_display:
        place_label['text']+=char
        if char!=' ':
            time.sleep(0.085)
        tk.update_idletasks()

def change_display(coords):
    for x in range(15):
        if places[x]['fg']=='yellowgreen':
            places[x]['fg']='red'

    if coords==[1,0]:
        places[0]['fg']='yellowgreen'
    elif coords==[2,0]:
        places[1]['fg']='yellowgreen'
    elif coords==[3,0]:
        places[2]['fg']='yellowgreen'
    elif coords==[1,1]:
        places[3]['fg']='yellowgreen'
    elif coords==[2,1]:
        places[4]['fg']='yellowgreen'
    elif coords==[3,1]:
        places[5]['fg']='yellowgreen'
    elif coords==[0,2]:
        places[6]['fg']='yellowgreen'
    elif coords==[1,2]:
        places[7]['fg']='yellowgreen'
    elif coords==[2,2]:
        places[8]['fg']='yellowgreen'
    elif coords==[3,2]:
        places[9]['fg']='yellowgreen'
    elif coords==[0,3]:
        places[10]['fg']='yellowgreen'
    elif coords==[1,3]:
        places[11]['fg']='yellowgreen'
    elif coords==[2,3]:
        places[12]['fg']='yellowgreen'
    elif coords==[3,3]:
        places[13]['fg']='yellowgreen'
    elif coords==[1,4]:
        places[14]['fg']='yellowgreen'

def move(y,x,coords,old_coords):
    global blocking
    coords[0] = coords[0] + x
    coords[1] = coords[1] + y
    if not game_map[coords[1]][coords[0]]['blocked']:
        if normal_mode:
            btn_config('off')
        change_display(coords)
        display_parameters(coords,text_display='Place:\n%s\n\nStatus:\n%s'%(game_map[coords[1]][coords[0]]['place']['title'],game_map[coords[1]][coords[0]]['place']['status']))
        if normal_mode:
            btn_config('on')
    else:
        display_parameters(coords,'BLOCKED')
        blocking+=1
        coords[0] = coords[0] - x
        coords[1] = coords[1] - y

def move_top(event=None):
    global out_mapping
    global coords
    if 't' in game_map[coords[1]][coords[0]]['moves']:
        move(-1,0,coords,coords)
        moves.append('top')
    else:
        display_parameters(coords,'OUT OF MAP')
        out_mapping+=1

def move_bottom(event=None):
    global out_mapping
    global coords
    if 'b' in game_map[coords[1]][coords[0]]['moves']:
        move(1,0,coords,coords)
        moves.append('bottom')
    else:
        display_parameters(coords,'OUT OF MAP')
        out_mapping+=1

def move_left(event=None):
    global out_mapping
    global coords
    if 'l' in game_map[coords[1]][coords[0]]['moves']:
        move(0,-1,coords,coords)
        moves.append('left')
    else:
        display_parameters(coords,'OUT OF MAP')
        out_mapping+=1

def move_right(event=None):
    global out_mapping
    global coords
    if 'r' in game_map[coords[1]][coords[0]]['moves']:
        move(0,1,coords,coords)
        moves.append('right')
    else:
        display_parameters(coords,'OUT OF MAP')
        out_mapping+=1


def get():
    tk.destroy()
    return{'place':game_map[coords[1]][coords[0]]['place']['title'],'status':game_map[coords[1]][coords[0]]['place']['status'],'coords':coords,'moves':moves,'out_map':out_mapping,'blocked':blocking}

def select(event=None):
    file=open('select.txt','w')
    file.write('Selected')
    file.close()
    print(get())

wd.grid(row=0,column=0)
window.grid(row=0,column=0)
if normal_mode:
    window2.grid(row=1,column=0)
window3.grid(row=2,column=0)

place_label.grid(row=0,column=0)
photo_frame.grid(row=0,column=1)

if not normal_mode:
    photo_frame.bind_all('<KeyPress-Up>',move_top)
    photo_frame.bind_all('<KeyPress-Down>',move_bottom)
    photo_frame.bind_all('<KeyPress-Left>',move_left)
    photo_frame.bind_all('<KeyPress-Right>',move_right)
    photo_frame.bind_all('<KeyPress-Return>',select)
else:
    t_button=Button(window2,bg='black',fg='dodgerblue',activebackground='black',activeforeground='dodgerblue',text='up',width=6,height=1,command=move_top)
    b_button=Button(window2,bg='black',fg='dodgerblue',activebackground='black',activeforeground='dodgerblue',text='down',width=6,height=1,command=move_bottom)
    l_button=Button(window2,bg='black',fg='dodgerblue',activebackground='black',activeforeground='dodgerblue',text='left',width=5,height=1,command=move_left)
    r_button=Button(window2,bg='black',fg='dodgerblue',activebackground='black',activeforeground='dodgerblue',text='right',width=5,height=1,command=move_right)
    ok_button=Button(window2,bg='black',fg='lime',activebackground='black',activeforeground='lime',text='OK',width=5,height=1,command=select)
    buttons=[]
    buttons.append(t_button)
    buttons.append(b_button)
    buttons.append(l_button)
    buttons.append(r_button)
    buttons.append(ok_button)

    t_button.grid(row=0,column=1)
    b_button.grid(row=2,column=1)
    l_button.grid(row=1,column=0)
    r_button.grid(row=1,column=2)
    ok_button.grid(row=1,column=1)

w1.grid(row=0,column=2)
w2.grid(row=0,column=4)
w3.grid(row=0,column=6)
w4.grid(row=2,column=2)
w5.grid(row=2,column=4)
w6.grid(row=2,column=6)
w7.grid(row=4,column=0)
w8.grid(row=4,column=2)
w9.grid(row=4,column=4)
w10.grid(row=4,column=6)
w11.grid(row=6,column=0)
w12.grid(row=6,column=2)
w13.grid(row=6,column=4)
w14.grid(row=6,column=6)
w15.grid(row=8,column=2)

j1=Label(window,bg='black',fg='red',text='--',width=2).grid(row=0,column=5)
j2=Label(window,bg='black',fg='red',text='|',width=2).grid(row=1,column=2)
j3=Label(window,bg='black',fg='red',text='|',width=2).grid(row=1,column=4)
j4=Label(window,bg='black',fg='red',text='--',width=2).grid(row=2,column=3)
j5=Label(window,bg='black',fg='red',text='--',width=2).grid(row=2,column=5)
j6=Label(window,bg='black',fg='red',text='|',width=2).grid(row=3,column=4)
j7=Label(window,bg='black',fg='red',text='--',width=2).grid(row=4,column=1)
j8=Label(window,bg='black',fg='red',text='--',width=2).grid(row=4,column=3)
j9=Label(window,bg='black',fg='red',text='--',width=2).grid(row=4,column=5)
j10=Label(window,bg='black',fg='red',text='|',width=2).grid(row=5,column=0)
j11=Label(window,bg='black',fg='red',text='|',width=2).grid(row=5,column=2)
j12=Label(window,bg='black',fg='red',text='|',width=2).grid(row=5,column=6)
j13=Label(window,bg='black',fg='red',text='--',width=2).grid(row=6,column=5)
j14=Label(window,bg='black',fg='red',text='|',width=2).grid(row=7,column=2)

x_coords={
    0:(0,1,3),
    1:(0,1,3,5,6),
    2:(0,1),
    3:(0,1,2,3,5,6),
    5:(1,3,4,5),
    6:(1,3),
    7:(0,1,3,4,5,6),
    8:(0,1,3,4,5,6)
    }
y_coords=(0,1,2,3,5,6,7,8)
for y in y_coords:
    for x in x_coords[y]:
        Label(window,bg='black',width=2).grid(row=y,column=x)

if normal_mode:
    x_coords={
        0:(0,2),
        2:(0,2)
        }
    y_coords=(0,2)
    for y in y_coords:
        for x in x_coords[y]:
            Label(window2,bg='black',width=5).grid(row=y,column=x)

tk.mainloop()
