# Ollama Text Generation Script

This Python script utilizes the Ollama API to generate text based on a given prompt. It interacts with a local Ollama instance to produce responses using a specified language model.

## Features

-   Generates text using the Ollama API.
-   Supports specifying a language model.
-   Provides a simple interface to send prompts and receive text responses.
-   Error handling for API call failures.
-   Non-streaming response.

## Prerequisites

-   Python 3.6 or higher
-   `pip` package manager
-   [Ollama](https://ollama.ai/) installed and running locally
-   Ollama 모델 다운로드 (예: `gemma2`)

## Installation

1.  Clone the repository (if applicable) or download the `script.py` file.
2.  Install the `requests` library using `pip`:

    ```bash
    pip install requests
    ```

3. Download required Ollama Model

   ```bash
   ollama pull gemma2
