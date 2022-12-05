#!/bin/bash
PWD=/netscratch/zhu/submission
SEC=$PWD/section4
DEVTEXT=$PWD/data/t2g_phoenix/dev/phoenix_sentences_dev_lower_lemm_norm.txt
DEVGLOSS=$PWD/data/t2g_phoenix/dev/phoenix_glosses_dev_lower.txt
mosesdecoder=$PWD/mosesdecoder
MODELNAME=phoenix_baseline_transformer_lemmnorm_pretrain_bpe_32k_dede
subword_nmt=$PWD/subword-nmt/subword_nmt
path=$SEC/model/$MODELNAME
echo "export LC_ALL=C">>~/.bashrc
source ~/.bashrc

cat $1 \
    | sed 's/\@\@ //g' \
    | $mosesdecoder/scripts/recaser/detruecase.perl 2>/dev/null \
    | $mosesdecoder/scripts/tokenizer/detokenizer.perl -l en 2>/dev/null \
    | $mosesdecoder/scripts/generic/multi-bleu-detok.perl $path/dev.tc.$TRG \
    | sed -r 's/BLEU = ([0-9.]+),.*/\1/'
