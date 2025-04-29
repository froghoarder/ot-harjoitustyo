# Ohjelmistotekniikka: harjoitustyö

This app is a Pacman-style game that users can play to gain points.

## Documentation
- [specification](pacman-game/documentation/specification.md)
- [timetracking](pacman-game/documentation/timetracking.md)
- [changelog](pacman-game/documentation/changelog.md)
- [architecture](pacman-game/documentation/architecture.md)
- [sources](pacman-game/documentation/sources.md)

## Releases
- [Week 6](https://github.com/froghoarder/ot-harjoitustyo/releases/tag/week6)  
- [Week 5](https://github.com/froghoarder/ot-harjoitustyo/releases/tag/week5)

## Installation
1. Install dependencies (with "pacman-game" as your current directory):
```
poetry install
```
2. Start the app by using the command:
```
poetry run invoke start
```

## Command-line operations

#### Running the app
```
poetry run invoke start
```
#### Testing
```
poetry run invoke test
```
#### Test coverage
```
poetry run invoke coverage-report
```
#### Pylint
```
poetry run invoke lint
```
