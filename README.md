# DVONN

## Description

A C++ implementation of the wonderful abstract strategy board game DVONN.  
Rules of the game and general strategy can be found at the [Project GIPF Website DVONN page](http://www.gipf.com/dvonn/).  

## Source Project

This program is a modified version of the C++ DVONN implementation included in the source code of the latest version of the Holtz application, Holtz 1.5.0, found at the [Holtz Project Website](https://holtz.sourceforge.io/down.php).  

Holtz 1.5.0 includes implementations of the board games Zertz, Relax, and Bloks in addition to DVONN.  
I will only be making modifications and adding features to the DVONN portion of the program, and intend to remove all other games from the program as soon as possible, with the exception of the holtz-1.5.0 branch, which will always contain the original, unmodified source code for reference.  

This project aims to expand beyond Holtz' DVONN application, producing a more refined DVONN implementation that offers players many new gameplay features:
- Greater control over the skill level of the AI by allowing parameter adjustments
- Preset AI skill levels so that the learning curve against the AI is not as steep
- Greater understanding of what move is the best on a given turn by providing the n best moves on that turn and their scores, if the option is enabled
- Handling saving of the move history of any game, so that that game may be replayed or shared at a later date
- Additionally, the game state of a saved game may be loaded immediately after the placement phase, and the player can replay through the movement phase with a placement identical to the saved game
- In addition to the moves made by the players, at each turn a number of game state statistics are calculated and saved, if the option is specified. These statistics will be used to collect a body of data which will hopefully show relations between winning strategies and the types of game states you want to aim for at different sections of the game
- This modded version of the game will continue support for playing DVONN online with other players
- I hope to wrap all of these features in an aesthetically pleasing, easy to use GUI that reflects the aesthetics of the latest version of the board game

## Authors

Original Holtz program developed by Martin Trautmann, Florian Fischer, and Manuel Moser.
This modded DVONN project developed by Aidan Wilson.
This information is stated in the AUTHORS file found in the main directory of any branch of this project.  


## Licensing

The original Holtz program is free and open source, and my public distribution of the original source code, my modifications to the source code, and my public distribution of the modified source code are all protected by the GNU General Public License, Version 2 (GPLv2), as stated in the COPYING file found in the main directory of any branch of this project.


## Installation

At the moment, I have not made significant changes in the original Holtz version, so that installation instructions are the same as for that program.
Those instructions are found in the INSTALL file found in the main directory of the holtz-1.5.0 branch of this project.


## Usage

Once installed using the directions in the INSTALL file, the executable can be run, which in the current project state opens the Holtz application.

In the menu bar, you may select to begin a new DVONN game.
You can either play against the AI (which in Holtz only has one difficulty: destruction), or you can play against another player online or locally.

Each player has the option of the game displaying either no helping information, displaying all possible moves that may be made on any turn, or displaying the "best" move recommended by the AI on any turn. 
You may choose these visualization options for the AI player as well, if you so choose.
The player order is decided by the order in which player names appear in the list, the top player has the white pieces, and as such plays first.


## Development Motivation and Roadmap

This is just a hobby project for me, as I really enjoy playing DVONN against the bot, but want to know more about why the moves it chooses end up in it winning, and how those general winning movesets combine into a larger strategy of how to approach the game.

Additionally, I want to be able to mess around with the parameters that the AI uses to calculate the "best" move on any given turn, specifically how it performs pruning of the search tree.

I hope to make some preset AI difficulties so that I can get more players interested in playing DVONN without them immediately losing game after game after game.

Because I work full time, and this is just a hobby project, I do not anticipate making constant heavy progress on this.
However, I expect I will be able to achieve many of the goals I outline below within a few months.


## Planned Modifications and Added Features

Highest priority tasks highlighted in __bold__.

### 1. Allow saving of move history/game state statistics for any played game 
  - [ ] __Move sequences are already tracked in-game, need to format to save to/load from file__    
  - [ ] __In addition to move sequences, some data metrics would be really nice to save at each turn__  
    - [ ] __Number of stacks of each height under each player's control__  
    - [ ] __Number of moves each player can make__  
    - [ ] __Number of mobile/immobile stacks each player has under their control__  
    - [ ] __Number of DVONN pieces (red pieces) that are free or under each player's control__  
    - [ ] __Number of pieces of each player that have been removed from the game__  

### 2. Develop stack grouping and distance metrics that could be saved in game history for strategy statistics
(all just ideas, some probably won't work and/or be useful)  
  - [ ] __Geometry characteristics of each player's stack groupings:__  
    - [ ] __How many blobs of stacks (relatively circular groupings) does that player have?__  
    - [ ] __How many contiguous lines of stacks?__  
    - [ ]  __Approximate diameter or some better size metric for those stack blobs__      
    - [ ] __Approximate width or some better size metric for those stack lines__  
    - [ ] __Number of stacks in blobs/lines that make contact with board edges,  
    DVONN pieces/stacks under varying control, and other player's stacks of varying heights__  
  - [ ] __Average minimum distance metrics of each player's controlled stacks:__  
    - [ ] __I suppose distance metrics would generally be designed as:__
    - [ ] __Distance in straight lines unless mentioned otherwise__  
    - [ ] __Possible stack moving distance metric is distance to some feature in possible stack move chains only__  
    e.g. Stack of distance 5 to DVONN stack could be a 2 stack capturing a 1 stack, then the resulting 3 stack capturing the DVONN stack,  
    i.e. 5 units of distance were moved in total  
    - [ ] __Average minimum distance from player's stacks of varying heights to board edges__  
    e.g. Average minimum distance from black stacks of height 1 to board edges  
    - [ ] __Average minimum distance from player's stacks of varying heights to DVONN pieces/stacks under varying control__  
    e.g. Average minimum distance from white stacks of height 2 to free DVONN pieces  
    - [ ] __Average minimum distance from player's stacks of varying heights to opponent's stacks of varying heights__  
    e.g. Average minimum distance from white stacks of height 2 to black stacks of height 4  


### 3. Allow replay of a game using saved move history
  - [ ] __Ability to view whole game, stepping forward and backward through the game's moves__  
  - [ ] __Ability to view all possible moves at any turn in the move history__  
  - [ ] __Ability to view AI recommended moves at any turn in the move history__  
    - [ ] __View moves recommended by AI used when the game was played__  
    - [ ] __View moves recommended by new AI with adjustments (see below planned feature category)__  
    - [ ] __View both at the same time__  
  - [ ] __Both all possible moves and AI recommended moves can be toggled on/off at any point in the game replay__  


### 4. Allow use of a placement setup loaded from a saved game for local and online play
  - [ ] __Placement phase results are copied from the saved game, and only movement phase is played through__  


### 5. Allow adjustment of AI
  - [ ] Ability to adjust skill level  
  - [ ] __Ability to adjust depth of search tree__  
  - [ ] __Ability to adjust parameter values for search algorithm__  
  - [ ] Possible ability to adjust overall move search algorithm used  

### 6. Allow increased transparency for AI recommended "best moves"
  - [ ] __Give top n recommended moves and their associated scores when requested__  

### 7. Fix bugs (applicable to DVONN) mentioned by developers in the TODO file in the Holtz 1.5.0 source code
  - [ ] Client name/ip not valid for server in linux  
  - [ ] Asking queries should be deferred during game setup dialog  
  - [ ] __Fix memory leak in ai.cpp -> AI_Input::destroy_ai__  

### 8. Redesign GUI
  - [ ] __Remove all other board games from the program, only allowing for DVONN functionality__  
  - [ ] __Add ability to scale up to larger resolutions/screen sizes, not just 50, 60, and 70 px sizes for the pieces__  
  - [ ] __Add artwork of current game board and box__  
  - [ ] __Design main menu screen__  

#### 8.a. Design options screen  
  - [ ] __Game resolution, aesthetics, and sound options__  
  - [ ] __Default game history save/load filepath options__  
#### 8.b. Design local game menu screen  
  - [ ] __Player vs. AI or Player vs. Player choice__  
  - [ ] __AI adjustment options__  
  - [ ] __Enable/disable game history save and specified game history save filepath options__  
  - [ ] __Enable/disable ability to show all possible moves and/or AI recommended moves at any turn (in-game toggle)__  
      - [ ] __Each player can: view no help, view all possible moves, view AI recommended moves, or view both__  
      - [ ] __Each player can toggle between enabled view states on any turn of the game, including opponent's turns__  

#### 8.c. Design online game menu screen  
  - [ ] Server and client options  
  - [ ] Enable/disable game history save and specified game history save filepath options  
  - [ ] Enable/disable ability to show all possible moves and/or AI recommended moves at any turn (in-game toggle)  
    - [ ] Both players must agree on viewing of all possible moves and/or AI recommended moves  
    - [ ] Each player can: view no help, view all possible moves, view AI recommended moves, or view both  
    - [ ] Each player can toggle between enabled view states on any turn of the game, including opponent's turns  
    - [ ] If AI recommended moves feature on for at least one player, both players must agree on AI adjustment options  
  - [ ] AI adjustment options, for case of AI recommended moves feature
 
#### 8.d. Design game screen  
  - [ ] __Use board background and piece textures from newest version of the game__  
 
#### 8.e. Design game history replay menu screen  
  - [ ] __Game history load filepath options__  

#### 8.f. Design game history replay viewing screen  
  - [ ] __During replay, viewer can: view no help, view all possible moves, view AI recommended moves, or view both__  
    - [ ] __Viewer can toggle between enabled view states on any turn of the game__  
    - [ ] __Ability to step forward and backward through the game's moves, or go to a specific turn of the game__  
    - [ ] __Recommended moves from the adjusted AI can be shown with/instead of original AI recommended moves__  
      - [ ] __View no recommended moves__ 
      - [ ] __View moves recommended by AI used when the game was played__  
      - [ ] __View moves recommended by new AI with adjustments (see below planned feature category)__  
      - [ ] __View both at the same time__  

#### 8.g. Ensure GUI is consistent and aesthetically pleasing in design:  
  - [ ] Ease of reading, navigability of menus, brevity and clarity of language  
    - [ ] Variant, size, weight, width, slope, spacing, etc. of chosen typefaces work well with rest of design  
    - [ ] Adequate contrast between text and surrounding textures  
    - [ ] Spacing between and relative sizing of text, textures, images, etc. work well, even after resolution scaling  
    - [ ] Overall color scheme, etc. should be consistent and pleasing to look at  
