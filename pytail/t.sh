a=9
let "a += 1"
echo $a

i=0;
#while true; do echo $i; let " i += 1 ";  sleep 1 ;  done
while true; do echo $i; (( i = i + 1 ));  echo $i >> "foo.txt"; sleep 1 ;  done

