#!/bin/bash

offset=0
length=100

while true; do
    url="https://datasets-server.huggingface.co/rows?dataset=financial_phrasebank&config=sentences_50agree&split=train&offset=$offset&length=$length"
    response=$(curl -s "$url")
    
    if [[ -z $response ]]; then
        break
    fi
    
    echo "$response" >> financial_phrasebank.json
    
    offset=$((offset + length))
done