#!/bin/bash

watch(/Dockerfile$/) { `fig build` }
watch(/compose.yml$/) { `fig up -d` }
