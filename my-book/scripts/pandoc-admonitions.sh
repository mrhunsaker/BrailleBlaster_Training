#!/usr/bin/env bash
exec pandoc --lua-filter=/home/ryhunsaker/GitHubRepos/BrailleBlaster_Training/my-book/admonitions.lua "$@"