import pgzrun,itertools,random
TITLE="Ship target"
WIDTH=400
HEIGHT=400
block=Actor("block")
block.pos=(50,50)
ship=Actor("ship")
ship.pos=200,200
BLOCKPOSITION=[
    (350,50),
    (350,350),
    (50,350),
    (50,50)
]
blockposition=itertools.cycle(BLOCKPOSITION)

def move_block():
    animate(block,
            "bounce_end",
            duration=1,
            pos=next(blockposition))
move_block()
clock.schedule_interval(move_block,2)
def draw():
    screen.clear()
    block.draw()
    ship.draw()

def next_ship_target():
    x=random.randint(100,300)
    y=random.randint(100,300)
    ship.target=x,y
    targetangle=ship.angle_to(ship.target)
    animate(
        ship,
        angle=targetangle,
        duration=0.3,
        on_finished=moveship
    )
def moveship():
    animate(
        ship,
        "accel_decel",
        pos=ship.target,
        duration=ship.distance_to(ship.target)/200,
        on_finished=next_ship_target
    )
next_ship_target()
pgzrun.go()