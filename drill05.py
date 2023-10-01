from pico2d import*
import random

open_canvas(1280,1080)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('hand_arrow.png')

running = True

def handle_events():
    global running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False

#points = [(random.randint(-1280,1080), random.randint(-1280,1080)) for i in range(10)]

while running:
    clear_canvas()
    TUK_ground.draw(1280//2, 1080//2)
    character.draw(500,500)
    update_canvas()

    handle_events()

close_canvas()