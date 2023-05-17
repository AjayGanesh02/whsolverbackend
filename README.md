# whsolverbackend

A solver api for the iMessage Word Hunt game. 

The project uses Python's Flask framework for web server architecture and Google Cloud Run for hosting and CD pipelines. 

Solving is done using a custom Solver class that performs a dfs with a custom Trie data structure.

The word list used to determine if words are legal can be found in the `Data` folder.

## Routes
- `GET /` 
  - displays a help message
- `GET /solve`
  - params
    - Board: 16 character alpabetical string
  - returns
    - list of words and positions of characters
