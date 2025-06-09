# Random IP Generator

## What does it do?

Generates a random IP address in the format `X.X.X.X`, where each part of the IP is a number between 0 and 255.

- Uses `randint(1, 255)` for the first block (avoiding 0, which may be invalid in some cases).
- Uses `randint(0, 255)` for the other three blocks.