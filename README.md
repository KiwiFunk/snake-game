# SNAKE
A recreation of Google's snake game written in Python using pygame. I created this using a wonderful tutorial by Clear Code to teach me the basics of pygame and help me through creating the basic game loop, before starting to extend the features using my own ideas.

So far I have added on and reworked the fruits class to allow multiple randomly selected sprites for some variation, as well as a simple scaling animation to make them feel more dynamic. As a challenge I am trying to implement most of the features the Google example has.

## Game Features
Use WASD or the Arrow Keys to move the snake around and feed him fruit! Gain ten points for each piece of fruit consumed, but careful not to chomp yourself or hit a wall!

## Planned features
<ul>
    <li>Add start and endgame menus</li>
    <li>Implement a highscore system with a primative .txt file to store persistant data</li>
    <li>Use Masks for snake sprites to allow the user to change color</li>
    <li>Implement some kind of gradient over the snake body like in the google one</li>
    <li>Create and implement a sprite sheet for a random change tongue animation</li>
    <li>Rework and create a cohesive set of fruit sprites</li>
    <li>Create BGM and more SFX</li>
</ul>

## Assets
All the featured assets were made by me! Assets were based off those featured in Google's version, and by extension the ones in the tutorial (linked below). I created the graphics inside of Adobe Illustrator, and then made the sounds inside of FL Studio


## Really Useful Resources

[Learning pygame by creating Snake - Clear Code](https://www.youtube.com/watch?v=QFvqStqPCRU&list=LL&index=6)

A really awesome introduction into PyGame by a channel called Clear Code that waks you through all the basic steps for creating the snake game in PyGame with only a basic understanding of the Python language required


[Stack Overflow on scaling](https://stackoverflow.com/questions/59919826/how-do-i-scale-a-pygame-image-surface-with-respect-to-its-center)

A great answer by Rabbid76 that explains how to handle scaling in pygame. I was pulling my hair out over trying to scale from the center instead of the top left!
