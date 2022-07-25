<div align="center">

# EDAKIT: Toolkit for data exploratory analysis
**A tool for analysing sentiment in a given text-based query.**

<!-- *Why not translate it yourself when Google Translate cannot satisfy you❓* -->

[![CircleCI](https://circleci.com/gh/pyurbans/urbans/tree/master.svg?style=svg)](https://circleci.com/gh/pyurbans/urbans/tree/master)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/b4937f1f9fe0477b9fc557cbedf92b24)](https://www.codacy.com/gh/pyurbans/urbans?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=pyurbans/urbans&amp;utm_campaign=Badge_Grade)
<!-- [![Codacy Badge](https://app.codacy.com/project/badge/Coverage/b4937f1f9fe0477b9fc557cbedf92b24)](https://www.codacy.com/gh/pyurbans/urbans?utm_source=github.com&utm_medium=referral&utm_content=pyurbans/urbans&utm_campaign=Badge_Coverage) -->
<!-- [![PyPI version](https://badge.fury.io/py/urbans.svg)](https://badge.fury.io/py/urbans)
[![GitHub release](https://img.shields.io/github/release/pyurbans/urbans.svg)](https://GitHub.com/pyurbans/urbans/releases/) -->
<!-- [![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/pyurbans/urbans/graphs/commit-activity) -->
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://github.com/pyurbans/urbans/blob/master/LICENSE)

</div>

## ⚙️ Installation
```bash
pip install eda
```

<!-- ## ✨ What is good about urbans?
- Rule-based, deterministic translation; unlike Google Translate - giving only 1 non-deterministic result
- Using NLTK parsing interface and is built on top of already-efficient NLTK backend
- Can be used for data augmentation -->

## 📖 Usage
```python
    from eda import SentimentAnalyzer

    sentiment_analyzer = SentimentAnalyzer()
    # Example texts
    texts = [
        "This movie sucks",
        "This one is great",
        "The world is about to end",
    ]  
    pred_results = sentiment_analyzer.get_list_sentiment(texts=texts)
    # This should returns ["negative", "positive", "negative"]
```

## ⚖️ License
This repository is using the Apache 2.0 license that is listed in the repo. Please take a look at [`LICENSE`](https://github.com/TagHubAI/edakit/blob/main/LICENSE) as you wish.

## ✍️ BibTeX
If you wish to cite the framework feel free to use this (but only if you loved it 😊):
```bibtex
@misc{phat2020urbans,
  author = {Truong-Phat Nguyen},
  title = {EDAKIT: Toolkit for data exploratory analysis},
  year = {2022},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/TagHubAI/edakit}}
```

## Contributors:
- Patrick Phat Nguyen