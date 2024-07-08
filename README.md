# BASIC_REST_API_TEMPLATE

This is a basic Python starting template for a REST API.

## Table of Contents

- [BASIC\_REST\_API\_TEMPLATE](#basic_rest_api_template)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
  - [Usage](#usage)
    - [Command Line Arguments](#command-line-arguments)
    - [Examples](#examples)
  - [Configuration](#configuration)
  - [Shell Script](#shell-script)
    - [Shell Script Examples](#shell-script-examples)
    - [Running the Shell Script](#running-the-shell-script)
  - [API Testing](#api-testing)
    - [Testing the `/api/salutatio` Endpoint](#testing-the-apisalutatio-endpoint)
      - [Example Response](#example-response)
  - [License](#license)

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/project_name.git
    cd project_name
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
    ```

3. **Install the required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set environment file**

    Copy or rename the `example_env` file to `.env` before running:

    ```bash
    cp example_env .env
    ```

## Usage

To run the library, use the provided `run.py` script with appropriate command-line arguments.

### Command Line Arguments

The following command-line arguments can be used:

- `--server` or `-s`: Specify the server host (default: `0.0.0.0`).
- `--port` or `-p`: Specify the server port (default: `8080`).

### Examples

To run the program with default settings:

```bash
python run.py
```

To run the program with a specified host and port:

```bash
python run.py --server 127.0.0.1 --port 5000
```

## Configuration

The configuration settings are managed through environment variables and can be set in a `.env` file in the root directory of the project. 

Example `.env` file:

``` 
SERVER_HOST=0.0.0.0
SERVER_PORT=8080
```

> [!NOTE]
> An `example_env` file is provided to get started. Copy the file to `.env` before running:

```bash
cp example_env .env
```

## Shell Script

A shell script `run.sh` is provided to automate the execution of the script.

### Shell Script Examples

Example `run.sh`

```bash
#!/bin/bash
source ./.venv/bin/activate
python ./run.py
deactivate
```

### Running the Shell Script

To run the script:

```bash
./run.sh
```

## API Testing

### Testing the `/api/salutatio` Endpoint

To test the `/api/salutatio` endpoint, you can use the following `curl` command to pass a name parameter:

```sh
curl -X GET "http://localhost:8080/api/salutatio?name=ego%20draconis"
```

#### Example Response

```json
{
    "greeting": "Salutatio: ego draconis"
}
```

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.