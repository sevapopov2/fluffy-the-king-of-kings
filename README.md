# fluffy-the-king-of-kings
A fighting audio game written on Python for fun

This is a project that's made as learning experience about audio game development.
It may remind you existing fighting games such as Super Smash Bros, which is the main inspiration for this project.
So if you find it like that please remember that I didn't want to make any plagiat or so, the game is made for fun and doesn't have any goals to make a parody of something.
The plushies list is taken from Plushiestan community (mainly plushies accounts on Instagram).
I hope you find it fun and interactive!
The game is in the development stage and I learn things at the same time, so I hope everything will work!
Enjoy!

## How to make the project work on Linux with pipenv
When installing and running the project with pipenv virtual environment, there will be an error that speech-dispatcher is not found when accessible_output2's commands are executed.
To fix that copy speech-dispatcher's package from
/usr/lib/python3.x/site-packages/speechd to site-packages of your pipenv virtual environment.
You can find the location of pipenv environment by typing pipenv --where.
