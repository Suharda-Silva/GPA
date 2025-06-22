# GUI Wrapper v1.0 for GPA Calculator

This folder contains a Flet-based Graphical User Interface (GUI) for the GPA Calculator.
The GUI is designed to be deployable as a client-side web application, suitable for platforms like GitHub Pages.

## Prerequisites

- Python 3.8+
- [UV (Python Package Installer and Resolver)](https://github.com/astral-sh/uv)

## Setup and Running Locally

1.  **Navigate to this directory:**
    ```bash
    cd "GUI Wrapper v1.0"
    ```

2.  **Initialize UV environment (if not already done) and install dependencies:**
    UV should have created a `uv.lock` and `pyproject.toml` if you ran `uv init` and `uv pip install flet` previously. If you are setting up fresh or in a new environment:
    ```bash
    # If starting from scratch without pyproject.toml or uv.lock:
    # uv init
    uv pip install flet
    # Otherwise, if pyproject.toml and uv.lock exist:
    # uv sync
    ```
    *(Note: The initial setup already performed `uv init` and `uv pip install flet`.)*

3.  **Run the Flet app (for local development with a web view):**
    ```bash
    flet run --web main.py
    ```
    This will typically open the app in your default web browser.

## Building for Static Deployment (e.g., GitHub Pages)

1.  **Build the application:**
    ```bash
    flet build web --output docs
    ```
    This command compiles the Flet app into static web assets (HTML, JavaScript, WASM) and places them in the `docs` subdirectory within `GUI Wrapper v1.0`.

2.  **Deployment to GitHub Pages:**
    *   Ensure the output directory from the build step is named `docs` (or configure GitHub Pages to look for assets in the root of your `gh-pages` branch if you build to a different location).
    *   Push the contents of the `docs` folder (or wherever you built the static assets) to your GitHub repository, typically to a `gh-pages` branch, or to the `main`/`master` branch if you configure GitHub Pages to serve from a `/docs` folder on that branch.
    *   If your GitHub Pages site is served from a subdirectory (e.g., `yourusername.github.io/repository-name/`), you might need to adjust the `--base-url` option during the `flet build web` command. For example:
        ```bash
        flet build web --output docs --base-url "/repository-name/"
        ```
        Replace `/repository-name/` with the actual subpath of your GitHub Pages site. If you are deploying to the root (e.g. `yourusername.github.io`), you might not need `--base-url` or can set it to `/`. The previous build step used a placeholder; adjust as needed for your specific GitHub repository name if deploying to a subpath.

## Project Structure

-   `main.py`: The main Flet application code for the GUI.
-   `GPA.py`: Contains the core GPA calculation logic, adapted from the original CLI version.
-   `docs/`: (After build) Contains the static web assets for deployment.
-   `pyproject.toml`: Project metadata and dependencies for UV.
-   `uv.lock`: Pinned versions of dependencies.
