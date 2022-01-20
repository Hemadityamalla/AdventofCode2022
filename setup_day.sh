#!/bin/bash

echo "Enter day:"
read day

echo "Creating folder day$day"
mkdir -p day$day
echo "Creating test input file"
touch day$day/test.inp
echo "Creating main input file"
touch day$day/day$day.inp
echo "Creating main file"
touch day$day/day$day.py
cat <<EOF >day$day/day$day.py
#Add import libs below

def parseInput(fin):



parsed = parseInput(open("test.inp"))
#parsed = parseInput(open("day$day.inp"))


#Part 1
print("Part 1: ", )



#Part 2
print("Part 2: ", )

EOF


echo "Fetching the main input"
python - << EOF
import requests
cookies_dict={"session": "53616c7465645f5f5b0c15fcbd65a268049a89bae5305465a4b3e35851d5fe5582f283134db93c8b5e12ad9e0db56fd1"}
url='https://adventofcode.com/2021/day/$day/input'
req = requests.get(url, cookies=cookies_dict)
f = open("day$day.inp","a")
f.write(req.text)
f.close()
EOF
echo "Finished fetching the main input, and wrote to day$day.inp"
echo "Done!"
