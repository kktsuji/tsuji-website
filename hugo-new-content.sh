#!/bin/bash

POST_NAME=$1
YEAR=2024
COMMAND_CREATE="hugo new content blog/$YEAR/$POST_NAME/index.md"
COMMAND_CP="cp -r content/en/blog/$YEAR/$POST_NAME/ content/jp/blog/$YEAR/"

echo $COMMAND_CREATE
$COMMAND_CREATE
echo $COMMAND_CP
$COMMAND_CP
