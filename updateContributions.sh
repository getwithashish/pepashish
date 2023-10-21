#!/bin/bash

entireContributions=`python3 contributionDetails.py`
echo $entireContributions

awk -v var="$entireContributions" '{sub(/- Total Contributions in GitHub: [0-9]+/, "- Total Contributions in GitHub: **" $$var$$ "**")} {print}' README.md > TEMP_README.md && mv TEMP_README.md README.md
