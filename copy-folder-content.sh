#!/bin/bash

# Ask for folder path
read -rp "Enter folder path: " FOLDER

# Validate folder
if [[ ! -d "$FOLDER" ]]; then
  echo "Error: '$FOLDER' is not a valid directory."
  exit 1
fi

# Create temporary file
TMP_FILE=$(mktemp)

# Write content header
echo "CONTENT" > "$TMP_FILE"

# Recursively find files and append their content with headers
find "$FOLDER" -type f | sort | while read -r FILE; do
  REL_PATH="${FILE#$FOLDER/}" # Strip the base path for relative paths
  echo -e "\n=== $REL_PATH ===\n" >> "$TMP_FILE"
  cat "$FILE" >> "$TMP_FILE"
done

# Write footer
echo -e "\n\nEND OF CONTENT" >> "$TMP_FILE"

# Copy to clipboard (macOS: pbcopy, Linux: xclip or xsel)
if command -v pbcopy &> /dev/null; then
  cat "$TMP_FILE" | pbcopy
  echo "📋 Copied to clipboard using pbcopy."
elif command -v xclip &> /dev/null; then
  cat "$TMP_FILE" | xclip -selection clipboard
  echo "📋 Copied to clipboard using xclip."
elif command -v xsel &> /dev/null; then
  cat "$TMP_FILE" | xsel --clipboard
  echo "📋 Copied to clipboard using xsel."
else
  echo "⚠️ No clipboard utility found. Here's the output:"
  cat "$TMP_FILE"
fi

# Clean up
rm "$TMP_FILE"
