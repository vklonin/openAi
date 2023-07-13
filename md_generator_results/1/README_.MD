# Chess Data Processing Service

This service is designed for analyzing chess positions and providing optimal moves.

## How to Start

1. Install the required dependencies by running `npm install`.

2. Start the service by running `node server.js`.

## Folder Structure

- `analysis`: Contains modules related to analyzing chess positions.
  - `analyzer.js`: Module responsible for analyzing chess positions and making optimal moves.
  - `pgn-analyzer.js`: Module for analyzing Portable Game Notation (PGN) and determining if the moves are within the optimal limit.
  - `depth-selector.js`: Module for selecting the depth of analysis required for a position.
  - `analysis-queue.js`: Module for managing the queue of positions to be analyzed.
- `chessbase`: Contains modules for managing the chess database.
  - `base-manager.js`: Module for managing the base of chess positions and performing optimizations.
  - `base-iterator.js`: Module for iterating over the chess base and finding specific positions.
- `converter.js`: Module for converting chess moves to FEN (Forsyth–Edwards Notation) format.
- `server.js`: Entry point for starting the service.

## Starting the Service

To start the service, follow these steps:

1. Install the dependencies by running `npm install`.

2. Start the service by running `node server.js`.

## Analyzing Chess Positions

To analyze a chess position, make a POST request to `/api/analyze` with the following JSON data:

```json
{
  "moves": ["e4", "e5", "Nf3"]
}
```

The service will analyze the position and return the optimal move(s) for the given moves.

## Retrieving Chess Base

To retrieve the current chess base, make a GET request to `/api/base`.

## Retrieving FEN Data

To retrieve FEN data for a specific position, make a GET request to `/api/fendata` with the `fen` query parameter:

```
GET /api/fendata?fen=rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1
```

## Getting Users Count

To get the number of active users, make a GET request to `/api/userscount`.

## Ping

To ping the service and process the analysis queue, send a GET request to `/api/ping`.