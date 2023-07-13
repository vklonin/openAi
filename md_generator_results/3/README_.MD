# Introduction

This repository is a service for chess data processing. It contains various files that are responsible for different functionalities of the service.

## analyzer.js

This file contains functions for analyzing chess positions. It uses other modules such as `analysisQueue`, `converter`, `depthSelector`, and `pgnAnalyzer` to perform the analysis. It can analyze a given chess position and post the analysis to a specified client.

## queue-serializer.js

This file provides functions for serializing and parsing a queue. It uses the `smart-stringifier` module to convert the queue into a string and parse it back into a queue.

## endgame-analyzer.js

This file contains a function for analyzing endgame positions. It uses the `fen-analyzer` module to count the number of pieces on the board and determines whether the position is an endgame or not.

## pgn-analyzer.js

This file includes various functions for analyzing a PGN (Portable Game Notation) file. It checks if the moves in the PGN are optimal, splits the moves into smaller sequences, and checks if the moves are within a certain limit. It also provides functions for converting moves to FEN (Forsyth–Edwards Notation) and vice versa.

## synchronizer.js

This file is responsible for serializing and deserializing a queue. It uses the `queue-serializer` module to convert the queue into a string and parse it back into a queue.

## analysis-queue.js

This file contains a class representing a queue for analyzing chess positions. It uses the `fen-queue` module to implement the queue.

## depth-selector.js

This file provides functions for determining the depth required for analyzing a position. It uses the `base-iterator` module to find the position object and checks if the depth is already set. If not, it returns the default depth value.

## queue-processing-strategy.js

This file defines a class representing a strategy for processing the analysis queue. It takes two dependencies, `pgnAnalyzer` and `baseProvider`, and determines if a move is interesting or not based on the provided dependencies.

## analysis-priority.js

This file defines an object representing the priority levels for analyzing positions. It includes properties for different priority levels such as Emergency, ExternalRequestsForNewPositions, OptimizationOfNotAnalyzedEnough, and MainLineOptimization.

## external-evaluation.js

This file includes a class for external evaluations. It takes a filename as a parameter and provides a method for getting the evaluation's FEN (Forsyth–Edwards Notation).

## converter.js

This file contains a class for converting chess moves to FEN (Forsyth–Edwards Notation) and vice versa. It uses the `chess.js` and `fen-analyzer` modules to perform the conversions.

## usage-statistics-synchronizer.js

This file provides functions for saving and loading usage statistics. It uses the `fs` module to read and write the statistics to a file.

## config.js

This file reads the contents of the `app.config.json` file and exports them.

## usage-statistics.js

This file includes functions for registering and tracking usage statistics. It keeps a log of the users who accessed the service and provides methods for getting the count of unique users within a time period.

## request-processor.js

This file defines a class for processing requests related to chess analysis. It takes dependencies such as `baseManager`, `queueProcessor`, `usageStatistics`, and `analyzer`. It provides methods for handling different request types, such as analyzing a position, getting the users' count, and pinging the service.

## api.js

This file provides functions for creating a request handler map and registering the request processor with an HTTP server. It exports the `register` function to start the server.

# Getting Started

To start the service, follow these steps:

1. Install the necessary dependencies by running `npm install`.
2. Configure the service by editing the `app.config.json` file.
3. Run the service by executing `node index.js`.

# Description

This service is designed for chess data processing. It includes modules for analyzing chess positions, managing analysis queues, converting chess moves to FEN, and optimizing the chess base. It also provides functions for saving and loading usage statistics.

# Contacts

For any inquiries, please contact us at chessdataprocessing@example.com.