from googletrans import Translator


def trans_ja2en(career: str, tastes: str, character: str) -> list:
    translator = Translator()

    jp_words = [career, tastes, character]
    en_words = []

    for src in jp_words:
        dst = translator.translate(src, src="ja", dest="en")
        en_words.append(dst.text)

    return en_words


if __name__ == "__main__":
    career = """美夢瞳は、未来を拓くテクノロジーと芸術の融合を追求する才能豊かなエンジニア兼アーティストです。彼女はネオシティの先進的な研究所で働いており、バイオメカニクスと仮想現実の分野で数々の革新的なプロジェクトに携わっています。彼女の専門は、身体と機械の融合によって進化した新しい形態の生命体を創り出すことです。
    美夢は若干神秘的で、その鮮やかな緑色の瞳は彼女が持つ非凡な知性を物語っています。彼女の髪はシルバーで、頭には複雑なサーキットのようなデザインのヘッドギアを身に着けています。身体の一部はバイオニックな要素を持ち、透明な皮膚の下に流れる光る光線が彼女の技術的な進化を象徴しています。"""

    tastes = """美夢はアートとテクノロジーの融合を好み、彼女の自宅アトリエには未知の次元を感じさせるインタラクティブな彫刻やデジタルアートが満ちています。彼女の趣味の一環として、仮想現実空間でのアート体験を提供するプロジェクトにも取り組んでいます。"""

    character = """知的で冷静かつ創造的な美夢は、穏やかな笑顔の裏に深い洞察力と情熱を秘めています。彼女は夢想家でありながらも、現実的な問題にも冷静に取り組む姿勢があります。友好的で協力的な性格で、卓越したリーダーシップとチームワークのスキルを発揮しています。"""

    print(trans_ja2en(career=career, tastes=tastes, character=character))
