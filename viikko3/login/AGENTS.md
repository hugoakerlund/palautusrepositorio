# Repository guidance

- Python projects declare Python `>=3.14`. Use exercise's own `uv` environment and lockfile; do not assume dependencies are shared between directories.
- This project is a Flask app (`src/app.py`) with Browser-based Robot suites. From `viikko3/login`, run the app with `uv run flask --app src.app run --port 5001`, then in a second shell run `uv run robot src/tests` (or a single suite such as `src/tests/login.robot`). The suites and `AppLibrary.py` expect the app at `localhost:5001` and use its `/tests/reset` endpoint; Browser tests use Chromium.
- Username and password validation happens in `src/services/user_service.py`.
