# gsc-500-checker

**gsc-500-checker** (Google Search Console 500 checker) is a Python script that helps you quickly check a list of URLs exported from Google Search Console for 500 errors. It takes a CSV input file with URLs, checks each URL for a 500 response, and generates an output CSV with the results.

## Features

- Checks the HTTP status of each URL in a CSV file.
- Detects if a URL returns a 500 error.
- Outputs a new CSV file with status codes and a flag indicating whether the URL is free from 500 errors.
- Progress bar for real-time feedback during execution.

## Prerequisites

Ensure you have Python 3 installed on your machine. You can download it from [python.org](https://www.python.org/).

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/bhhaskin/gsc-500-checker.git
    cd gsc-500-checker
    ```

2. (Optional) Set up a virtual environment using `venv` to manage your dependencies.

### Using `venv`

To create and activate a virtual environment:

- **On Linux/macOS:**

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

- **On Windows:**

    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. When you are done working with the project, you can deactivate the virtual environment by running:

    ```bash
    deactivate
    ```

## Usage

1. Prepare a CSV file named `input_urls.csv` with the following columns:

    - `URL`
    - `Last crawled`

    Example:

    | URL                      | Last crawled |
    |---------------------------|--------------|
    | http://example.com/page1   | 2024-09-30   |
    | http://example.com/page2   | 2024-09-29   |
    | http://example.com/page3   | 2024-09-28   |

2. Run the script:

    ```bash
    python main.py
    ```

By default, the script will check the URLs in `input_urls.csv` and output the results in `output_results.csv`.

## Example

Output CSV (`output_results.csv`):

| URL                      | Status Code | Not 500 |
|---------------------------|-------------|---------|
| http://example.com/page1   | 200         | True    |
| http://example.com/page2   | 500         | False   |
| http://example.com/page3   | 200         | True    |

## Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/bhhaskin/gsc-500-checker/issues) if you want to contribute.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
