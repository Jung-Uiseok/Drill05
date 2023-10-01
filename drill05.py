from pico2d import*
import random

open_canvas(1280,1080)

TUK_ground = load_image('TUK_GROUND.png')
hand_arrow = load_image('hand_arrow.png')
character = load_image('animation_sheet.png')

def handle_events():
    global running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False

running = True
x = random.randint(0,1280)
y = random.randint(0,1080)
frame = 0

while running:
    clear_canvas()
    TUK_ground.draw(1280//2, 1080//2)
    #character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    hand_arrow.draw(x,y)
    update_canvas()
    frame = (frame + 1) % 8

    handle_events()

close_canvas()