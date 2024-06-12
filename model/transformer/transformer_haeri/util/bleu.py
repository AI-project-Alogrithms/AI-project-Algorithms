"""
@author : Hyunwoong
@when : 2019-12-22
@homepage : https://github.com/gusdnd852
"""
import math
from collections import Counter

import numpy as np


def bleu_stats(hypothesis, reference):  # 가설 (hyphotesis)와 참조(reference)
    """Compute statistics for BLEU."""
    stats = []
    stats.append(len(hypothesis))
    stats.append(len(reference))

    for n in range(1, 5): # 1 ~ 4 gram 측정
        s_ngrams = Counter(
            [tuple(hypothesis[i:i + n]) for i in range(len(hypothesis) + 1 - n)] # n-gram의 빈도를 세기 (range는 n-gram이 가능한 경우의 인덱스까지)
        )
        r_ngrams = Counter(
            [tuple(reference[i:i + n]) for i in range(len(reference) + 1 - n)] # n-gram의 빈도
        )

        stats.append(max([sum((s_ngrams & r_ngrams).values()), 0])) # n-gram이 hyp & ref가 겹치는 경우의 합
        stats.append(max([len(hypothesis) + 1 - n, 0])) # n-gram 측정 시, 가능한 n-gram의 총 개수
    return stats


def bleu(stats):
    """Compute BLEU given n-gram statistics."""
    if len(list(filter(lambda x: x == 0, stats))) > 0: # stats 중 0과 동일한 원소가 있을 때 (즉, 1개도 못맞힌 경우가 있을 때) -> 0점
        return 0
    (c, r) = stats[:2] # c: 기계 번역된 문장(hypothesis)의 길이, r: 참조 문장, 정답(reference)의 길이
    log_bleu_prec = sum(
        [math.log(float(x) / y) for x, y in zip(stats[2::2], stats[3::2])] # stats[2::2]: n-gram 매칭 값)(26행) / stats[3::2]: 가능한 n-gram 총 개수(27행)
    ) / 4. # 모든 로그값을 더하여 평균을 취함
    return math.exp(min([0, 1 - float(r) / c]) + log_bleu_prec) # r이 c보다 길이가 짧을 땐 일부 점수에 보정 계수 (높게끔)를 더해줌


def get_bleu(hypotheses, reference): # 가설과 정답 간 비교
    """Get validation BLEU score for dev set."""
    stats = np.array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0.]) # stats가 뭐임?
    for hyp, ref in zip(hypotheses, reference): # hypotheses와 reference 길이가 다르면, 짧은 길이 까지로 멈춰 # len(list(zip(hypotheses, reference)))
        stats += np.array(bleu_stats(hyp, ref))
    return 100 * bleu(stats)


def idx_to_word(x, vocab): # 디코딩 (주어진 숫자 인덱스들을 단어로 변환해줌)
    words = []
    for i in x:
        word = vocab.itos[i] # index to string
        if '<' not in word: # "<unk>, <pad>, <sos>, <eos>와 같은 스페셜 토큰이 아닐 때
            words.append(word)
    words = " ".join(words)
    return words