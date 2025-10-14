#!/bin/bash

name=$1

echo "Hi $name"

sleep 1

echo "Let's start coding!"

read answer

if [[ $answer == "Yes" ]]; then

 echo "Let's go!"
 sleep 1

else

 echo "Maybe next time!"

fi
