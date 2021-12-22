#!/bin/bash

echo "Enter day:"
read day

echo "Creating folder day$day"
mkdir day$day
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
echo "Done!"
