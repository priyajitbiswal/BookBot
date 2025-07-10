# BookBot

BookBot is a simple Python command-line tool that analyzes text files (books) to provide word and character statistics.

## Features

- Counts the total number of words in a book
- Counts the frequency of each alphabetic character (case-insensitive)
- Displays character counts sorted by frequency

## Usage

1. Place your book (text file) in the `books/` directory or specify any `.txt` file path.
2. Run the script from the command line:

```
python main.py <path_to_book>
```

**Example:**

```
python main.py books/frankenstein.txt
```

## Output Example

```
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found 78,000 total words
--------- Character Count -------
e: 10,000
t: 8,000
... (other characters)
============= END ===============
```

## Requirements

- Python 3.6 or higher

## Project Structure

- `main.py` — Main script to run BookBot
- `stats.py` — Functions for word and character statistics
- `books/` — Directory for book text files

## License

MIT License
