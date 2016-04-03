#!/bin/bash

:<<'COMMENT'
extension=".txt"
cd trunk
echo $(pwd)
echo $array
for dir in *
	do
		cd "$dir"
		#echo $(pwd)
		name="$dir$extension"
		#echo $name
		array=("${array[@]}" "$(pwd)/$name")
		echo "creating $name in $(pwd)"
		touch "$name"

		cd ..
	done
#echo "${array[@]}"
for name in "${array[@]}"
	do
		git --add "$name"
	done
COMMENT

cd trunk
name="hello.txt"
echo "$name"
touch "$name"
:<<'COMMENT'
git add "$name"
git commit -m "adding $name to repo through shell script"
git push
COMMENT