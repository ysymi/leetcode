#! /usr/bin/bash


function parse_words() {
    for line in `cat words.txt`
    do
        for word in ${line}
        do
            echo ${word}
        done
    done
}

parse_words | sort | uniq -c | awk '{print $2, $1}'| sort -rk2

# other solutions
# awk '{for(i=1;i<=NF;++i){count[$i]++}} END{for(i in count) {print i,count[i]}}' words.txt | sort -k2nr
# cat words.txt | tr -s ' ' '\n' | sort | uniq -c | sort -r | awk '{ print $2, $1}'
