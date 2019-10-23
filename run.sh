#!/bin/sh
START=$(date +%s)


echo -e "Week-1 completed"
echo -e "Training Processed Files Created"
echo -e ""
START=$(date +%s)
python2 ./src/week-2.py > /dev/null
END=$(date +%s)
DIFF=$(( $END - $START ))
echo -e  "In time \e[33m $DIFF seconds \e[39m Week-2 completed"
echo -e "Output Frequencies of word_tag calculated"
echo -e ""
START=$(date +%s)
python2 ./src/week-3.py > /dev/null
END=$(date +%s)
DIFF=$(( $END - $START ))
echo -e "In time \e[33m $DIFF seconds \e[39m Week-3 completed"
echo -e "10 word with highest frequency and frequency of tags calculated"
echo -e ""
START=$(date +%s)
python ./src/week-4.py > /dev/null
END=$(date +%s)
DIFF=$(( $END - $START ))
echo -e "In time \e[33m $DIFF seconds \e[39m Week-4 completed"
echo -e "Probabilities of word of having a certain tag calculated"
echo -e ""
START=$(date +%s)
Accuracy="$(python ./src/week-5.py)"
END=$(date +%s)
DIFF=$(( $END - $START ))
echo -e "In time \e[33m $DIFF seconds \e[39m Week-5 completed"
echo -e "Tags for test corpus predicted with accuracy $Accuracy"
echo -e ""
START=$(date +%s)
Confusion_matrix="$(python ./src/week-6.py)"
END=$(date +%s)
DIFF=$(( $END - $START ))
echo -e "In time \e[33m $DIFF seconds \e[39m Week-6 completed"
echo -e "A confusion matrix generated"