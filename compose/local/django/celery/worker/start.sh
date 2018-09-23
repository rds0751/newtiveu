#!/bin/sh

set -o errexit
set -o pipefail
set -o nounset
set -o xtrace


celery -A tiveU.taskapp worker -l INFO
