col=`awk 'NR==1{print NF}' file.txt`

awk -v col=$col  \
'
{
    for(i = 1; i <= col; i++) {
        if ( NR == 1) {
            s[i] = $i;
        } else {
            s[i] = s[i] " " $i;
        }
    }
}
END {
    for(i = 1; i <= col ; i++) {
        print s[i]
    }
}
' file.txt


# script below is MLE, because it may call too many awk subprocess
#
# col=`awk 'NR==1{print NF}' file.txt`
# row=`awk 'END{print NR}' file.txt`
# 
# for i in `seq $col`
# do
#     if [ $i -gt 1 ] ; then
#         echo ''
#     fi
#     for j in `seq $row`
#     do
#         if [ $j -gt 1 ] ; then
#             echo -n " "
#         fi
#         echo -n "$(awk 'NR=='$j'{print $'$i'}' file.txt)"
#     done
# done
