# Written by Jessica Zehavi for CoderDojo Twin Cities - www.coderdojotc.org
#! /usr/bin/python
import mcpi.minecraft as minecraft
import mcpi.block as block
import minecraft_letters as letters

# Connect to the Minecraft server
world  =  minecraft.Minecraft.create()

letters.write( world, "CoderDojo", block.GLOWSTONE_BLOCK );
