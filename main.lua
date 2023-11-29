lg = love.graphics

screen_w = lg.getWidth()
screen_h = lg.getHeight()

grid_size = 32

-- mew mew
local function new_frame(x1, y1, x2, y2, color)
    return {x1=x1, y1=y1, x2=x2, y2=y2, color=color}
end

-- new color
local function gc(color_str)
    colors = {
        red = {1, 0, 0},
        blue = {0, 0, 1},
        green = {0, 1, 0},
        yellow = {1, 1, 0},
        magenta = {1, 0, 1},
        off_white = {0.5, 0.5, 0.5}
    }

    return colors[color_str]
end

-- axis aligned bounding box
function aabb(x, y, f)
    return x >= f.x1 and y >= f.y1 and x <= f.x2 and y <= f.y2
end

-- set color per grid square
function color_frames(x, y, frames)
    for i = 1, #frames do
        foo_frame = frames[i]

        if aabb(x, y, foo_frame) then
            lg.setColor(unpack(foo_frame.color))
        end
    end
end

function love.load()
    print(unpack(gc('blue')))
end

function love.update(dt)

end

frames = {
    new_frame(1, 1, 6, 6, gc('blue')),
    new_frame(6, 1, 18, 3, gc('green')),
    new_frame(6, 4, 18, 6, gc('yellow')),
    new_frame(1, 11, 30, 14, gc('red')),
    new_frame(12, 1, 30, 10, gc('off_white')),
}

function love.draw()
    for y = 1, grid_size do
        for x = 1, grid_size do
            lg.setColor(1, 1, 1)
            color_frames(x - 1, y - 1, frames)
            
            lg.rectangle(
                "line",
                (x - 1) * grid_size,
                (y - 1) * grid_size,
                grid_size,
                grid_size
            )
        end
    end
end
