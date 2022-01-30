#!/usr/bin/env bash

THIS_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" &> /dev/null && pwd)
export FLASK_ENV=development
flask run