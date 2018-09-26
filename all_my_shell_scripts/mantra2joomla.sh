#!/bin/bash

DNAME=`dirname $0`
BNAME=`basename $0 .sh`
FILENAME_BASE="$HOME/Desktop/cnp"
FILE2EDIT="${FILENAME_BASE}.txt"
FILEOUT_DE="${FILENAME_BASE}_DE.txt"
FILEOUT_EN="${FILENAME_BASE}_EN.txt"

sed \
	-e "s/    / /g" \
	-e "s/^ //g" \
	-e "/^$/d" \
	-e "s#^Complete Mantra:#<b>Komplettes Mantra:</b>#" \
	-e "s#^Language:#<b>Sprache:</b>#" \
	-e "s#^Translation:#<b>\&Uuml;bersetzung:</b>#" \
	-e "s#^More Information:#<b>Weitere Informationen:</b>#" \
	-e "s/^/<p>/g" \
	-e "s/$/<\/p>/g" \
	-e "s/:<\/b><\/p>\\n<p>/:<\/b><br>\\n/" \
	< ${FILE2EDIT} \
	> ${FILEOUT_DE}
sed \
	-e "s/    / /g" \
	-e "s/^ //g" \
	-e "/^$/d" \
	-e "s#^Complete Mantra:#<b>Complete Mantra:</b>#" \
	-e "s#^Language:#<b>Language:</b>#" \
	-e "s#^Translation:#<b>Translation:</b>#" \
	-e "s#^More Information:#<b>More Information:</b>#" \
	-e "s/^/<p>/g" \
	-e "s/$/<\/p>/g" \
	-e "s/:<\/b><\/p>\\n<p>/:<\/b><br>\\n/" \
	< ${FILE2EDIT} \
	> ${FILEOUT_EN}
${DNAME}/${BNAME}.pl ${FILEOUT_DE} DE
${DNAME}/${BNAME}.pl ${FILEOUT_EN} EN
#echo $?
