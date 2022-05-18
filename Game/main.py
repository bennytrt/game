from pylmao import pylmao

g = pylmao()

while g.running:
    g.curr_menu.display_menu()
    g.game_loop()
