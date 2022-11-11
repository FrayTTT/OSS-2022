#!/bin/bash

echo "Каталоги: "
if [[$(ls -l | grep "^d" | wc -l) != "			0"]]
then
	ls -l | grep "^d"
else
	echo "Каталогов нет 0___0"
fi

echo "Обычные файлы: "
if [[ $(ls -l | grep "^-" | wc -l) != "			0" ]]
then
	ls -l | grep "^-"
else
	echo "Обычных файлов нет 0______0"
fi

echo "Символьные ссылки: "
if [[ $(ls -l | grep "^l" | wc -l) !=  "		0" ]]
then
	ls -l | grep "^l"
else
	echo "Символьных ссылок нет 0_____________0"
fi
echo "Символьные устройства: "
if [[ $(ls -l | grep "^c" | wc -l) != "			0" ]]
then
	ls -l | grep "^c"
else
	echo "Символьных устройств нет 0______________________0"
fi

echo "Блочные устройства: " 
if [[ $(ls -l | grep "^b" | wc -l) != "			0" ]]
then
	ls -l | grep "^b"
else
	echo "Блочных устройств нет 0_________________________________0"
fi
