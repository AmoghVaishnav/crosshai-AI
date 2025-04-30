# CrosshairAI – Code Suggestion Assistant
CrosshairAI is a minimalistic, interactive AI assistant prototype designed to demonstrate how natural language prompts can be used to trigger intelligent code modifications. The current implementation uses a rule-based approach to simulate how an AI model might behave in a production environment.

# What This Project Does
This project enables a user to:

Paste a block of game-related code.

Provide a natural language prompt describing what they want changed or improved (e.g., "optimize player movement").

Receive a suggested change along with a brief explanation.

Optionally integrate the suggested code directly into the original snippet.

The entire interaction takes place through a simple browser-based interface powered by Flask on the backend.

# Current Logic
The core engine is built around a static knowledge_base.json file, which contains pre-written mappings of:

A natural language intent

The original code snippet

The corresponding suggested version

A short explanation

When the user submits a prompt, the backend performs fuzzy matching between the prompt and the predefined intents. If a close match is found, the system returns the associated code suggestion and explanation. If no match is found, it informs the user that no suggestions are available.

This approach mimics how a real code suggestion engine might behave while using no actual machine learning models.
