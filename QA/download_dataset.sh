#!/usr/bin/env bash

# Download CMRC2018 dataset
SQUAD_DIR=./CMRC2018
mkdir -p $SQUAD_DIR
wget -O cmrc2018_trial.json https://worksheets.codalab.org/rest/bundles/0xcd4c755829064426896ef942a249aced/contents/blob/
wget -O cmrc2018_train.json https://worksheets.codalab.org/rest/bundles/0x296baa11dfbc4ab08cdeb5b4adf182e2/contents/blob/
wget -O cmrc2018_dev.json https://worksheets.codalab.org/rest/bundles/0xb70e5e281fcd437d9aa8f1c4da107ae4/contents/blob/
