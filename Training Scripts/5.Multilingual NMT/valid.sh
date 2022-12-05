#!/bin/bash
echo "export LC_ALL=C">>~/.bashrc
source ~/.bashrc
PWD=/netscratch/zhu/submission
SEC=$PWD/section5
DEVGLOSS=$PWD/data/t2g_phoenix/dev/phoenix_glosses_dev_lower.txt
mosesdecoder=$PWD/mosesdecoder
subword_nmt=$PWD/subword-nmt/subword_nmt
path=$SEC/model/$MODELNAME


cat $1 \
    | sed 's/\@\@ //g' \
    | $mosesdecoder/scripts/tokenizer/detokenizer.perl -l de 2>/dev/null \
    | $mosesdecoder/scripts/generic/multi-bleu-detok.perl $DEVGLOSS \
    | sed -r 's/BLEU = ([0-9.]+),.*/\1/'
