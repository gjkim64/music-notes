# Music Theory 화성학 기초

[← Home](README.md)

> 출처: `music-mar22.pptx` (화성학 강의 정리), `music-notes-2026-10.txt` (경과 코드)

음악의 3요소: **선율 (Melody)**, **화성 (Harmony)**, **리듬 (Rhythm)**

---

## 1. C Major Scale (Diatonic Scale) 음의 이름

| 음 | 영문 | 한글 |
| :---: | :--- | :--- |
| 도 | Tonic | 으뜸음 |
| 레 | Supertonic | 웃으뜸음 |
| 미 | Mediant | 가온음 |
| 파 | Subdominant | 버금딸림음 |
| 솔 | Dominant | 딸림음 |
| 라 | Submediant | 버금가온음 |
| 시 | Leading tone | 이끔음 |

---

## 2. 음정 (Intervals)

| 음정 | 온음 | 반음 | 한글 |
| :--- | :---: | :---: | :--- |
| Perfect 1 (P1) | 0 | 0 | 완전 1도 |
| Major 2 (M2) | 1 | 0 | 장 2도 |
| Major 3 (M3) | 2 | 0 | 장 3도 |
| Perfect 4 (P4) | 2 | 1 | 완전 4도 |
| Perfect 5 (P5) | 3 | 1 | 완전 5도 |
| Major 6 (M6) | 4 | 1 | 장 6도 |
| Major 7 (M7) | 5 | 1 | 장 7도 |
| Perfect 8 (P8) | 5 | 2 | 완전 8도 |

**음정 세는 법**
1. "도"는 그냥 음표 수를 센다 (flat, sharp 생각하지 말고).
2. 그 다음 온음/반음이 몇 개인지 본다. (미–파, 시–도는 반음 1개뿐 → 단 2도)
3. **완전** 음정에서 반음 좁아지면 **감 (dim)**, 넓어지면 **증 (aug)**. 두 번이면 **겹 (double)**.
4. **장** 음정에서 반음 좁아지면 **단 (minor)**, 넓어지면 **증**. 단에서 한 번 더 좁아지면 **감**.
5. 온음 3개 = 증4도 / 감5도 = **Tritone**.

**홑음정 / 겹음정**: 1옥타브 이하는 홑음정, 이상은 겹음정 (+7). 예: M2 (도–레) → 한 옥타브 아래 도–레 = M9.

**전위 (Inversion)**: 두 음정을 더하면 9. P↔P, M↔m, a↔d. 예: P4↔P5, M3↔m6, a4↔d5.

### 협화 / 불협화
- 어울리는 음정 (완전 협화): 완전 1, 4, 5, 8도
- 불완전 협화: 장/단 3, 6도
- 안 어울리는 음정: 장/단/증/감 2, 7도
- 어울림은 진동수의 비가 간단해야 함 (1:2 = 한 옥타브, 배음열 1:2:3:4:…:16).

### 음자리표와 악기
- 높은음자리표: G clef — "솔"을 중심으로 그린다.
- 낮은음자리표: F clef — "파"를 중심으로 그린다.
- 현악기 개방현: 바이올린 솔–레–라–미 (각 P5), 비올라·첼로 도–솔–레–라. 기타는 바이올린의 전위처럼 P4 간격.
- 짧을수록 높은 음: 피콜로 – 플루트 – 오보에 – 클라리넷 – 바순 / 트럼펫 – 트롬본 – 튜바.

---

## 3. 3화음 (Triads)

검은 건반 없이 근음 기준으로 쌓으면: **C, Dm, Em, F, G, Am, Bdim** (= B° = Bm(b5))

| 종류 | 구성 | 느낌 | 표기 예 |
| :--- | :--- | :--- | :--- |
| Major | M3 + m3 | 밝고 단순 | C |
| Minor | m3 + M3 | 어둡고 단단 (월광) | Cm |
| Diminished | m3 + m3 | 긴장, 불안 | Cdim = C° = Cm(b5) |
| Augmented | M3 + M3 | 미스테리 | Caug = C+ = C(#5) |
| Suspended 4 | P4 + M2 | 곡 끝 리딩, 공간감 | Csus4 |

> 각각 다른 근음에 대해 똑같이 연습하고, 귀로 구분하는 연습이 필요.

### 코드의 연속과 전위
- 반주 시 왼손이 일정한 음역 안에 머물도록 한다.
- 이어질 때 **공통음은 최대한 유지**하고, 나머지를 움직이며 전위(Inversion)를 쓴다.
- 기본 위치: C / 1st inversion: C/E / 2nd inversion: C/G

**예: 사랑하기 때문에** — `C – F – Em – Dm – G – C`

**예: Pachelbel Canon**
```
C – G – Am – Em – F – C – Dm – Gsus – G        (기본)
C – G/B – Am – Em/G – F – C/E – Dm – Gsus – G  (전위로 베이스 하행)
```

---

## 4. 7화음 (Seventh Chords)

| 코드 | 구성 / 설명 |
| :--- | :--- |
| Cmaj7 (M7) | 장3화음 + 근음에서 반음 1개 내려온 음 |
| C7 (dom7) | 장3화음 + 근음에서 온음 1개 내려온 음 |
| Cmaj7(#5) | maj7에서 5음 # |
| Cm7 (C-7) | 단3화음 + dom7 |
| CmM7 | 단3화음 + 근음에서 반음 내려온 음 |
| Cdim7 (C°7) | m3 + m3 + m3 |
| Cm7(b5) (Cø) | m3 + m3 + M3 |
| C7(#5) | dom7에서 5음 # |
| C7(b5) | dom7에서 5음 b |
| C7sus4 | sus4 + dom7 |
| C6 | 도–미–솔–라 |
| Cm6 | 도–미b–솔–라 |

**7th 코드 칠 때**: 오른손은 근음을 빼고 3, 5, 7음, 왼손은 근음.
예 (사랑하기 때문에): `Cmaj7 – Fmaj7 – Em7 – Dm7 – G7 – Cmaj7 …`

**다이어토닉 7화음**
- C부터: Cmaj7, Dm7, Em7, Fmaj7, G7, Am7, Bm7(b5)
- F부터: Fmaj7, Gm7, Am7, Bbmaj7, C7, Dm7, Em7(b5)
- 연습: 하나의 근음으로 12가지 코드 잡기 (F: Fmaj7, F7, Fmaj7(#5), Fm7, FmM7, F°7, Fm7(b5), F7(#5), F7(b5), F7sus4, F6, Fm6)

---

## 5. 세컨더리 도미넌트 (Secondary Dominant)

다이어토닉 7화음 (C 기준):

| I | IIm | IIIm | IV | V | VIm | VIIm(b5) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Cmaj7 | Dm7 | Em7 | Fmaj7 | G7 | Am7 | Bm7(b5) |

각 코드의 **완전 5도 위 음을 근음으로 하는 dom7 코드**를 그 코드 앞에 연결/인트로로 쓴다.

| 대상 | V7/II | V7/III | V7/IV | V7/V | V7/VI |
| :--- | :---: | :---: | :---: | :---: | :---: |
| 코드 | A7 | B7 | C7 | D7 | E7 |

- G7은 이미 Primary dominant (V7/I).
- 예: `C – E7 – Am7 – C7 – Fmaj7 – D7 – G7sus – G7`
- C 중심으로 정리했지만 다른 키에서도 같은 관계.

---

## 6. 대리 코드 (Substitute Chords)

- **주화음**: I, IV, V (+ subdominant minor IVm)
- **부화음**: II, III, VI, VII — 주화음과 공통음이 2개 이상이면 대신할 수 있다.

| 기능 | 주화음 | 대체 코드 (C 기준) | 대체 코드 (도수) |
| :--- | :--- | :--- | :--- |
| 1: Tonic | Cmaj7 | Em7 (3음 공통), Am7 (4음 공통), F#m7(b5) | IIIm7, VIm7, #IVm7(b5) |
| 4: Subdominant | Fmaj7 | Dm7, F#m7(b5), Bbmaj7, G7sus4 | IIm7, #IVm7(b5), bVIImaj7, V7sus4 |
| 5: Dominant | G7 | Bm7(b5), Db7 | VIIm7(b5), bII7 |
| 4*: SD minor | Fm7 (Fm6) | Dbmaj7, Dm7(b5), Abmaj7, Ab7, Bb7 | bIImaj7, IIm7(b5), bVImaj7, bVI7, bVII7 |

- 화음 안에 증4/감5 (온음 3개) 음정이 있으면 **Tritone이 있다**고 하며 불안감이 있다.
- 4와 4*는 비슷하나 음색 차이가 있음 (4*는 minor 풍).

---

## 7. 종지 (Cadence)

코드는 **동적 → 정적**, **불안 → 안정**으로 해결된다. Tritone을 없애 주는 것이 해결.

| 종지 | 진행 | 예 | 메모 |
| :--- | :--- | :--- | :--- |
| Dominant | V → I | G7 → C | G7의 시–파(d5) tritone이 C의 도–미(M3)로 해결 |
| Subdominant | IV → I | Fmaj7 → C | tritone 없음, 이미 안정적 |
| SD minor | IVm → I | Fm7 → C, Fm6 → C | Fm6의 증4도로 큰 해결감 |
| SD / D | IV → V → I | Fmaj7 → G7 → C, Dm7 → G7 → C | Dm7은 Fmaj7의 대리 코드 |
| SD / SD minor | IV → IVm → I | Fmaj7 → Fm7 → C, Dm7 → Dm7(b5) → C | |
| SD minor / D | IVm → V → I | Fm7 → G7 → C, Dm7(b5) → G7 → C (II–V–I) | |
| SD / SDm / D | IV → IVm → V → I | Fmaj7 → Fm7 → G7 → C | Dm7 → Dm7(b5) → G7 → C |
| Deceptive (거짓 종지) | V → (I 대신 대리 코드) | F → G7 → F#m7(b5) | 끝에 다른 길로 간다 |

---

## 8. 경과 코드 (Passing Chords)

- **I 코드로 갈 때** 앞에 V7 또는 IV7을 쓴다. 예: `C → E7 → Am`
- **코드에서 코드로 갈 때** 베이스가 반음/온음으로 이어지게 전위를 쓴다.
  - C → F: `C – C/E – F` (E가 F로 이끈다)
  - Am → C: `Am – Am/B – C` (B가 C로 이끈다)
- **순차 진행 코드** (예: G → Am)는 근음만 반음 올린 증3화음을 끼운다: `G – G#(G+) – A`
- **II–V–I**: 목표 코드 앞에 IIm7 → V7. 예: `Gm7 – C7 – F`
