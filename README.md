# BATTLESHIPS

This is a battleships game played in a mock terminal created by code institute.
[This is a live link to the project.](http://battleships-vs-computer.herokuapp.com/)
![intro](https://user-images.githubusercontent.com/89077706/154116688-ba745c5a-fa7c-47f1-971d-3eceb43972ad.png)

## How to play

This game is played against a computer, taking turns to guess ship coordinates on a gameboard that’s eight spaces wide and long. All ships resemble one character or space on the board. The player will get to place out four ships and then start guessing the location of the computer's ships. If the computer manages to sink a ship, the computer's guessing board will display, showing what ship it sunk and send a message telling the user it sank one of their ships. The first one to sink all four of the opponent's ships wins!

## Features

### Existing features

- The user inputs two numbers that will be translated to coordinates where their ships will be placed on the board.
- The randint function is imported to get two random integers from the computer to place out its ships.
- There is a function to get the coordinate value from the user and validate it so that there is an error message for whenever the user enters numbers that are     higher or lower than the board size, any letter, and when no value is entered. 
- The user will be alerted when the computer sinks one of the user's ships and the computer's guesses and sunken ships will be displayed.
- Every time the user or computer sinks a ship their score will be incremented and the first one to get a score of four, wins.
- If the user enters a value for a coordinate that they have already guessed then they will be told so and asked to enter a new value.


### Future features 
- The user gets to set the width and length of the board.
- The user gets to set the length of the ships.
- The user gets to choose how many ships are to be placed out on the board.

## Testing

I have manually tested this application by doing the following:

- The application has been run through the PEP8 linter with no problems returned.
- I have asked friends to play through the game and they have done so without any issues.
- I have tested it in my local terminal as well as the deployed version.

### Validator testing

No error or warnings were returned when run through the [PEP8-linter](http://pep8online.com/)

### Fixed bugs
When using the randint function I asked the computer to return an integer starting at zero and stopping at nine, as you would when setting the range method, which returned an IndexError. I solved this by changing the values to correspond with the indexes on the gameboard. 

### Unfixed bugs
- no bugs remaining

### Deployment

This project was deployed using Code Institute’s mock terminal for Heroku.

- Steps for deployment are as follows:
- Fork or clone this repository
- Create a new Heroku app
- Set the buildpacks to Python and NodeJs in that order
- Link the Heroku app to the repository
- Click on Deploy

### Credits

Code Institute 
- Template for the deployment terminal.
