## Chess Data Processing Service

This repository contains a service for processing chess data. Here is a brief overview of the files:

1. `analysis/analyzer.js`: This file contains functions for analyzing chess positions and making recommendations based on the analysis.
2. `analysis/queue-serializer.js`: This file provides functions for serializing and deserializing the analysis queue.
3. `analysis/endgame-analyzer.js`: This file is responsible for analyzing the endgame and determining if a position is in the endgame phase.
4. `analysis/pgn-analyzer.js`: This file contains functions for analyzing Portable Game Notation (PGN) and checking if moves are within the limit.
5. `analysis/synchronizer.js`: This file handles the loading and saving of the analysis queue to a file.
6. `converter.js`: This file provides functions for converting chess moves and JSON base to FEN notation.
7. `usage-statistics-synchronizer.js`: This file handles loading and saving of the usage statistics to a file.
8. `config.js`: This file reads the configuration data from `app.config.json`.
9. `usage-statistics.js`: This file keeps track of usage statistics and allows for resetting and retrieving the statistics.
10. `request-processor.js`: This file handles processing of API requests, such as analyzing positions and retrieving users count.
11. `api.js`: This file creates an HTTP server and maps API endpoints to the request processor.

To start the service, you need to run the `api.js` file.