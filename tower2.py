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

# Execute the loop, building from the bottom up
for level in range( 0, height ):
	world.setBlock( x, level, z, material )

# Put the player on top of the tower
world.player.setPos( x, height, z )
