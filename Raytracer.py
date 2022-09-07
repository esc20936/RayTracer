from gl import Raytracer, V3, color
from figures import *
from lights import *


width = 1024
height = 1024

# Materiales

snow = Material(diffuse = (0.8, 0.8, 0.8))
black = Material(diffuse = (0, 0, 0))
white = Material(diffuse = (1, 1, 1))
orange = Material(diffuse = (1, 0.5, 0))




rtx = Raytracer(width, height)


rtx.lights.append( AmbientLight( ))
rtx.lights.append( DirectionalLight(direction = (-1,-1,-1) ))

# Body
rtx.scene.append( Sphere(V3(0, -4, -12), 2, snow) )
rtx.scene.append( Sphere(V3(0, -1, -12.1), 1.5, snow) )
rtx.scene.append( Sphere(V3(0, 1, -12), 1, snow) )


# Nose
rtx.scene.append( Sphere(V3(0, 1, -11), 0.2, orange) )

# Eyes
rtx.scene.append( Sphere(V3(-0.2, 1.2, -10), 0.1, black) )
rtx.scene.append( Sphere(V3(0.2, 1.2, -10), 0.1, black) )


# parable as smile
rtx.scene.append( Sphere(V3(-0.1, 0.5, -11.2), 0.1, black) )
rtx.scene.append( Sphere(V3(-0.3, 0.7, -11.1), 0.1, black) )
rtx.scene.append( Sphere(V3(0.1, 0.5, -11.2), 0.1, black) )
rtx.scene.append( Sphere(V3(0.3, 0.7, -11.1), 0.1, black) )


# Buttons
rtx.scene.append( Sphere(V3(0, -3, -10), 0.3, black) )
rtx.scene.append( Sphere(V3(0, -2.3, -11),0.3, black) )
rtx.scene.append( Sphere(V3(0, -1, -10.5),0.3, black) )




# rtx.scene.append( Sphere(V3(0,0,-10), 2, brick)  )
# rtx.scene.append( Sphere(V3(-4,-2,-15), 1.5, stone)  )
# rtx.scene.append( Sphere(V3(2,2,-8), 0.2, grass)  )


rtx.glRender()

rtx.glFinish("outputa.bmp")