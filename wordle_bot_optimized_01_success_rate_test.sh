#!/bin/bash

y=0
n=0
l="#"
for i in {0..999}
do
	rval=$(python3 ./src/wordle_bot_optimized_01.py > /dev/null)
	if [ $? == 1 ]; then
		((++n))
	else
		((++y))
	fi
	printf "\r%s %%" "$(( $i / 10 ))"
done
printf "\r100 %%"
echo
VAR=$(bc <<< "scale=1; $y / 10")
echo "Success rate: $VAR %"
VAR=$(bc <<< "scale=1; $n / 10")
echo "Failure rate: $VAR %"
