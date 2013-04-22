# Written by Jessica Zehavi for CoderDojo Twin Cities - www.coderdojotc.org
#!/usr/bin/python
import mcpi.minecraft as minecraft
import mcpi.block as block

# Connect to the Minecraft server
world  =  minecraft.Minecraft.create()

# Get the player's current position and store the coordinates
[x,y,z] =  world.player.getPos()

# Set some variables to customize your tower
height    =  3 
material  =  block.GLASS

level  =  0
keep_building  =  True

# Execute the loop, building from the bottom up
while keep_building:
	world.setBlock( x, level, z, material )
	level = level + 1

	if level > height:
		keep_building  =  False

# Put the player on top of the tower
world.player.setPos( x, height, z )
