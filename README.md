# Neural Machine Translation Methods for Translating Text to Sign Language Glosses

This repository provides complementary material to aid the replication of the experiments described in the thesis work as well as ACL'23 publication of [Neural Machine Translation Methods for Translating Text to Sign Language Glosses](https://aclanthology.org/2023.acl-long.700/).



## Content 

The structure of the repository is as following:

 * `Data`: the plain-text versions of the paraller corpora for both the DGS and the Phoenix corpora. It includes the training, dev and test split for both the Phoenix and DGS corpus. Additionally, one can find lemmatized, alphabet normalized and augmented versions as reported in the thesis.  
 * `Training Scripts`: bash files including SLURM commands to execute Marian-NMT for training the NMT transformer models.
 * `Human Evaluations`: streamlit-based evalution interface for collecting the human judgements of selected trained systems
 * `Notebooks`: Python notebooks containing the code for reproducing the experiments, 
   *  mapping of lemmatization algorithm and data statistics analysis
   *  statistical analysis for the results of human evaluation


## Citation

This work has been done with the aim to contribute to the research towards the automatic translation of sign languages. We encourage any further research on top of our work and we are happy to answer related questions. The code is released under the GPL-3.0 License.

If you use the code or derivatives of this repository, please cite:

```
@inproceedings{zhu-etal-2023-neural,
    title = "Neural Machine Translation Methods for Translating Text to Sign Language Glosses",
    author = "Zhu, Dele  and
      Czehmann, Vera  and
      Avramidis, Eleftherios",
    booktitle = "Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)",
    month = jul,
    year = "2023",
    address = "Toronto, Canada",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2023.acl-long.700",
    pages = "12523--12541",
    abstract = "State-of-the-art techniques common to low resource Machine Translation (MT) are applied to improve MT of spoken language text to Sign Language (SL) glosses. In our experiments, we improve the performance of the transformer-based models via (1) data augmentation, (2) semi-supervised Neural Machine Translation (NMT), (3) transfer learning and (4) multilingual NMT. The proposed methods are implemented progressively on two German SL corpora containing gloss annotations. Multilingual NMT combined with data augmentation appear to be the most successful setting, yielding statistically significant improvements as measured by three automatic metrics (up to over 6 points BLEU), and confirmed via human evaluation. Our best setting outperforms all previous work that report on the same test-set and is also confirmed on a corpus of the American Sign Language (ASL).",
}
```

More citation formats [here](https://aclanthology.org/2023.acl-long.700/)

Please note that the corpora ([Phoenix 2014T](https://www-i6.informatik.rwth-aachen.de/~koller/RWTH-PHOENIX-2014-T/) and [DGS Corpus](https://www.sign-lang.uni-hamburg.de/meinedgs/ling/start_en.html)) have their own licenses and any use of them should be conforming with them and include the appropriate citations. 

