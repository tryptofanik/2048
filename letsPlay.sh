#!/bin/bash


for i in $(seq 3 1 7)
 do
  echo "gra nr. " $i 
  touch "gra"$i

  for j in $(seq 1 1 100)
   do 
     Game.py -n $i -r | grep "move" | tail -1 | awk '{print $3}' >> game$i
     #echo "game nr " $i $a
   done
 done
