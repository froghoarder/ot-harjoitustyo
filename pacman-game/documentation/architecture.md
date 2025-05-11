# Architecture description

## Structure
The package structure of the program is as follows:
![Package structure](./pictures/architecture_package_diagram.png)  
The package _ui_ contains the code responsible for the UI, _entities_ contains code responsible for data objects used by the application and _sprites_ contains code for different sprite objects that make up the game.

## User Interface
The UI consists of the game view created by the class _Renderer_.
The view updates consistently as the game progresses; based on the set value of fps, the function _render_ gets called. It checks whether the level was cleared or the game is over and updated the view if necessary. Afterwards, it draws all the sprites onto the screen: when the playable character or enemies move or collectibles are collected, the attribute _all_sprites_ of the level (which has been passed to the renderer) is updated. This way, the view is updated in real-time.

## Application Logic


#### Class diagram
```mermaid
classDiagram
  GameLoop "1" --> "1" Level
  GameLoop "1" --> "1" Renderer
  GameLoop "1" --> "1" EventQueue
  GameLoop "1" --> "1" Clock
  Level "1" --> "*" Floor
  Level "1" --> "*" Wall
  Level "1" --> "*" Collectible
  Level "1" --> "1" Frog
  Level "1" --> "1" Enemy
  class GameLoop{
      level
      cell_size
      renderer
      event_queue
      clock
    }
  class Level{
      level_map
      cell_size
    }
```
  

### Completing a level
```mermaid
sequenceDiagram
  actor User
  participant Gameloop
  participant Level
  participant Renderer
  User->>Gameloop: collect last collectible
  Gameloop->>Level: collect_stuff()
  Gameloop->>Level: level_status()
  Level-->>Gameloop: 1
  Gameloop->>Renderer: level_cleared()
```
  
  
  
