#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Varoluşsal Kriz Fabrikası
Bu kod gerçekten çalışır ve seni düşündürür. Belki de düşündürmez.
"""

import random
import time

krizler = [
    "Ya çay demlenirken ben de eriyorsam?",
    "Kedi miyavlıyorsa, ben de mi miyavlamalıyım?",
    "Evrende sonsuz çay molası varsa neden ben hep iştayım?",
    "Eğer her şey anlamsızsa, neden bu kodu çalıştırıyorum?",
    "Ya ayna bana bakıyorsa ve ben de aynaya bakıyorsam, kim kimi izliyor?",
    "Sadece 5 saniye uyusam, tüm evren yeniden başlar mı?",
    "Neden her şey çok ciddi görünüyor ama aslında komik?",
    "Eğer bu satırı okuyorsan, zaten krizdesin. Tebrikler.",
    "Ya köfte ekmek yerken felsefe yaparsam, köfte de düşünür mü?",
    "Bu repo var olduğuna göre, ben de varım. Ya yoksam?"
]

def kriz_uret():
    print("\n🤯 VAROLUŞSAL KRİZ ÜRETİCİSİ AKTİF 🤯\n")
    time.sleep(1)
    print("Düşünüyorum...")
    time.sleep(2)
    kriz = random.choice(krizler)
    print(f"\n>>> {kriz} <<<\n")
    print("Bu kriz seni değiştirdi mi? Değiştirmedi mi? Zaten fark etmez.\n")
    # gizli not: aGVya2VzIGVzaXQgb2xtYWxpIGFtYSBzZXkgY29rIG9sdSBzaW5pcmkgZGVnaWw= (base64, saklı)

if __name__ == "__main__":
    kriz_uret()
