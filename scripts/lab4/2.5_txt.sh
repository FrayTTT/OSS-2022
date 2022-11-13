#!/bin/bash

find ~ -name ".txt" > /tmp/temp.txt 2>/dev/null
cat /tmp/temp.txt | wc -l
du -h /tmp/temp.txt | cut -f1
rm /tmp/temp.txt
