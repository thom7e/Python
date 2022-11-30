#target area: x=20..30, y=-10..-5
#target area: x=207..263, y=-115..-63


def hitting(velocity,x,y):
    hits = []
    hit_ = []
    counter = 0
    for steps in range(0,500):
        x_velo,y_velo = velocity
        ## x Velocity

        if x_velo > 0:
            x_velo -= 1*steps
        elif x_velo < 0:
            x_velo += 1 * steps
        elif x_velo == 0:
            x_velo = 0 * steps

        ## y Velocity
        y_velo -= 1 *steps
        if x_velo < 0:
            x_velo = 0
        x += x_velo
        y += y_velo

        hits.append(y)
        if x in range(207,264) and y in range(-115,-64):
            hit_.append(max(hits))

    if len(hit_)== 0:
        return False
    else:

        return max(hit_)

maximum = []
counter = 0
for x_velo in range(0,1000):
    for y_velo in range(-500,100):
        if hitting((x_velo,y_velo),0,0):
            counter += 1
        #print(x_velo,y_velo)
        if maximum.append(hitting((x_velo,y_velo),0,0)) == False:
            pass
        else:
            maximum.append(hitting((x_velo,y_velo),0,0))

print(max(maximum))

print(counter)

