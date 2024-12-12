from tkinter import *
import menu


def set_status(status_text, color='black'):
    canvas.itemconfig(text_id, text=status_text, fill=color)


def pause_toggle():
    global pause
    pause = not pause
    if pause:
        set_status("ПАУЗА")
    else:
        set_status("Вперед!")


def menu_toggle():
    menu.menu_toggle()


def key_handler(event):
    if event.keycode == menu.KEY_UP:
        menu.menu_up()
    elif event.keycode == menu.KEY_DOWN:
        menu.menu_down()
    elif event.keycode == menu.KEY_ENTER:
        menu.menu_enter()
    elif event.keycode == menu.KEY_ESC:
        menu.menu_toggle()


    if game_over:
        return

    if event.keycode == KEY_PAUSE:
        pause_toggle()

    if pause:
        return

    if menu.menu_mode:
        return

    set_status('Вперед!')

    if event.keycode == KEY_FORWARD1:
        canvas.move(player1_id, SPEED, 0)
    elif event.keycode == KEY_FORWARD2:
        canvas.move(player2_id, SPEED, 0)

    check_finish()


def check_finish():
    global game_over

    coords_player1 = canvas.coords(player1_id)
    coords_player2 = canvas.coords(player2_id)
    coords_finish = canvas.coords(finish_id)

    x1_right = coords_player1[2]
    x2_right = coords_player2[2]
    x_finish = coords_finish[0]

    if x1_right >= x_finish:
        set_status('Победил красный игрок!', player1_color)
        game_over = True

    if x2_right >= x_finish:
        set_status('Победил синий игрок!', player2_color)
        game_over = True


def menu_enter():
    menu.menu_enter()


def game_new():
    menu.game_new()

def game_resume():
    menu.game_resume()


def save_game():
    menu.game_save()


def load_game():
    menu.game_load()


def game_exit():
    menu.game_exit()


def menu_show():
    menu.menu_show()


def menu_hide():
    menu.menu_hide()


def menu_up():
    menu.menu_up()

def menu_down():
    menu.menu_down()


def menu_update():
    menu.menu_update()


def menu_create():
    menu.menu_create(canvas)


KEY_FORWARD1 = 39
KEY_FORWARD2 = 68
KEY_PAUSE = 32

game_width = 800
game_height = 800
game_over = False
pause = False

player_size = 100
SPEED = 12
x1, y1 = 50, 50
x2, y2  = x1, y1 + player_size + 100
player1_color = 'red'
player2_color = "blue"
x_finish = game_width - 50

window = Tk()
window.title('game')
canvas = Canvas(window, width=game_width, height=game_height, bg='white')

player1_id = canvas.create_rectangle(x1, y1, x1+player_size, y1+player_size, fill=player1_color)
player2_id = canvas.create_rectangle(x2, y2, x2+player_size, y2+player_size, fill=player2_color)
finish_id = canvas.create_rectangle(x_finish, 0, x_finish + 10, game_height, fill='black')
text_id = canvas.create_text(x1, game_height - 50, anchor = SW, font=('Arial', '25'), text='Вперед!')

canvas.pack()
window.bind('<KeyRelease>', key_handler)
window.mainloop()
